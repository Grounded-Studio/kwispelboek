"""Guides for pet owners: one question per page, with a summary table, FAQ (FAQPage) and named sources.

Health facts on these pages come only from the sources listed with each guide. Do not add numbers or
schedules that are not in those sources.
"""
from html import escape
import json

DATE = "2026-11-18"

SRC = {
    "esccap_nl": ("ESCCAP – Hoe bescherm ik mijn huisdieren tegen parasieten (Nederlandse aanbevelingen)",
                  "https://www.esccap.org/uploads/docs/kob7oqrb_0635_ESCCAP_Recommendations__Dutch_update_v3.pdf"),
    "knmvd": ("KNMvD – De 12 meest gestelde vragen over vaccineren (2021)",
              "https://www.knmvd.nl/app/uploads/sites/1/2021/05/QA-vaccinatie-dierenartsnl.pdf"),
    "wsava": ("WSAVA – 2024 Guidelines for the Vaccination of Dogs and Cats",
              "https://wsava.org/wp-content/uploads/2024/05/2024-Guidelines-for-the-Vaccination-of-Dogs-and-Cats.pdf"),
}

TX = {
    "nl": {
        "name": "Gidsen", "path": "/gidsen/",
        "title": "Gidsen voor baasjes: zorg voor hond en kat | Kwispelboek",
        "desc": "Heldere antwoorden op vragen over de zorg voor je hond of kat, zoals ontwormen en vaccineren, met bronnen van dierenartsenorganisaties.",
        "lead": "Korte, heldere antwoorden op vragen die elk baasje heeft. Met de bron erbij, zodat je weet waar het advies vandaan komt.",
        "open": "Lezen",
        "glance": "In het kort",
        "faq": "Veelgestelde vragen",
        "sources": "Bronnen",
        "related": "Lees ook",
        "updated": "Bijgewerkt op",
        "disclaimer": "Deze gids is algemene informatie en geen vervanging voor advies van je dierenarts. Elk dier is anders: je dierenarts kijkt naar leeftijd, gezondheid, leefstijl en waar je woont.",
        "cta_title": "Laat Kwispelboek je eraan herinneren",
        "cta_btn": "Gratis in Google Play",
    },
    "en": {
        "name": "Guides", "path": "/en/guides/",
        "title": "Guides for pet owners: dog and cat care | Wagbook",
        "desc": "Clear answers to questions about caring for your dog or cat, such as deworming and vaccinations, with sources from veterinary organisations.",
        "lead": "Short, clear answers to questions every pet owner has. With the source included, so you know where the advice comes from.",
        "open": "Read",
        "glance": "At a glance",
        "faq": "Frequently asked questions",
        "sources": "Sources",
        "related": "Read next",
        "updated": "Updated on",
        "disclaimer": "This guide is general information and does not replace advice from your vet. Every pet is different: your vet looks at age, health, lifestyle and where you live.",
        "cta_title": "Let Wagbook remind you",
        "cta_btn": "Free on Google Play",
    },
}

GUIDES = [
    {
        "key": "deworm", "emoji": "🪱", "sources": ["esccap_nl"],
        "related": {"nl": [("/gidsen/vaccinatieschema-pup-kitten/", "Vaccinatieschema voor pup en kitten"),
                           ("/gidsen/vlooien-en-teken-hond-kat/", "Vlooien en teken: hoe vaak behandelen?"),
                           ("/voor/hond/", "Kwispelboek voor je hond"), ("/voor/kat/", "Kwispelboek voor je kat"),
                           ("/checklists/puppy-in-huis/", "Checklist: puppy in huis")],
                    "en": [("/en/guides/puppy-kitten-vaccination-schedule/", "Puppy and kitten vaccination schedule"),
                           ("/en/guides/fleas-and-ticks-dog-cat/", "Fleas and ticks: how often to treat?"),
                           ("/en/for/dogs/", "Wagbook for your dog"), ("/en/for/cats/", "Wagbook for your cat"),
                           ("/en/checklists/new-puppy/", "Checklist: new puppy")]},
        "nl": {
            "slug": "hoe-vaak-ontwormen-hond-kat",
            "title": "Hoe vaak moet je je hond of kat ontwormen? | Kwispelboek",
            "h1": "Hoe vaak moet je je hond of kat ontwormen?",
            "short": "Hoe vaak ontwormen?",
            "desc": "Hoe vaak ontworm je een pup, kitten of volwassen hond of kat? Het advies van ESCCAP op een rij, met een overzichtstabel en veelgestelde vragen.",
            "intro": "Een volwassen hond of kat ontworm je volgens de Europese parasitologen van ESCCAP gemiddeld 4 keer per jaar. Pups en kittens ontworm je veel vaker: elke 14 dagen, tot 14 dagen na het spenen. Woont er een jong kind of iemand met een minder goed werkende afweer in huis, dan is vaker ontwormen raadzaam, tot zelfs maandelijks.",
            "table": (["Wie", "Advies van ESCCAP"], [
                ["Pup", "Vanaf 14 dagen oud elke 14 dagen tegen spoelwormen, tot 14 dagen na het spenen"],
                ["Kitten", "Vanaf 21 dagen oud elke 14 dagen tegen spoelwormen, tot 14 dagen na het spenen"],
                ["Moederdier", "Op dezelfde momenten als de jongen, tot twee weken na het spenen"],
                ["Volwassen hond of kat", "Gemiddeld 4 keer per jaar"],
                ["Jonge kinderen of verminderde afweer in huis", "Vaker, tot zelfs maandelijks"],
                ["Liever niet standaard ontwormen", "Regelmatig ontlastingsonderzoek; bij een positieve uitslag ontwormen"],
            ]),
            "sections": [
                ("Waarom ontwormen belangrijk is", [
                    "Spoelwormen (Toxocara) leven in de darmen van honden en katten. Een besmet dier scheidt eitjes uit met de ontlasting, en zo raakt de omgeving besmet: de tuin, het park of de zandbak.",
                    "ESCCAP noemt twee doelen van ontwormen: ziekte bij je dier voorkomen, en voorkomen dat de omgeving besmet raakt met Toxocara-eitjes. Spoelwormen kunnen ook mensen besmetten. Daarom is het advies strenger als er jonge kinderen of mensen met een verminderde afweer in huis wonen.",
                ]),
                ("Pups en kittens: vaak en vroeg", [
                    "ESCCAP adviseert pups vanaf 14 dagen en kittens vanaf 21 dagen elke 14 dagen te ontwormen tegen spoelwormen, tot 14 dagen na het spenen. Het moederdier wordt op dezelfde momenten meebehandeld.",
                    "Haal je een pup of kitten in huis, vraag dan aan de fokker of het asiel wanneer er voor het laatst ontwormd is en met welk middel. Zo weet je dierenarts waar je verder gaat.",
                ]),
                ("Volwassen honden en katten: gemiddeld 4 keer per jaar", [
                    "Voor een volwassen hond of kat is het uitgangspunt van ESCCAP gemiddeld 4 keer per jaar. Dat vermindert de uitscheiding van spoelwormeitjes. Het is een gemiddelde: de juiste frequentie hangt af van je dier en je situatie.",
                    "Wanneer vaker? Bij jonge kinderen of mensen met een minder goed werkende afweer in huis is vaker ontwormen raadzaam, tot zelfs maandelijks. Ook jachthonden, honden die eerder longworm hadden en dieren die rauw vlees eten vragen om een aanpak op maat. In gebieden waar de vossenlintworm voorkomt, adviseert ESCCAP jagende honden en honden die kleine prooidieren eten maandelijks te behandelen met praziquantel. Je dierenarts weet of dat in jouw regio speelt.",
                ]),
                ("Ontlastingsonderzoek als alternatief", [
                    "Wil je niet standaard volgens schema ontwormen? Dan kun je volgens ESCCAP ook regelmatig de ontlasting laten onderzoeken. Is de uitslag positief, dan ontworm je alsnog. Bespreek met je dierenarts hoe vaak dat onderzoek nodig is.",
                ]),
                ("Hygiëne helpt ook", [
                    "Ruim de ontlasting van je hond of kat direct op, in de tuin en tijdens het uitlaten, en was daarna je handen. Gooi ontlasting niet bij het groenafval of op de composthoop.",
                    "Dek zandbakken af als ze niet gebruikt worden, was groente en fruit goed en geef geen rauw vlees. Let vooral bij kinderen op goede handhygiëne.",
                    "ESCCAP raadt aan om de parasietenbestrijding minstens elke 12 maanden met je dierenarts te bespreken, bijvoorbeeld tijdens de jaarlijkse controle.",
                ]),
            ],
            "faq": [
                ("Hoe vaak moet ik mijn volwassen hond ontwormen?", "Volgens ESCCAP gemiddeld 4 keer per jaar. Met jonge kinderen of iemand met een verminderde afweer in huis is vaker raadzaam, tot maandelijks. Je dierenarts stemt het af op je hond."),
                ("Hoe vaak moet ik mijn kat ontwormen?", "Ook voor een volwassen kat is het uitgangspunt gemiddeld 4 keer per jaar. Kittens ontworm je vanaf 21 dagen oud elke 14 dagen, tot 14 dagen na het spenen."),
                ("Wanneer ontworm je een pup voor het eerst?", "ESCCAP adviseert te beginnen als de pup 14 dagen oud is, en daarna elke 14 dagen tot 14 dagen na het spenen. Het moederdier wordt tegelijk behandeld."),
                ("Kan ik in plaats van ontwormen de ontlasting laten onderzoeken?", "Ja. Regelmatig ontlastingsonderzoek is volgens ESCCAP een alternatief. Bij een positieve uitslag moet je dier wel ontwormd worden."),
                ("Waarom vaker ontwormen als er kleine kinderen zijn?", "Spoelwormen kunnen ook mensen besmetten. Daarom adviseert ESCCAP in die huishoudens vaker te ontwormen, tot zelfs maandelijks."),
            ],
            "app": "Kwispelboek zet een ontwormingsschema voor je klaar en stuurt je op tijd een herinnering. Zo weet je altijd wanneer de volgende keer is, ook als je het schema met je dierenarts hebt aangepast.",
        },
        "en": {
            "slug": "how-often-deworm-dog-cat",
            "title": "How often should you deworm your dog or cat? | Wagbook",
            "h1": "How often should you deworm your dog or cat?",
            "short": "How often to deworm?",
            "desc": "How often should you deworm a puppy, kitten, adult dog or cat? The ESCCAP advice in one place, with a summary table and frequently asked questions.",
            "intro": "According to the European parasitology experts at ESCCAP, you deworm an adult dog or cat on average 4 times a year. Puppies and kittens are dewormed much more often: every 14 days, until 14 days after weaning. If a young child or someone with a weakened immune system lives with you, more frequent deworming is advisable, up to monthly.",
            "table": (["Who", "ESCCAP advice"], [
                ["Puppy", "From 14 days old, every 14 days against roundworm, until 14 days after weaning"],
                ["Kitten", "From 21 days old, every 14 days against roundworm, until 14 days after weaning"],
                ["Mother", "At the same times as the young, until two weeks after weaning"],
                ["Adult dog or cat", "On average 4 times a year"],
                ["Young children or weakened immunity at home", "More often, up to monthly"],
                ["Rather not deworm routinely", "Regular faecal testing; deworm if the result is positive"],
            ]),
            "sections": [
                ("Why deworming matters", [
                    "Roundworms (Toxocara) live in the intestines of dogs and cats. An infected pet passes eggs in its faeces, and that is how the environment becomes contaminated: the garden, the park or the sandpit.",
                    "ESCCAP names two goals of deworming: preventing disease in your pet, and preventing the environment from being contaminated with Toxocara eggs. Roundworms can also infect people. That is why the advice is stricter when young children or people with weakened immunity live in the household.",
                ]),
                ("Puppies and kittens: early and often", [
                    "ESCCAP advises deworming puppies from 14 days and kittens from 21 days old every 14 days against roundworm, until 14 days after weaning. The mother is treated at the same times.",
                    "Bringing home a puppy or kitten? Ask the breeder or shelter when it was last dewormed and with which product. That way your vet knows where to continue.",
                ]),
                ("Adult dogs and cats: on average 4 times a year", [
                    "For an adult dog or cat, ESCCAP’s starting point is on average 4 times a year. This reduces the shedding of roundworm eggs. It is an average: the right frequency depends on your pet and your situation.",
                    "When more often? With young children or people with weakened immunity at home, more frequent deworming is advisable, up to monthly. Hunting dogs, dogs that have had lungworm and pets fed raw meat also need a tailored approach. In areas where the fox tapeworm occurs, ESCCAP advises treating hunting dogs and dogs that eat small prey monthly with praziquantel. Your vet knows whether that applies where you live.",
                ]),
                ("Faecal testing as an alternative", [
                    "Rather not deworm on a fixed schedule? According to ESCCAP you can also have your pet’s faeces tested regularly. If the result is positive, you deworm after all. Discuss with your vet how often testing is needed.",
                ]),
                ("Hygiene helps too", [
                    "Pick up your dog’s or cat’s poo straight away, in the garden and on walks, and wash your hands afterwards. Don’t put faeces in the green waste or on the compost heap.",
                    "Cover sandpits when they are not in use, wash fruit and vegetables well and don’t feed raw meat. Pay extra attention to hand hygiene with children.",
                    "ESCCAP recommends discussing parasite control with your vet at least every 12 months, for example during the yearly check-up.",
                ]),
            ],
            "faq": [
                ("How often should I deworm my adult dog?", "According to ESCCAP, on average 4 times a year. With young children or someone with weakened immunity at home, more often is advisable, up to monthly. Your vet will tailor it to your dog."),
                ("How often should I deworm my cat?", "For an adult cat the starting point is also on average 4 times a year. Kittens are dewormed from 21 days old every 14 days, until 14 days after weaning."),
                ("When do you deworm a puppy for the first time?", "ESCCAP advises starting when the puppy is 14 days old, then every 14 days until 14 days after weaning. The mother is treated at the same time."),
                ("Can I have my pet’s faeces tested instead of deworming?", "Yes. Regular faecal testing is an alternative according to ESCCAP. If the result is positive, your pet does need to be dewormed."),
                ("Why deworm more often when there are young children?", "Roundworms can also infect people. That is why ESCCAP advises deworming more often in those households, up to monthly."),
            ],
            "app": "Wagbook sets up a deworming schedule for you and reminds you in time. So you always know when the next one is due, even after adjusting the schedule with your vet.",
        },
    },
    {
        "key": "vacc", "emoji": "💉", "sources": ["knmvd", "wsava"],
        "related": {"nl": [("/gidsen/hoe-vaak-ontwormen-hond-kat/", "Hoe vaak moet je je hond of kat ontwormen?"),
                           ("/hulpmiddelen/21-dagenregel/", "Rekenhulp: de 21-dagenregel voor op reis"),
                           ("/checklists/puppy-in-huis/", "Checklist: puppy in huis"),
                           ("/voor/hond/", "Kwispelboek voor je hond"), ("/voor/kat/", "Kwispelboek voor je kat")],
                    "en": [("/en/guides/how-often-deworm-dog-cat/", "How often should you deworm your dog or cat?"),
                           ("/en/tools/21-day-rule/", "Calculator: the 21-day rule for travel"),
                           ("/en/checklists/new-puppy/", "Checklist: new puppy"),
                           ("/en/for/dogs/", "Wagbook for your dog"), ("/en/for/cats/", "Wagbook for your cat")]},
        "nl": {
            "slug": "vaccinatieschema-pup-kitten",
            "title": "Vaccinatieschema pup en kitten: welke prik wanneer? | Kwispelboek",
            "h1": "Welke vaccinaties heeft je pup of kitten nodig, en wanneer?",
            "short": "Vaccinatieschema pup en kitten",
            "desc": "Wanneer krijgt je pup of kitten welke vaccinatie? Het schema volgens de KNMvD en de WSAVA, met de booster, herhalingen en een overzichtstabel.",
            "intro": "Pups en kittens krijgen hun eerste vaccinatie als ze 6 tot 8 weken oud zijn, en daarna elke 2 tot 4 weken een herhaling tot ze 14 tot 16 weken oud zijn. Tussen 6 en 12 maanden volgt een booster. Daarna is voor de belangrijkste ziekten een herhaling om de drie jaar genoeg, behalve voor de ziekte van Weil en kennelhoest bij de hond en niesziekte bij een kat die buiten komt: die zijn jaarlijks. Zo staat het in de richtlijnen die de Nederlandse dierenartsenorganisatie KNMvD noemt.",
            "table": (["Moment", "Pup", "Kitten"], [
                ["Basisvaccinatie", "Eerste enting op 6–8 weken, daarna elke 2–4 weken tot 14–16 weken", "Eerste enting op 6–8 weken, daarna elke 2–4 weken tot 14–16 weken"],
                ["Booster", "Op 6–12 maanden", "Op 6–12 maanden"],
                ["Om de drie jaar", "Parvo, hondenziekte en hepatitis", "Kattenziekte"],
                ["Elk jaar", "Ziekte van Weil (leptospirose) en kennelhoest", "Niesziekte, als je kat buiten komt, naar een pension gaat of in het asiel zit"],
                ["Naar het buitenland", "Hondsdolheid (rabiës) is verplicht", "Vraag je dierenarts wat je bestemming eist"],
            ]),
            "sections": [
                ("Waarom zoveel prikjes in het begin?", [
                    "Een pup of kitten krijgt via de moeder afweerstoffen mee. Die beschermen de eerste weken, maar ze zitten een vaccin ook in de weg. Hoe lang die afweerstoffen blijven, verschilt per dier, zelfs binnen één nest.",
                    "Daarom adviseert de wereldwijde dierenartsenorganisatie WSAVA meerdere entingen, elke 2 tot 4 weken, met de laatste op 16 weken of ouder. Een hervaccinatie vanaf 26 weken (ongeveer een half jaar) vangt de dieren op bij wie de afweerstoffen van de moeder bij de laatste prik nog actief waren. De KNMvD noemt de basisentingen samen met de booster de volledige basisvaccinatie.",
                ]),
                ("Welke ziekten zijn het belangrijkst?", [
                    "Volgens de richtlijnen die de KNMvD noemt zijn dit de belangrijkste vaccinaties: bij de hond parvo, hondenziekte, hepatitis (leverziekte) en de ziekte van Weil (leptospirose); bij de kat kattenziekte en niesziekte; bij het konijn myxomatose, RHD1 en RHD2.",
                    "Andere vaccinaties hangen af van het leven van je dier. Gaat je hond naar een pension of kennel, of mee met een uitlaatservice, dan is een vaccinatie tegen kennelhoest meestal verplicht.",
                ]),
                ("Na het eerste jaar: niet alles hoeft jaarlijks", [
                    "Na de basisvaccinatie is het volgens de KNMvD raadzaam om je hond om de drie jaar te laten vaccineren tegen parvo, hondenziekte en hepatitis, en je kat om de drie jaar tegen kattenziekte. Ook de WSAVA zegt dat kernvaccins bij volwassen dieren niet vaker gegeven moeten worden dan nodig.",
                    "Voor de ziekte van Weil en kennelhoest is wel een jaarlijkse vaccinatie nodig. Een kat die buiten loopt, naar een pension gaat of in het asiel zit, krijgt jaarlijks een vaccinatie tegen niesziekte. Veel dieren krijgen dus elk jaar een prik, maar niet elk jaar dezelfde.",
                    "De WSAVA raadt aan elk jaar een gezondheidscontrole te laten doen. Dat is meer dan alleen een prik: je dierenarts kijkt het hele dier na.",
                ]),
                ("Binnenkat of tuinkonijn: toch inenten?", [
                    "Ja. De KNMvD wijst erop dat je virussen zelf mee naar binnen kunt nemen, via je handen, kleding en schoenen. Het niesziektevirus blijft dagenlang besmettelijk. Konijnen kunnen sommige ziekten via muggen of via geplukt gras krijgen.",
                ]),
                ("Titeren in plaats van vaccineren", [
                    "Bij titeren meet de dierenarts met een druppel bloed of je dier nog genoeg antistoffen heeft. Volgens de KNMvD kan dat bij een volwassen hond of kat een alternatief zijn voor vaccineren tegen parvo, hondenziekte, hepatitis en kattenziekte. Bespreek met je dierenarts of het voor jouw dier zinvol is.",
                ]),
            ],
            "faq": [
                ("Wanneer krijgt een pup de eerste vaccinatie?", "Volgens de richtlijnen die de KNMvD noemt op 6 tot 8 weken. Daarna volgt elke 2 tot 4 weken een herhaling tot 14 tot 16 weken, en tussen 6 en 12 maanden een booster."),
                ("Moet mijn hond elk jaar gevaccineerd worden?", "Voor de ziekte van Weil en kennelhoest wel. Tegen parvo, hondenziekte en hepatitis is na de basisvaccinatie een herhaling om de drie jaar raadzaam. Een jaarlijkse gezondheidscontrole is altijd goed."),
                ("Moet een binnenkat ingeënt worden?", "Ja. Je kunt virussen zelf mee naar binnen nemen via handen, kleding en schoenen. Een herhaling tegen kattenziekte om de drie jaar is raadzaam; tegen niesziekte jaarlijks als je kat buiten komt, naar een pension gaat of in het asiel zit."),
                ("Wat heb ik nodig om met mijn hond naar het buitenland te gaan?", "Je hond moet ingeënt zijn tegen hondsdolheid (rabiës). Na de eerste rabiësprik geldt een wachttijd voordat je mag reizen; reken die uit met onze 21-dagenregel."),
                ("Heeft vaccineren bijwerkingen?", "Zelden. Als ze optreden, zijn de meest voorkomende lusteloosheid, niet willen eten en pijn, jeuk of een bultje op de prikplek."),
                ("Wat is titeren?", "Met een druppel bloed wordt gemeten of je dier nog genoeg antistoffen heeft. Bij een volwassen hond of kat kan dat een alternatief zijn voor vaccineren tegen parvo, hondenziekte, hepatitis en kattenziekte."),
            ],
            "app": "Kwispelboek stelt per diersoort een vaccinatieschema voor dat je met je dierenarts kunt aanpassen. Je krijgt op tijd een herinnering, en bij het afvinken scan je het batchnummer van de sticker.",
        },
        "en": {
            "slug": "puppy-kitten-vaccination-schedule",
            "title": "Puppy and kitten vaccination schedule: which jab when? | Wagbook",
            "h1": "Which vaccinations does your puppy or kitten need, and when?",
            "short": "Puppy and kitten vaccination schedule",
            "desc": "When does your puppy or kitten get which vaccination? The schedule from the WSAVA and the Dutch veterinary association, with booster, repeats and a table.",
            "intro": "Puppies and kittens get their first vaccination at 6 to 8 weeks old, then a repeat every 2 to 4 weeks until they are 14 to 16 weeks old. A booster follows between 6 and 12 months. After that, a repeat every three years is enough for the main diseases, except leptospirosis and kennel cough in dogs and cat flu in cats that go outside: those are yearly. This is the schedule described by the Dutch veterinary association (KNMvD), in line with the global WSAVA guidelines. Rules can differ by country, so check with your own vet.",
            "table": (["Moment", "Puppy", "Kitten"], [
                ["Primary vaccination", "First jab at 6–8 weeks, then every 2–4 weeks until 14–16 weeks", "First jab at 6–8 weeks, then every 2–4 weeks until 14–16 weeks"],
                ["Booster", "At 6–12 months", "At 6–12 months"],
                ["Every three years", "Parvovirus, distemper and hepatitis", "Feline panleukopenia"],
                ["Every year", "Leptospirosis and kennel cough", "Cat flu, if your cat goes outside, to a cattery or is in a shelter"],
                ["Travel abroad", "Rabies is required", "Ask your vet what your destination requires"],
            ]),
            "sections": [
                ("Why so many jabs at the start?", [
                    "A puppy or kitten receives antibodies from its mother. They protect in the first weeks, but they also get in the way of a vaccine. How long these antibodies last varies per animal, even within one litter.",
                    "That is why the global veterinary association WSAVA advises several doses, every 2 to 4 weeks, with the last one at 16 weeks or older. Revaccination from 26 weeks (about six months) catches the animals in which the mother’s antibodies were still active at the last jab. The KNMvD calls the primary jabs plus the booster together the complete primary vaccination.",
                ]),
                ("Which diseases matter most?", [
                    "According to the guidelines the KNMvD refers to, the most important vaccinations are: for dogs parvovirus, distemper, hepatitis and leptospirosis; for cats feline panleukopenia and cat flu; for rabbits myxomatosis, RHD1 and RHD2. WSAVA calls distemper, adenovirus (hepatitis) and parvovirus the core vaccines for dogs everywhere, and panleukopenia, calicivirus and herpesvirus (cat flu) for cats.",
                    "Other vaccinations depend on your pet’s life. If your dog goes to boarding kennels or with a dog walker, a kennel cough vaccination is usually required.",
                ]),
                ("After the first year: not everything is yearly", [
                    "After the primary vaccination, the KNMvD advises vaccinating your dog against parvovirus, distemper and hepatitis every three years, and your cat against panleukopenia every three years. WSAVA also says core vaccines should not be given more often than necessary in adult animals.",
                    "Leptospirosis and kennel cough do need a yearly vaccination. A cat that goes outside, to a cattery or lives in a shelter gets a yearly cat flu vaccination. So many pets get a jab every year, but not the same one every year.",
                    "WSAVA recommends a yearly health check. That is more than a jab: your vet examines the whole animal.",
                ]),
                ("Indoor cat or garden rabbit: still vaccinate?", [
                    "Yes. The KNMvD points out that you can carry viruses inside yourself, on your hands, clothes and shoes. The cat flu virus stays infectious for days. Rabbits can catch some diseases through mosquitoes or picked grass.",
                ]),
                ("Titre testing instead of vaccinating", [
                    "With titre testing, the vet uses a drop of blood to measure whether your pet still has enough antibodies. According to the KNMvD this can be an alternative to vaccinating an adult dog or cat against parvovirus, distemper, hepatitis and panleukopenia. Ask your vet whether it makes sense for your pet.",
                ]),
            ],
            "faq": [
                ("When does a puppy get its first vaccination?", "According to the guidelines the KNMvD refers to, at 6 to 8 weeks. Then a repeat every 2 to 4 weeks until 14 to 16 weeks, and a booster between 6 and 12 months."),
                ("Does my dog need vaccinating every year?", "For leptospirosis and kennel cough, yes. Against parvovirus, distemper and hepatitis, a repeat every three years is advised after the primary vaccination. A yearly health check is always a good idea."),
                ("Does an indoor cat need vaccinating?", "Yes. You can carry viruses inside on your hands, clothes and shoes. A repeat against panleukopenia every three years is advised; against cat flu yearly if your cat goes outside, to a cattery or is in a shelter."),
                ("What do I need to travel abroad with my dog?", "Your dog must be vaccinated against rabies. After the first rabies jab there is a waiting period before you may travel; work it out with our 21-day rule calculator."),
                ("Does vaccination have side effects?", "Rarely. When they occur, the most common are tiredness, not wanting to eat and pain, itching or a small lump where the jab was given."),
                ("What is titre testing?", "A drop of blood is used to measure whether your pet still has enough antibodies. For an adult dog or cat it can be an alternative to vaccinating against parvovirus, distemper, hepatitis and panleukopenia."),
            ],
            "app": "Wagbook suggests a vaccination schedule per species that you can adjust with your vet. You get a reminder in time, and when you tick one off you can scan the batch number from the sticker.",
        },
    },
]


def src_of(key, lang):
    s = SRC[key]
    return s[lang] if isinstance(s, dict) else s


def p_guide(lang, g):
    return f'{TX[lang]["path"]}{g[lang]["slug"]}/'


def pages():
    rows = [(TX["nl"]["path"], TX["en"]["path"], DATE)]
    rows += [(p_guide("nl", g), p_guide("en", g), DATE) for g in GUIDES]
    return rows


def llms_lines(lang, domain):
    return [f"- [{g[lang]['h1']}]({domain}{p_guide(lang, g).removeprefix('/en')}): {g[lang]['desc']}" for g in GUIDES]


def words(g, lang):
    x = g[lang]
    text = " ".join([x["intro"], x["app"]] + [p for _, ps in x["sections"] for p in ps] + [q + " " + a for q, a in x["faq"]]
                    + [" ".join(r) for r in x["table"][1]])
    return len(text.split())


def guide_page(b, extra, lang, g):
    o = "en" if lang == "nl" else "nl"
    x, t = g[lang], TX[lang]
    path, alt = p_guide(lang, g), p_guide(o, g)
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (t["name"], t["path"]), (x["short"], path)]
    head, rows = x["table"]
    table = ('<div class="table-wrap"><table class="guide-table"><thead><tr>' + "".join(f"<th scope=\"col\">{escape(h)}</th>" for h in head)
             + "</tr></thead><tbody>"
             + "".join("<tr>" + "".join((f'<th scope="row">{escape(c)}</th>' if i == 0 else f"<td>{escape(c)}</td>") for i, c in enumerate(r)) + "</tr>"
                       for r in rows)
             + "</tbody></table></div>")
    secs = "".join(f"<h2>{escape(h)}</h2>" + "".join(f"<p>{escape(p)}</p>" for p in ps) for h, ps in x["sections"])
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in x["faq"])
    src = "".join(f'<li><a href="{u}" rel="noopener">{escape(n)}</a></li>' for n, u in (src_of(k, lang) for k in g["sources"]))
    url = f'{b.PLAY_URL}&amp;hl={b.T[lang]["hl"]}'
    cta = f"""<div class="post-cta">
  <img src="/assets/img/kwispel-happy.svg" alt="{escape(b.T[lang]['kw_alt'])}" width="96" height="96" loading="lazy">
  <div><h2>{escape(t['cta_title'])}</h2><p>{escape(x['app'])}</p>
  <a class="btn btn-primary" href="{url}" rel="noopener">{escape(t['cta_btn'])} →</a></div>
</div>"""
    nice = b.nice_date(DATE, lang)
    body = f"""<p class="post-emoji" aria-hidden="true">{g['emoji']}</p>
<h1>{escape(x['h1'])}</h1>
<p class="meta">{t['updated']} <time datetime="{DATE}">{nice}</time></p>
<p class="summary">{escape(x['intro'])}</p>
<h2>{t['glance']}</h2>
{table}
{secs}
{cta}
<h2>{t['faq']}</h2>
<div class="faq">{faq}</div>
<h2>{t['sources']}</h2>
<ul class="sources">{src}</ul>
<p class="note">{escape(t['disclaimer'])}</p>
<h2>{t['related']}</h2>
{extra.links_list(g['related'][lang])}"""
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x["faq"]]}
    art_ld = {"@context": "https://schema.org", "@type": "Article", "headline": x["h1"], "description": x["desc"],
              "inLanguage": lang, "datePublished": DATE, "dateModified": DATE, "url": b.DOMAIN + path,
              "author": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
              "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"},
              "citation": [u for _, u in (src_of(k, lang) for k in g["sources"])]}
    ld = (f'<script type="application/ld+json">{json.dumps(art_ld, ensure_ascii=False)}</script>\n'
          f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>\n')
    return extra.page(b, lang, x["title"], x["desc"], path, alt, trail, body, extra_ld=ld)


def hub_page(b, lang):
    o = "en" if lang == "nl" else "nl"
    t = TX[lang]
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (t["name"], t["path"])]
    grid = "".join(f'<a class="post-card" href="{p_guide(lang, g)}"><span class="post-ico" aria-hidden="true">{g["emoji"]}</span>'
                   f'<h2>{escape(g[lang]["h1"])}</h2><p>{escape(g[lang]["desc"])}</p><span class="post-meta">{t["open"]} →</span></a>'
                   for g in GUIDES)
    body = f"""<div class="wrap">
<h1>{escape(t['name'])}</h1>
<p class="lead" style="margin-top:12px">{escape(t['lead'])}</p>
<div class="post-grid">{grid}</div>
</div>"""
    c_html, c_ld = b.crumbs(lang, trail)
    return (b.head(lang, t["title"], t["desc"], t["path"], TX[o]["path"], lang, c_ld) + b.header(lang, t["path"], TX[o]["path"], nav=False)
            + f'<main id="main" class="blog">\n<div class="wrap">{c_html}</div>\n{body}\n</main>\n' + b.footer(lang))


def build(b, extra):
    from blog_content import ARTICLES as ALL_ARTICLES
    by_key = {g["key"]: g for g in GUIDES}
    for a in ALL_ARTICLES:  # old blog posts that became a guide: keep the URL alive as a redirect
        if a["key"] in MOVED:
            g = by_key[MOVED[a["key"]]]
            b.out(b.SITE / "blog" / a["nl"]["slug"] / "index.html", b.redirect_stub(b.DOMAIN + p_guide("nl", g)))
            b.out(b.EN_SITE / "blog" / a["en"]["slug"] / "index.html", b.redirect_stub(b.EN_DOMAIN + p_guide("en", g).removeprefix("/en")))
            b.out(b.SITE / "en" / "blog" / a["en"]["slug"] / "index.html", b.redirect_stub(b.EN_DOMAIN + p_guide("en", g).removeprefix("/en")))
    for lang, w in (("nl", b.write), ("en", b.write_en)):
        def rel(path):
            return (path.removeprefix("/en") if lang == "en" else path).lstrip("/") + "index.html"
        w(rel(TX[lang]["path"]), hub_page(b, lang))
        for g in GUIDES:
            w(rel(p_guide(lang, g)), guide_page(b, extra, lang, g))


from guides_more import MORE_GUIDES, MORE_SRC, MOVED  # noqa: E402
SRC.update(MORE_SRC)
GUIDES += MORE_GUIDES
