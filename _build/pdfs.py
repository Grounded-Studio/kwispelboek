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


def _keep_if_same(root, target):
    """Chrome stamps every PDF with the time it was made. When nothing else changed, put the
    committed file back, so an unchanged checklist is not seen as a change (sitemap, IndexNow)."""
    import re
    rel = target.relative_to(root).as_posix()
    old = subprocess.run(["git", "-C", str(root), "show", f"HEAD:{rel}"], capture_output=True)
    if old.returncode != 0:
        return
    stamp = re.compile(rb"/(CreationDate|ModDate) \(D:[^)]*\)")
    if stamp.sub(b"", old.stdout) == stamp.sub(b"", target.read_bytes()):
        target.write_bytes(old.stdout)


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
                _keep_if_same(root, target)
                print("pdf", target.relative_to(root.parent))
        finally:
            srv.shutdown()
