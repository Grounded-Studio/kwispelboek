"""Generates the static Kwispelboek / Wagbook site (NL at /, EN at /en/).

Run:  python -I _build/build.py
Jekyll (GitHub Pages) skips folders starting with "_", so this script is not published.
"""
from html import escape
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blog_content import ARTICLES, BLOG_T, DATE as BLOG_DATE  # noqa: E402

SITE = Path(__file__).resolve().parent.parent
DOMAIN = "https://kwispelboek.app"
UPDATED = {"nl": "5 november 2026", "en": "5 November 2026"}
MAIL = "contact@grounded-studio.app"

PLAY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.18 23.75c.36.2.78.22 1.15.07l12.5-11.5L13.67 9 3.18 23.75Z" fill="#EA4335"/>'
            '<path d="M20.82 10.26a1.5 1.5 0 0 0 0-2.52l-3.17-1.84-3.64 3.35 3.64 3.35 3.17-1.34Z" fill="#FBBC04"/>'
            '<path d="M3.18.25 13.67 9l3.16-2.9L4.33.18C3.96.03 3.54.05 3.18.25Z" fill="#4285F4"/>'
            '<path d="M3.18.25C2.49.64 2 1.38 2 2.25v19.5c0 .87.49 1.61 1.18 2l10.49-12L3.18.25Z" fill="#34A853"/></svg>')
MAIL_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m4 7 8 6 8-6"/></svg>')

T = {
 "nl": {
  "name": "Kwispelboek", "other": "en", "path": "/", "privacy": "/privacy/",
  "title": "Kwispelboek – Huisdier logboek voor hond, kat & meer",
  "desc": "Vaccinaties, ontworming, medicijnen en dierenartsbezoeken van al je huisdieren op één plek, met herinneringen op tijd. Zonder account. Binnenkort voor Android.",
  "nav": [("#functies", "Functies"), ("#schermen", "Screenshots"), ("#pro", "Prijzen"), ("#faq", "Vragen"), ("/blog/", "Blog")],
  "h1": 'Zorg voor je maatje,<br><span class="accent">zonder iets te vergeten</span>',
  "lead": "Kwispelboek houdt vaccinaties, ontworming, medicijnen, dierenartsbezoeken en gewicht van al je dieren bij en herinnert je op het juiste moment. Afvinken met een pootstempel, een agenda met een kleur per dier en confetti als alles gedaan is. Geen account: alles blijft op je telefoon.",
  "soon_small": "BINNENKORT OP", "soon": "Google Play",
  "notify": "Hou me op de hoogte", "notify_subject": "Laat me weten wanneer Kwispelboek uitkomt",
  "badges": ["Gratis te gebruiken", "Geen account", "Geen advertenties"],
  "alt_today": "Kwispelboek: het Vandaag-scherm met voortgangsring, je dieren en wat er nu moet gebeuren",
  "alt_profile": "Kwispelboek: profiel van een hond met de tabbladen Zorg, Gezondheid en Paspoort",
  "trust": [("🔒", "Je gegevens blijven op je telefoon"), ("🚫", "Geen advertenties of tracking"), ("🐾", "Hond, kat, konijn, vogel & meer"), ("💬", "Nederlands & Engels")],
  "feat_eyebrow": "Functies", "feat_title": "Alles voor de gezondheid van je dier, op één plek",
  "feat_lead": "Voor baasjes die rust willen: niets vergeten, alles bij de hand, en het mag best een beetje leuk zijn.",
  "features": [
   ("☀️", "", "Vandaag in één oogopslag", "Een voortgangsring, ‘Nu doen’ op volgorde van belang, wat er later vandaag komt en een balk met de hele week. Voor al je dieren samen.", False),
   ("🐾", "amber", "Afvinken is een feestje", "Tik op ✓ en er verschijnt een pootstempel. Alles gedaan? Dan komen er confetti en een blije Kwispel, en houd je je reeks bij.", False),
   ("➕", "", "Alles noteren met één knop", "De grote gele + in het midden: vaccinatie, medicijn, gewicht, dierenartsbezoek of paspoort scannen. Kies wat, kies voor wie, klaar.", False),
   ("🔔", "", "Herinneringen op tijd", "Vaccinaties, ontworming en vlooien- en tekenmiddel met herhaalschema. Een melding vooraf én op de dag zelf.", False),
   ("📅", "sage", "Agenda per maand", "Gekleurde stipjes per dier laten zien wat er wanneer komt, met verjaardagen en adoptiedagen erbij.", False),
   ("🎨", "amber", "Elk dier een eigen kleur", "Kies uit acht kleuren. Die kleur komt overal terug: op de kaart, in de agenda en bij de taken.", False),
   ("💊", "sage", "Medicijnen & kuren", "Dosis met − en +, tijden per dag, doorlopend of als kuur. Je ziet in blokjes hoe ver de kuur is.", False),
   ("🩺", "sage", "Dierenarts & kosten", "Bezoeken met reden, notities, foto’s en kosten, met het totaal van dit jaar. Je dierenarts bellen of de route openen in één tik.", False),
   ("⚖️", "amber", "Gewichtsgrafiek", "Weeg regelmatig en zie veranderingen op tijd. In kilo’s, of in grammen voor vogels.", False),
   ("🪪", "", "Paspoort & tijdlijn", "Chipnummer en gegevens als een overzichtelijk paspoortkaartje, en een tijdlijn met alles wat er gebeurde.", False),
   ("🎉", "amber", "Verjaardagen met feestkaartje", "Op de verjaardag of adoptiedag een feestkaart op Vandaag, en een vrolijk kaartje om te delen.", False),
   ("📱", "sage", "Widgets op je beginscherm", "Een groot en een klein widget met je voortgang, je dieren en wat het eerst moet. Zonder de app te openen.", False),
   ("✈️", "", "Reischecklist", "Op vakantie met je dier? Zie in één oogopslag of chip, paspoort en rabiësvaccinatie op tijd in orde zijn.", False),
   ("📣", "", "Vermist-poster", "Is je dier zoek? Maak in een minuut een poster met foto, kenmerken en je telefoonnummer om te printen of te delen.", False),
   ("💾", "amber", "Back-up in één bestand", "Alle dieren, gegevens en foto’s in één bestand. Zet het in Google Drive en zet het terug op een nieuwe telefoon.", False),
   ("📄", "", "PDF voor de dierenarts", "Een overzichtelijk document met chipnummer, vaccinaties met batchnummers, medicijnen, gewicht en recente bezoeken.", True),
   ("🧑‍🍼", "", "Overzicht voor de oppas", "Voer, karakter, medicijnen en contactgegevens in één PDF voor de oppas of het pension.", True),
   ("📷", "", "Paspoort scannen", "Fotografeer de vaccinatiepagina en de datums en batchnummers worden ingevuld. Jij controleert altijd eerst.", True),
  ],
  "spots": [
   ("today", "Vandaag", "Open de app en je weet wat er moet gebeuren",
    "Een persoonlijk blok met hoe ver je bent, en daaronder één lijst op volgorde van belang. Wat te laat is staat bovenaan.",
    ["Voortgangsring: ‘2 van 5 gedaan’", "Je dieren met een bolletje voor wat openstaat", "‘Deze week’ met stipjes per dier"]),
   ("done", "Beloning", "Alles gedaan? Dan is het feest",
    "Elke keer dat je iets afvinkt verschijnt een pootstempel. Is alles voor vandaag klaar, dan komen er confetti en een blije Kwispel.",
    ["Afvinken met één tik, ongedaan maken kan altijd", "Je reeks: zoveel dagen op rij alles op tijd", "Kwispel, onze mascotte, viert het met je mee"]),
   ("profile", "Per dier", "Alles over je dier, in drie tabbladen",
    "Een banner in de eigen kleur van je dier, vier handige knoppen en de tabbladen Zorg, Gezondheid en Paspoort. Geen eindeloos scrollen meer.",
    ["Zorg: vaccinaties, ontworming en medicijnkuren", "Gezondheid: gewicht, dierenarts en kosten", "Paspoort: chip en gegevens als een kaartje"]),
   ("agenda", "Agenda", "De hele maand, met een stipje per dier",
    "Zie in één oogopslag wanneer welke behandeling komt. Tik op een dag en je ziet wat er gepland staat.",
    ["Verjaardagen en adoptiedagen staan er vanzelf bij", "Medicijnkuren per dag", "Een rustige dag? Dan ligt Kwispel te slapen"]),
   ("card", "Feest", "Verjaardag? Maak er een kaartje van",
    "Op de verjaardag of adoptiedag van je dier staat er een feestkaart op Vandaag. Maak in één tik een vrolijk kaartje om te delen met familie en vrienden.",
    ["Kies uit vier kleuren", "Delen via WhatsApp, Instagram of mail", "Een melding op de dag zelf, zodat je het niet vergeet"]),
  ],
  "shots_eyebrow": "Screenshots", "shots_title": "Zo ziet Kwispelboek eruit",
  "shots_lead": "Echte schermen uit de app, met voorbeelddieren.",
  "shots": [("today", "Vandaag"), ("pets", "Mijn dieren"), ("profile", "Profiel"), ("health", "Gezondheid"), ("agenda", "Agenda"), ("add", "Snel noteren"), ("party", "Verjaardag"), ("done", "Alles gedaan!")],
  "kw_eyebrow": "Kwispel", "kw_title": "Maak kennis met Kwispel",
  "kw_lead": "Onze mascotte laat zich zien op de momenten die ertoe doen.",
  "kw": [("happy", "Blij", "Als alles voor vandaag gedaan is"), ("sleeping", "Slaapt", "Op een rustige dag zonder taken"), ("curious", "Nieuwsgierig", "Als er nog iets ingevuld kan worden"), ("party", "Feest", "Op verjaardagen en adoptiedagen")],
  "pro_eyebrow": "Prijzen", "pro_title": "Gratis beginnen, PRO als je meer wilt",
  "pro_lead": "Alle logboeken, herinneringen, de gewichtsgrafiek en back-ups zijn gratis. PRO neem je per maand of per jaar en zeg je op elk moment op via Google Play.",
  "free_title": "Gratis", "free_price": "Voor altijd, zonder advertenties",
  "free_items": ["Tot 2 huisdieren", "Alle herinneringen en medicijnschema’s", "Agenda, widgets en feestkaartjes", "Dierenartsbezoeken, gewicht en tijdlijn", "Reischecklist en vermist-poster", "Back-ups en 1 foto per bezoek"],
  "pro_title2": "PRO", "pro_price": "€ 2,99 per maand of € 19,99 per jaar",
  "pro_items": ["Onbeperkt aantal huisdieren", "PDF-overzicht voor de dierenarts", "Overzicht voor de oppas of het pension", "Reischecklist als PDF", "Paspoort, rekening of medicijnetiket scannen met AI", "Onbeperkt foto’s per bezoek"],
  "faq_eyebrow": "Vragen", "faq_title": "Veelgestelde vragen",
  "faq": [
   ("Is Kwispelboek gratis?", "Ja. Je kunt gratis tot 2 dieren bijhouden met alle logboeken, herinneringen, de gewichtsgrafiek, de reischecklist, de vermist-poster en back-ups. PRO voegt onbeperkt dieren en foto’s, de PDF-overzichten en scannen met AI toe."),
   ("Heb ik een account nodig?", "Nee. Kwispelboek werkt zonder account en bewaart alles op je eigen telefoon. Wij hebben geen server die je gegevens ontvangt."),
   ("Wat gebeurt er als ik een nieuwe telefoon krijg?", "Maak in Instellingen een back-up: één bestand met alle dieren, gegevens en foto’s. Bewaar het in Google Drive of mail het naar jezelf, en zet het terug op je nieuwe telefoon."),
   ("Hoe werken de herinneringen?", "Per vaccinatie of behandeling kies je hoe ver vooraf je een melding wilt, plus een melding op de dag zelf op het tijdstip dat je instelt. Medicijnen herinneren je op elk tijdstip, met de knoppen ‘Gegeven’ en ‘Later’."),
   ("Is het alleen voor honden?", "Nee. Kwispelboek is er voor honden, katten, konijnen, vogels en andere huisdieren. Suggesties voor vaccinaties passen zich aan per diersoort, en vogels weeg je in grammen."),
   ("Wat gebeurt er met mijn foto bij scannen met AI?", "Alleen als je zelf kiest om te scannen, wordt die ene foto naar Google (Gemini) gestuurd om de tekst te lezen. Wij bewaren hem niet. Je controleert het resultaat altijd voordat er iets wordt opgeslagen."),
   ("Geeft Kwispelboek medisch advies?", "Nee. Kwispelboek helpt je bijhouden en onthouden. Voorgestelde schema’s zijn gangbare standaarden; volg altijd het advies van je eigen dierenarts."),
   ("Wanneer komt Kwispelboek uit?", "Kwispelboek komt binnenkort in Google Play voor Android. In het Engels heet de app Wagbook. Een iPhone-versie staat nog niet gepland."),
  ],
  "cta_title": "Binnenkort in Google Play",
  "cta_text": "Kwispelboek zit in de laatste testfase. Wil je weten wanneer de app uitkomt? Stuur ons een berichtje.",
  "foot_by": "Gemaakt door", "foot_privacy": "Privacy", "foot_contact": "Contact",
  "skip": "Naar de inhoud",
  "switch_label": "Taal",
 },
 "en": {
  "name": "Wagbook", "other": "nl", "path": "/en/", "privacy": "/en/privacy/",
  "title": "Wagbook – Pet health log for dogs, cats & more",
  "desc": "Vaccinations, deworming, medication and vet visits for all your pets in one place, with reminders on time. No account. Coming soon to Android.",
  "nav": [("#features", "Features"), ("#screens", "Screenshots"), ("#pro", "Pricing"), ("#faq", "FAQ"), ("/en/blog/", "Blog")],
  "h1": 'Care for your buddy,<br><span class="accent">without forgetting a thing</span>',
  "lead": "Wagbook keeps track of vaccinations, deworming, medication, vet visits and weight for all your pets and reminds you at the right moment. Tick things off with a paw stamp, see a calendar with a colour per pet and get confetti when everything is done. No account: everything stays on your phone.",
  "soon_small": "COMING SOON TO", "soon": "Google Play",
  "notify": "Let me know", "notify_subject": "Let me know when Wagbook launches",
  "badges": ["Free to use", "No account", "No ads"],
  "alt_today": "Wagbook: the Today screen with progress ring, your pets and what to do now",
  "alt_profile": "Wagbook: a dog's profile with the tabs Care, Health and Passport",
  "trust": [("🔒", "Your data stays on your phone"), ("🚫", "No ads, no tracking"), ("🐾", "Dogs, cats, rabbits, birds & more"), ("🌍", "English & Dutch")],
  "feat_eyebrow": "Features", "feat_title": "Everything for your pet’s health, in one place",
  "feat_lead": "For owners who want peace of mind: nothing forgotten, everything at hand, and a little fun along the way.",
  "features": [
   ("☀️", "", "Today at a glance", "A progress ring, ‘To do now’ with the most important first, what’s coming later today and a strip with the whole week. For all your pets together.", False),
   ("🐾", "amber", "Ticking off is a treat", "Tap ✓ and a paw stamp appears. All done? Then there’s confetti and a happy Kwispel, and you keep your streak going.", False),
   ("➕", "", "Log anything with one button", "The big yellow + in the middle: vaccination, medicine, weight, vet visit or passport scan. Choose what, choose for whom, done.", False),
   ("🔔", "", "Reminders on time", "Vaccinations, deworming and flea & tick treatments with repeat schedules. A reminder in advance and on the day itself.", False),
   ("📅", "sage", "Monthly calendar", "Coloured dots per pet show what’s coming when, with birthdays and adoption days included.", False),
   ("🎨", "amber", "A colour for every pet", "Choose from eight colours. It shows up everywhere: on the card, in the calendar and on the tasks.", False),
   ("💊", "sage", "Medication & courses", "Dose with − and +, times of day, ongoing or as a course. Little blocks show how far along the course is.", False),
   ("🩺", "sage", "Vet & costs", "Visits with reason, notes, photos and costs, with this year’s total. Call your vet or get directions in one tap.", False),
   ("⚖️", "amber", "Weight chart", "Weigh regularly and spot changes early. In kilos, or in grams for birds.", False),
   ("🪪", "", "Passport & timeline", "Microchip number and details as a tidy passport card, and a timeline of everything that happened.", False),
   ("🎉", "amber", "Birthdays with a party card", "On a birthday or adoption day a party card on Today, and a cheerful card to share.", False),
   ("📱", "sage", "Home screen widgets", "A large and a small widget with your progress, your pets and what comes first. Without opening the app.", False),
   ("✈️", "", "Travel checklist", "Going abroad with your pet? See at a glance whether microchip, passport and rabies vaccination are in order in time.", False),
   ("📣", "", "Missing poster", "Pet gone missing? Make a poster with photo, markings and your phone number in a minute, to print or share.", False),
   ("💾", "amber", "Backup in one file", "All pets, records and photos in one file. Keep it in Google Drive and restore it on a new phone.", False),
   ("📄", "", "PDF for the vet", "A clear overview with microchip number, vaccinations with batch numbers, medication, weight and recent visits.", True),
   ("🧑‍🍼", "", "Pet sitter overview", "Food, character, medication and contact details in one PDF for the sitter or boarding kennel.", True),
   ("📷", "", "Scan the pet passport", "Photograph the vaccination page and the dates and batch numbers are filled in. You always check first.", True),
  ],
  "spots": [
   ("today", "Today", "Open the app and you know what to do",
    "A personal header showing how far you are, and below it one list with the most important first. Anything overdue sits at the top.",
    ["Progress ring: ‘2 of 5 done’", "Your pets, with a badge for what’s still open", "‘This week’ with a dot per pet"]),
   ("done", "Reward", "All done? Time to celebrate",
    "Every time you tick something off, a paw stamp appears. When everything for today is done, there’s confetti and a happy Kwispel.",
    ["Tick off in one tap, undo any time", "Your streak: so many days in a row, all on time", "Kwispel, our mascot, celebrates with you"]),
   ("profile", "Per pet", "Everything about your pet, in three tabs",
    "A banner in your pet’s own colour, four handy buttons and the tabs Care, Health and Passport. No more endless scrolling.",
    ["Care: vaccinations, deworming and medication courses", "Health: weight, vet and costs", "Passport: microchip and details as a card"]),
   ("agenda", "Calendar", "The whole month, with a dot per pet",
    "See at a glance when each treatment is due. Tap a day to see what’s planned.",
    ["Birthdays and adoption days added automatically", "Medication courses per day", "A quiet day? Kwispel takes a nap"]),
   ("card", "Party", "Birthday? Make it a card",
    "On your pet’s birthday or adoption day there’s a party card on Today. Make a cheerful card in one tap to share with family and friends.",
    ["Choose from four colours", "Share via WhatsApp, Instagram or email", "A reminder on the day, so you never forget"]),
  ],
  "shots_eyebrow": "Screenshots", "shots_title": "See Wagbook in action",
  "shots_lead": "Real screens from the app, with example pets.",
  "shots": [("today", "Today"), ("pets", "My pets"), ("profile", "Pet profile"), ("health", "Health"), ("agenda", "Calendar"), ("add", "Quick log"), ("party", "Birthday"), ("done", "All done!")],
  "kw_eyebrow": "Kwispel", "kw_title": "Meet Kwispel",
  "kw_lead": "Our mascot shows up at the moments that matter.",
  "kw": [("happy", "Happy", "When everything for today is done"), ("sleeping", "Sleeping", "On a quiet day without tasks"), ("curious", "Curious", "When there’s still something to fill in"), ("party", "Party", "On birthdays and adoption days")],
  "pro_eyebrow": "Pricing", "pro_title": "Free to start, PRO when you need more",
  "pro_lead": "All logs, reminders, the weight chart and backups are free. PRO is available monthly or yearly, and you can cancel anytime in Google Play.",
  "free_title": "Free", "free_price": "Forever, without ads",
  "free_items": ["Up to 2 pets", "All reminders and medication schedules", "Calendar, widgets and party cards", "Vet visits, weight and timeline", "Travel checklist and missing poster", "Backups and 1 photo per visit"],
  "pro_title2": "PRO", "pro_price": "€2.99 a month or €19.99 a year",
  "pro_items": ["Unlimited pets", "PDF overview for the vet", "Overview for the pet sitter or kennel", "Travel checklist as PDF", "Scan a passport, invoice or medicine label with AI", "Unlimited photos per visit"],
  "faq_eyebrow": "FAQ", "faq_title": "Frequently asked questions",
  "faq": [
   ("Is Wagbook free?", "Yes. You can keep up to 2 pets for free with all logs, reminders, the weight chart, the travel checklist, the missing poster and backups. PRO adds unlimited pets and photos, the PDF overviews and AI scanning."),
   ("Do I need an account?", "No. Wagbook works without an account and stores everything on your own phone. We have no server that receives your data."),
   ("What happens when I get a new phone?", "Make a backup in Settings: one file with all pets, records and photos. Keep it in Google Drive or email it to yourself, and restore it on your new phone."),
   ("How do the reminders work?", "For each vaccination or treatment you choose how far in advance you want a reminder, plus one on the day itself at the time you set. Medication reminds you at every time of day, with ‘Given’ and ‘Later’ buttons."),
   ("Is it only for dogs?", "No. Wagbook is for dogs, cats, rabbits, birds and other pets. Vaccination suggestions adapt to the species, and birds are weighed in grams."),
   ("What happens to my photo when I scan with AI?", "Only when you choose to scan, that one photo is sent to Google (Gemini) to read the text. We do not store it. You always check the result before anything is saved."),
   ("Does Wagbook give medical advice?", "No. Wagbook helps you keep track and remember. Suggested schedules are common defaults; always follow the advice of your own vet."),
   ("When is Wagbook available?", "Wagbook is coming soon to Google Play for Android. In Dutch the app is called Kwispelboek. An iPhone version is not planned yet."),
  ],
  "cta_title": "Coming soon to Google Play",
  "cta_text": "Wagbook is in its final testing phase. Want to know when it launches? Send us a message.",
  "foot_by": "Made by", "foot_privacy": "Privacy", "foot_contact": "Contact",
  "skip": "Skip to content",
  "switch_label": "Language",
 },
}

PRIVACY = {
 "nl": {
  "title": "Privacybeleid – Kwispelboek",
  "desc": "Privacybeleid van Kwispelboek, het huisdier-logboek van Grounded Studio. Geen account, geen advertenties, geen tracking: je gegevens blijven op je telefoon.",
  "h1": "Privacybeleid",
  "meta": f"Laatst bijgewerkt: {UPDATED['nl']} · Grounded Studio, Nederland",
  "summary": "Kort gezegd: alles wat je invoert blijft op je eigen telefoon. De app heeft geen account, geen server en geen tracking.",
  "sections": [
   ("Wie zijn wij", ["Kwispelboek (in het Engels: Wagbook) is een app van Grounded Studio uit Nederland. Voor vragen over privacy kun je mailen naar <a href=\"mailto:%s\">%s</a>." % (MAIL, MAIL)]),
   ("Opgeslagen op je telefoon", ["Je hebt geen account nodig. Alles wat je invoert, zoals dieren, vaccinaties, medicijnen, dierenartsbezoeken, gewicht, reizen, foto’s en je eigen naam en telefoonnummer, wordt alleen op deze telefoon opgeslagen. Wij hebben geen server die het ontvangt en kunnen er niet bij."]),
   ("Geen advertenties, geen tracking", ["De app toont geen advertenties, bevat geen analytics of tracking en gebruikt geen advertentie-ID."]),
   ("Herinneringen en widget", ["Herinneringen worden op je telefoon zelf ingepland. De widget op je beginscherm toont gegevens uit de app op je eigen telefoon. Daarvoor wordt niets naar ons verstuurd."]),
   ("Delen en PDF’s", ["Een PDF (bijvoorbeeld voor de dierenarts of de oppas), een vermist-poster of een back-upbestand gaat alleen naar de plek waar jij het zelf naartoe stuurt of opslaat. Staat de Android-back-up aan in je telefooninstellingen, dan kan Android ook een kopie van de app-gegevens in je eigen Google-account bewaren."]),
   ("Scannen met AI (optioneel, PRO)", ["Alleen als je zelf kiest om een dierenpaspoort, rekening of medicijnetiket te scannen, wordt die ene foto via een beveiligde verbinding naar Google (Gemini API) gestuurd om de tekst te lezen. Wij bewaren de foto niet. Je controleert het resultaat altijd voordat er iets wordt opgeslagen. Voordat je voor het eerst scant, vraagt de app je toestemming."]),
   ("Aankopen", ["Kwispelboek PRO koop je via Google Play. Google regelt de betaling; de app krijgt alleen te zien of PRO actief is. Wij ontvangen geen betaalgegevens."]),
   ("Toestemmingen", ["De app vraagt alleen wat nodig is: toestemming voor meldingen (herinneringen) en internet (scannen met AI en aankopen). Foto’s maak of kies je via de standaardcamera en fotokiezer van Android; de app krijgt alleen de foto die jij kiest."]),
   ("Deze website", ["We tellen bezoeken aan kwispelboek.app met Cloudflare Web Analytics, zonder cookies: welke pagina is bekeken, van welke site je kwam, browser, type apparaat, land en hoe snel de pagina laadde. Cloudflare gebruikt geen cookies of fingerprinting en maakt geen profiel van je; wij zien alleen totalen. Dit gaat over de website, niet over de app."]),
   ("Je gegevens verwijderen", ["Via Instellingen → Alle gegevens verwijderen wis je alles van deze telefoon. De app verwijderen doet hetzelfde. Omdat wij geen gegevens van je hebben, hoef je ons daarvoor niets te vragen."]),
   ("Kinderen", ["Kwispelboek is niet speciaal voor kinderen gemaakt en verzamelt van niemand persoonsgegevens."]),
   ("Wijzigingen", ["Als dit beleid verandert, passen we de datum bovenaan aan. Bij belangrijke wijzigingen melden we dat ook in de app."]),
  ],
  "back": "← Terug naar Kwispelboek",
 },
 "en": {
  "title": "Privacy policy – Wagbook",
  "desc": "Privacy policy of Wagbook (Kwispelboek), the pet health log by Grounded Studio. No account, no ads, no tracking: your data stays on your phone.",
  "h1": "Privacy policy",
  "meta": f"Last updated: {UPDATED['en']} · Grounded Studio, the Netherlands",
  "summary": "In short: everything you enter stays on your own phone. The app has no account, no server and no tracking.",
  "sections": [
   ("Who we are", ["Wagbook (Kwispelboek in Dutch) is an app by Grounded Studio from the Netherlands. For privacy questions, email <a href=\"mailto:%s\">%s</a>." % (MAIL, MAIL)]),
   ("Stored on your phone", ["You don’t need an account. Everything you enter, such as pets, vaccinations, medication, vet visits, weights, trips, photos and your own name and phone number, is stored only on this phone. We have no server that receives it and we cannot access it."]),
   ("No ads, no tracking", ["The app shows no ads, contains no analytics or tracking, and does not use the advertising ID."]),
   ("Reminders and widget", ["Reminders are scheduled on your phone itself. The home screen widget shows data from the app on your own phone. Nothing is sent to us for this."]),
   ("Sharing and PDFs", ["A PDF (for example for the vet or a pet sitter), a missing poster or a backup file goes only where you send or save it yourself. If Android backup is switched on in your phone settings, Android may also keep a copy of the app data in your own Google account."]),
   ("Scanning with AI (optional, PRO)", ["Only when you choose to scan a pet passport, invoice or medicine label, that one photo is sent over a secure connection to Google (Gemini API) to read the text. We do not store the photo. You always check the result before anything is saved. The app asks for your consent before your first scan."]),
   ("Purchases", ["Wagbook PRO is bought through Google Play. Google handles the payment; the app only learns whether PRO is active. We receive no payment details."]),
   ("Permissions", ["The app only asks for what it needs: permission for notifications (reminders) and internet (AI scanning and purchases). You take or pick photos through Android’s standard camera and photo picker; the app only receives the photo you choose."]),
   ("This website", ["We count visits to kwispelboek.app with Cloudflare Web Analytics, without cookies: which page was viewed, the site you came from, browser, device type, country and how fast the page loaded. Cloudflare does not use cookies or fingerprinting and does not build a profile of you; we only see totals. This is about the website, not the app."]),
   ("Deleting your data", ["Settings → Delete all data removes everything from this phone. Uninstalling the app does the same. Because we hold no data about you, there is nothing you need to ask us."]),
   ("Children", ["Wagbook is not made specifically for children and collects no personal data from anyone."]),
   ("Changes", ["If this policy changes, we update the date at the top. Important changes are also announced in the app."]),
  ],
  "back": "← Back to Wagbook",
 },
}


def head(lang, title, desc, path, alt_path, og, extra=""):
    other = T[lang]["other"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{DOMAIN}{path}">
<link rel="alternate" hreflang="{lang}" href="{DOMAIN}{path}">
<link rel="alternate" hreflang="{other}" href="{DOMAIN}{alt_path}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{path if lang == 'nl' else alt_path}">
<meta name="theme-color" content="#F2F6F9">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/nunito-black.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/nunito-semibold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v=3">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{T[lang]['name']}">
<meta property="og:locale" content="{'nl_NL' if lang == 'nl' else 'en_US'}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-{og}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{extra}<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "fd857a6afd0c4ecdbaa74eafc299b943"}}'></script><!-- End Cloudflare Web Analytics -->
</head>
"""


def header(lang, path_here, path_other, nav=True):
    t = T[lang]
    links = "".join(f'<a href="{h}">{escape(l)}</a>' for h, l in t["nav"]) if nav else ""
    nl_href, en_href = (path_here, path_other) if lang == "nl" else (path_other, path_here)
    cur_nl = ' aria-current="true"' if lang == "nl" else ""
    cur_en = ' aria-current="true"' if lang == "en" else ""
    return f"""<body>
<a class="skip" href="#main">{t['skip']}</a>
<header class="top" id="top">
  <div class="wrap">
    <a class="brand" href="{t['path']}"><img src="/assets/img/icon.webp" alt="" width="36" height="36">{t['name']}</a>
    <nav class="nav" aria-label="Menu">{links}</nav>
    <div class="lang" role="group" aria-label="{t['switch_label']}"><a href="{nl_href}" hreflang="nl" lang="nl"{cur_nl}>NL</a><a href="{en_href}" hreflang="en" lang="en"{cur_en}>EN</a></div>
  </div>
</header>
"""


def crumbs(lang, trail):
    """trail: [(name, path), ...] from home to the current page. Returns (html, json-ld script)."""
    items = []
    for i, (name, path) in enumerate(trail):
        last = i == len(trail) - 1
        items.append(f'<li><span aria-current="page">{escape(name)}</span></li>' if last
                     else f'<li><a href="{path}">{escape(name)}</a></li>')
    html = f'<nav class="crumbs" aria-label="{"Kruimelpad" if lang == "nl" else "Breadcrumb"}"><ol>{"".join(items)}</ol></nav>'
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": DOMAIN + path} for i, (name, path) in enumerate(trail)]}
    return html, f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'


def footer(lang):
    t = T[lang]
    return f"""<footer>
  <div class="wrap">
    <span>© 2026 {t['name']} · {t['foot_by']} <a href="https://grounded-studio.app/">Grounded Studio</a></span>
    <nav aria-label="Footer"><a href="{BLOG_T[lang]['path']}">Blog</a><a href="{t['privacy']}">{t['foot_privacy']}</a><a href="mailto:{MAIL}">{t['foot_contact']}</a><a href="https://grounded-studio.app/">Grounded Studio</a></nav>
  </div>
</footer>
<script>
(function(){{var h=document.getElementById('top');function s(){{h.classList.toggle('scrolled',window.scrollY>8)}}s();window.addEventListener('scroll',s,{{passive:true}});
try{{document.querySelectorAll('.lang a').forEach(function(a){{a.addEventListener('click',function(){{localStorage.setItem('kb-lang',a.getAttribute('hreflang'))}})}})}}catch(e){{}}}})();
</script>
</body>
</html>
"""


def phone(img, alt, cls="", w=540, h=1205, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<div class="phone {cls}"><img src="/assets/img/{img}.webp" alt="{escape(alt)}" width="{w}" height="{h}" {load} decoding="async"></div>'


def home(lang):
    t = T[lang]
    other = T[t["other"]]
    ids = {"nl": ("functies", "schermen"), "en": ("features", "screens")}[lang]
    subject = escape(t["notify_subject"]).replace(" ", "%20")
    soon = f'<span class="soon">{PLAY_SVG}<span><small>{t["soon_small"]}</small><b>{t["soon"]}</b></span></span>'
    notify = f'<a class="btn btn-ghost" href="mailto:{MAIL}?subject={subject}">{MAIL_SVG}{t["notify"]}</a>'
    ld = {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": t["name"],
        "alternateName": other["name"], "operatingSystem": "Android", "applicationCategory": "LifestyleApplication",
        "description": t["desc"], "url": DOMAIN + t["path"], "image": f"{DOMAIN}/assets/img/og-{lang}.jpg",
        "inLanguage": ["nl", "en"], "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "author": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    site_ld = {"@context": "https://schema.org", "@type": "WebSite", "name": t["name"], "url": DOMAIN + t["path"],
               "inLanguage": lang, "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"}}
    extra = (f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>\n'
             f'<script type="application/ld+json">{json.dumps(site_ld, ensure_ascii=False)}</script>\n'
             + crumbs(lang, [(t["name"], t["path"])])[1])
    if lang == "nl":
        # First visit with a non-Dutch browser: offer English once (no forced redirect).
        extra += ("<script>try{if(!localStorage.getItem('kb-lang')&&!/^nl\\b/i.test(navigator.language||'')"
                  "&&!/bot|crawl|spider/i.test(navigator.userAgent)){localStorage.setItem('kb-lang','en');location.replace('/en/')}}catch(e){}</script>\n")

    feats = "".join(
        f'<div class="card {tone}"><div class="ico" aria-hidden="true">{ico}</div><h3>{escape(title)}'
        f'{" <span class=\"pro\">PRO</span>" if pro else ""}</h3><p>{escape(desc)}</p></div>'
        for ico, tone, title, desc, pro in t["features"])
    spots = ""
    for i, (img, eb, title, text, bullets) in enumerate(t["spots"]):
        lis = "".join(f"<li>{escape(b)}</li>" for b in bullets)
        spots += (f'<div class="spot{" flip" if i % 2 else ""}"><div class="text"><span class="eyebrow">{escape(eb)}</span>'
                  f'<h2>{escape(title)}</h2><p class="lead" style="margin-top:14px">{escape(text)}</p><ul>{lis}</ul></div>'
                  f'{phone(f"{img}-{lang}", f"{t["name"]}: {title}")}</div>')
    shots = "".join(f'<figure>{phone(f"{img}-{lang}", f"{t["name"]}: {cap}")}<figcaption>{escape(cap)}</figcaption></figure>'
                    for img, cap in t["shots"])
    free = "".join(f"<li>{escape(x)}</li>" for x in t["free_items"])
    pro = "".join(f"<li>{escape(x)}</li>" for x in t["pro_items"])
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in t["faq"])
    trust = "".join(f'<li><span aria-hidden="true">{i}</span>{escape(x)}</li>' for i, x in t["trust"])
    badges = "".join(f"<span><i></i>{escape(b)}</span>" for b in t["badges"])
    kw = "".join(f'<figure class="kw-{m}"><img src="/assets/img/kwispel-{m}.svg" alt="" width="150" height="150" loading="lazy">'
                 f'<figcaption><b>{escape(n)}</b><span>{escape(d)}</span></figcaption></figure>' for m, n, d in t["kw"])

    return head(lang, t["title"], t["desc"], t["path"], other["path"], lang, extra) + header(lang, t["path"], other["path"]) + f"""<main id="main">
<section class="hero" style="padding-top:48px">
  <div class="wrap">
    <div>
      <img class="hero-icon" src="/assets/img/icon.webp" alt="{t['name']}" width="72" height="72">
      <h1>{t['h1']}</h1>
      <p class="lead">{escape(t['lead'])}</p>
      <div class="actions">{soon}{notify}</div>
      <div class="badges">{badges}</div>
    </div>
    <div class="phones">
      {phone(f"today-{lang}", t['alt_today'], "main", eager=True)}
      {phone(f"profile-{lang}", t['alt_profile'], "back")}
    </div>
  </div>
</section>

<div class="trust"><div class="wrap"><ul>{trust}</ul></div></div>

<section id="{ids[0]}">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{t['feat_eyebrow']}</span><h2>{escape(t['feat_title'])}</h2><p class="lead">{escape(t['feat_lead'])}</p></div>
    <div class="grid">{feats}</div>
  </div>
</section>

<section style="padding-top:20px">
  <div class="wrap">{spots}</div>
</section>

<section class="kw-band" style="padding-top:40px">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{t['kw_eyebrow']}</span><h2>{escape(t['kw_title'])}</h2><p class="lead">{escape(t['kw_lead'])}</p></div>
    <div class="kw">{kw}</div>
  </div>
</section>

<section id="{ids[1]}" style="padding-top:40px">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{t['shots_eyebrow']}</span><h2>{escape(t['shots_title'])}</h2><p class="lead">{escape(t['shots_lead'])}</p></div>
    <div class="shots" tabindex="0" aria-label="{escape(t['shots_title'])}">{shots}</div>
  </div>
</section>

<section id="pro" style="padding-top:40px">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{t['pro_eyebrow']}</span><h2>{escape(t['pro_title'])}</h2><p class="lead">{escape(t['pro_lead'])}</p></div>
    <div class="plans">
      <div class="plan"><h3>{t['free_title']}</h3><p class="price">{escape(t['free_price'])}</p><ul>{free}</ul></div>
      <div class="plan pro-plan"><h3>{t['name']} {t['pro_title2']}</h3><p class="price">{escape(t['pro_price'])}</p><ul>{pro}</ul></div>
    </div>
  </div>
</section>

<section id="faq" style="padding-top:40px">
  <div class="wrap">
    <div class="head"><span class="eyebrow">{t['faq_eyebrow']}</span><h2>{escape(t['faq_title'])}</h2></div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section style="padding-top:20px;padding-bottom:40px">
  <div class="wrap">
    <div class="cta">
      <img class="cta-kw" src="/assets/img/kwispel-party.svg" alt="" width="130" height="130" loading="lazy">
      <h2>{escape(t['cta_title'])}</h2>
      <p>{escape(t['cta_text'])}</p>
      <div class="actions">{soon}<a class="btn btn-primary" href="mailto:{MAIL}?subject={subject}">{MAIL_SVG}{t['notify']}</a></div>
    </div>
  </div>
</section>
</main>
""" + footer(lang)


def privacy(lang):
    p = PRIVACY[lang]
    t = T[lang]
    other = T[t["other"]]
    body = "".join(f"<h2>{escape(h)}</h2>" + "".join(f"<p>{x}</p>" for x in paras) for h, paras in p["sections"])
    c_html, c_ld = crumbs(lang, [(t["name"], t["path"]), (p["h1"], t["privacy"])])
    return head(lang, p["title"], p["desc"], t["privacy"], other["privacy"], lang, c_ld) + header(lang, t["privacy"], other["privacy"], nav=False) + f"""<main id="main" class="legal">
{c_html}
<h1 style="margin-top:18px">{p['h1']}</h1>
<p class="meta">{p['meta']}</p>
<p class="summary">{p['summary']}</p>
{body}
</main>
""" + footer(lang)


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "h2":
            out.append(f"<h2>{escape(val)}</h2>")
        elif kind == "p":
            out.append(f"<p>{val}</p>")
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>")
        elif kind == "tip":
            out.append(f'<aside class="tip"><span aria-hidden="true">💡</span><p>{val}</p></aside>')
    return "\n".join(out)


def blog_index(lang):
    t, b = T[lang], BLOG_T[lang]
    other = T[t["other"]]
    ob = BLOG_T[t["other"]]
    c_html, c_ld = crumbs(lang, [(t["name"], t["path"]), (b["h1"], b["path"])])
    items = [{"@type": "ListItem", "position": i + 1, "url": f'{DOMAIN}{b["path"]}{a[lang]["slug"]}/', "name": a[lang]["title"]}
             for i, a in enumerate(ARTICLES)]
    list_ld = {"@context": "https://schema.org", "@type": "Blog", "name": f'{t["name"]} {b["h1"]}', "url": DOMAIN + b["path"],
               "inLanguage": lang, "publisher": {"@type": "Organization", "name": "Grounded Studio"},
               "blogPost": [{"@type": "BlogPosting", "headline": a[lang]["title"], "url": f'{DOMAIN}{b["path"]}{a[lang]["slug"]}/',
                             "datePublished": BLOG_DATE} for a in ARTICLES]}
    extra = c_ld + f'<script type="application/ld+json">{json.dumps(list_ld, ensure_ascii=False)}</script>\n'
    del items
    cards = "".join(
        f'<a class="post-card" href="{b["path"]}{a[lang]["slug"]}/"><span class="post-ico" aria-hidden="true">{a["emoji"]}</span>'
        f'<h2>{escape(a[lang]["title"])}</h2><p>{escape(a[lang]["desc"])}</p>'
        f'<span class="post-meta">{b["read"].format(n=a[lang]["read"])} · {b["more"]} →</span></a>' for a in ARTICLES)
    also = ""
    if b["also_links"]:
        also = (f'<h2 class="also">{escape(b["also"])}</h2><ul class="also-list">'
                + "".join(f'<li><a href="{u}">{escape(n)}</a></li>' for u, n in b["also_links"]) + "</ul>")
    return head(lang, b["title"], b["desc"], b["path"], ob["path"], lang, extra) + header(lang, b["path"], ob["path"], nav=False) + f"""<main id="main" class="blog">
<div class="wrap">
{c_html}
<h1>{b['h1']}</h1>
<p class="lead" style="margin-top:12px">{escape(b['lead'])}</p>
<div class="post-grid">{cards}</div>
{also}
</div>
</main>
""" + footer(lang)


def article(lang, a):
    t, b = T[lang], BLOG_T[lang]
    o = t["other"]
    ob = BLOG_T[o]
    art = a[lang]
    path = f'{b["path"]}{art["slug"]}/'
    other_path = f'{ob["path"]}{a[o]["slug"]}/'
    c_html, c_ld = crumbs(lang, [(t["name"], t["path"]), (b["h1"], b["path"]), (art["title"], path)])
    art_ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": art["title"], "description": art["desc"],
              "inLanguage": lang, "datePublished": BLOG_DATE, "dateModified": BLOG_DATE,
              "mainEntityOfPage": DOMAIN + path, "url": DOMAIN + path, "image": f"{DOMAIN}/assets/img/og-{lang}.jpg",
              "author": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
              "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/",
                            "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/icon-512.png"}},
              "about": {"@type": "MobileApplication", "name": t["name"], "url": DOMAIN + t["path"]}}
    extra = (c_ld + f'<script type="application/ld+json">{json.dumps(art_ld, ensure_ascii=False)}</script>\n'
             + '<meta property="article:published_time" content="' + BLOG_DATE + '">\n')
    related = "".join(f'<li><a href="{b["path"]}{x[lang]["slug"]}/">{x["emoji"]} {escape(x[lang]["title"])}</a></li>'
                      for x in ARTICLES if x is not a)
    title = f'{art["title"]} | {t["name"]}'
    return head(lang, title, art["desc"], path, other_path, lang, extra).replace(
        '<meta property="og:type" content="website">', '<meta property="og:type" content="article">') + header(lang, path, other_path, nav=False) + f"""<main id="main" class="legal article">
{c_html}
<p class="post-emoji" aria-hidden="true">{a['emoji']}</p>
<h1>{escape(art['title'])}</h1>
<p class="meta">{b['published']} <time datetime="{BLOG_DATE}">{b['date']}</time> · {b['read'].format(n=art['read'])} · <a href="{other_path}" hreflang="{o}" lang="{o}">{b['other_lang']}</a></p>
<p class="summary">{escape(art['desc'])}</p>
{render_body(art['body'])}
<div class="post-cta">
  <img src="/assets/img/kwispel-happy.svg" alt="" width="96" height="96" loading="lazy">
  <div><h2>{escape(b['cta_title'])}</h2><p>{escape(b['cta_text'])}</p>
  <a class="btn btn-primary" href="{t['path']}">{escape(b['cta_btn'])}</a></div>
</div>
<h2>{escape(b['related'])}</h2>
<ul class="related">{related}</ul>
</main>
""" + footer(lang)


def llms_txt():
    lines = ["# Kwispelboek (Wagbook)", "",
             "> Kwispelboek (Dutch) / Wagbook (English) is an Android app by Grounded Studio (the Netherlands) to keep track of "
             "pet health: vaccinations, deworming, flea & tick treatments, medication courses, vet visits and costs, weight, "
             "travel checklists and a missing-pet poster, with reminders. No account: all data stays on the phone. "
             "Free for up to 2 pets; PRO (€2.99/month or €19.99/year) adds unlimited pets, PDF overviews and AI passport scanning. "
             "Coming soon to Google Play.", "",
             "## Main pages",
             f"- [Kwispelboek (Dutch)]({DOMAIN}/): features, screenshots, pricing and FAQ",
             f"- [Wagbook (English)]({DOMAIN}/en/): features, screenshots, pricing and FAQ",
             f"- [Privacy policy (Dutch)]({DOMAIN}/privacy/)",
             f"- [Privacy policy (English)]({DOMAIN}/en/privacy/)", "",
             "## Blog (Dutch)"]
    lines += [f'- [{a["nl"]["title"]}]({DOMAIN}/blog/{a["nl"]["slug"]}/): {a["nl"]["desc"]}' for a in ARTICLES]
    lines += ["", "## Blog (English)"]
    lines += [f'- [{a["en"]["title"]}]({DOMAIN}/en/blog/{a["en"]["slug"]}/): {a["en"]["desc"]}' for a in ARTICLES]
    lines += ["", "## Optional",
              "- [Grounded Studio](https://grounded-studio.app/): the studio behind the app",
              "- Contact: contact@grounded-studio.app", ""]
    return "\n".join(lines)


NOT_FOUND = f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina niet gevonden – Kwispelboek</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/site.css?v=3">
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "fd857a6afd0c4ecdbaa74eafc299b943"}}'></script><!-- End Cloudflare Web Analytics -->
</head>
<body>
<main class="legal" style="text-align:center;padding-top:96px">
<img src="/assets/img/kwispel-curious.svg" alt="" width="140" height="140" style="margin:0 auto 16px">
<h1>Oeps, deze pagina is weggelopen</h1>
<p class="meta">This page ran off. Let’s go back home.</p>
<div class="actions" style="justify-content:center;margin-top:24px">
<a class="btn btn-primary" href="/">Naar Kwispelboek</a><a class="btn btn-ghost" href="/en/">English</a>
</div>
</main>
</body>
</html>
"""

MANIFEST = {
    "name": "Kwispelboek", "short_name": "Kwispelboek", "start_url": "/", "display": "browser",
    "background_color": "#F2F6F9", "theme_color": "#2B7A9E",
    "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
}

SITEMAP_URLS = [("/", "/en/"), ("/privacy/", "/en/privacy/"), ("/blog/", "/en/blog/")] + [
    (f"/blog/{a['nl']['slug']}/", f"/en/blog/{a['en']['slug']}/") for a in ARTICLES]


def sitemap():
    rows = []
    for nl, en in SITEMAP_URLS:
        for loc in (nl, en):
            rows.append(f"""  <url>
    <loc>{DOMAIN}{loc}</loc>
    <lastmod>2026-11-05</lastmod>
    <xhtml:link rel="alternate" hreflang="nl" href="{DOMAIN}{nl}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{en}"/>
  </url>""")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")


def write(rel, text):
    f = SITE / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8", newline="\n")


write("index.html", home("nl"))
write("en/index.html", home("en"))
write("privacy/index.html", privacy("nl"))
write("en/privacy/index.html", privacy("en"))
write("blog/index.html", blog_index("nl"))
write("en/blog/index.html", blog_index("en"))
for a in ARTICLES:
    write(f"blog/{a['nl']['slug']}/index.html", article("nl", a))
    write(f"en/blog/{a['en']['slug']}/index.html", article("en", a))
write("llms.txt", llms_txt())
write("404.html", NOT_FOUND)
write("site.webmanifest", json.dumps(MANIFEST, indent=2))
write("sitemap.xml", sitemap())
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
write("CNAME", "kwispelboek.app\n")
print("built")
