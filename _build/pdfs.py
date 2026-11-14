"""Renders the printable checklists to PDF with headless Chrome. The print sources live in _print/
(Jekyll skips folders starting with "_", so they are never published); the PDFs go next to the pages."""
import functools
import http.server
import subprocess
import threading
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def _serve(root):
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(_Quiet, directory=str(root)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def make(site, en_site, extra):
    if not Path(CHROME).exists():
        print("pdfs: Chrome not found, skipped")
        return
    for lang, root in (("nl", Path(site)), ("en", Path(en_site))):
        srv = _serve(root)
        try:
            for c in extra.CHECKLISTS:
                slug = c[lang]["slug"]
                target = root / "checklists" / f"{slug}.pdf"
                target.parent.mkdir(parents=True, exist_ok=True)
                url = f"http://127.0.0.1:{srv.server_address[1]}/_print/{slug}.html"
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                                "--virtual-time-budget=4000", f"--print-to-pdf={target}", url],
                               check=True, capture_output=True)
                print("pdf", target.relative_to(root.parent))
        finally:
            srv.shutdown()
