"""Extra pages for kwispelboek.app (NL) and wagbook.app (EN): tools (calculators), a page per species and
printable checklists. Rendered with the helpers of build.py (passed in as `b`), so header, footer,
breadcrumbs and hreflang work exactly like the other pages.

English paths are written with the /en/ prefix, like everywhere in build.py; en_links() maps them to
wagbook.app."""
from html import escape
import json
import re

DATE = "2026-11-14"

# ---------------------------------------------------------------------------------------------- texts
TX = {
 "nl": {
  "tools": "Hulpmiddelen", "tools_path": "/hulpmiddelen/",
  "tools_title": "Gratis hulpmiddelen voor baasjes | Kwispelboek",
  "tools_desc": "Gratis rekenhulpjes voor je huisdier: leeftijd in mensenjaren, de 21-dagenregel voor reizen en hoe lang een zak voer meegaat.",
  "tools_lead": "Kleine rekenhulpjes die je meteen kunt gebruiken. Gratis, zonder account, alles rekent in je eigen browser.",
  "species": "Per diersoort", "species_path": "/voor/",
  "species_title": "Kwispelboek voor hond, kat, konijn en vogel",
  "species_desc": "Wat Kwispelboek per diersoort bijhoudt: vaccinaties, ontworming, gewicht en meer, voor honden, katten, konijnen en vogels.",
  "species_lead": "Elke diersoort heeft andere zorg nodig. Kwispelboek past de suggesties aan op je dier.",
  "lists": "Checklists", "lists_path": "/checklists/",
  "lists_title": "Printbare checklists voor je huisdier | Kwispelboek",
  "lists_desc": "Gratis checklists om te printen of af te vinken: puppy in huis en op vakantie met je hond of kat.",
  "lists_lead": "Om te printen, op te slaan als PDF of gewoon hier af te vinken.",
  "open": "Openen", "print": "Printen", "pdf": "Download PDF",
  "cta_title": "Alles op één plek, met een herinnering op tijd",
  "cta_text": "Kwispelboek onthoudt vaccinaties, ontworming, medicijnen, gewicht en voer voor al je dieren. Gratis, zonder account.",
  "cta_btn": "Gratis in Google Play",
  "disclaimer": "Dit is een hulpmiddel en geen veterinair advies. Twijfel je? Vraag het je dierenarts.",
  "also": "Ook handig",
  "track": "Wat houd je bij?", "vacc": "Vaccinaties die Kwispelboek voorstelt", "tips": "Goed om te weten",
  "app": "Zo helpt Kwispelboek",
  "vacc_note": "Dit zijn gangbare schema’s. Je dierenarts bepaalt wat jouw dier nodig heeft; in de app pas je het schema aan.",
  "checked": "Je vinkjes worden alleen in deze browser bewaard.",
  "reset": "Alles leegmaken",
 },
 "en": {
  "tools": "Tools", "tools_path": "/en/tools/",
  "tools_title": "Free tools for pet owners | Wagbook",
  "tools_desc": "Free calculators for your pet: age in human years, the 21-day rule for travel and how long a bag of food lasts.",
  "tools_lead": "Small calculators you can use right away. Free, no account, everything is worked out in your own browser.",
  "species": "Per species", "species_path": "/en/for/",
  "species_title": "Wagbook for dogs, cats, rabbits and birds",
  "species_desc": "What Wagbook tracks per species: vaccinations, deworming, weight and more, for dogs, cats, rabbits and birds.",
  "species_lead": "Every species needs different care. Wagbook tailors its suggestions to your pet.",
  "lists": "Checklists", "lists_path": "/en/checklists/",
  "lists_title": "Printable checklists for your pet | Wagbook",
  "lists_desc": "Free checklists to print or tick off: a new puppy at home and going on holiday with your dog or cat.",
  "lists_lead": "To print, save as a PDF or simply tick off right here.",
  "open": "Open", "print": "Print", "pdf": "Download PDF",
  "cta_title": "Everything in one place, with a reminder on time",
  "cta_text": "Wagbook remembers vaccinations, deworming, medication, weight and food for all your pets. Free, no account.",
  "cta_btn": "Free on Google Play",
  "disclaimer": "This is a tool, not veterinary advice. In doubt? Ask your vet.",
  "also": "Also handy",
  "track": "What do you keep track of?", "vacc": "Vaccinations Wagbook suggests", "tips": "Good to know",
  "app": "How Wagbook helps",
  "vacc_note": "These are common schedules. Your vet decides what your pet needs; you adjust the schedule in the app.",
  "checked": "Your ticks are only kept in this browser.",
  "reset": "Clear all",
 },
}

# ---------------------------------------------------------------------------------------------- tools
TOOLS = [
 {
  "key": "age", "emoji": "🎂",
  "nl": {"slug": "leeftijd-in-mensenjaren", "title": "Hoe oud is je hond of kat in mensenjaren?",
         "short": "Leeftijd in mensenjaren",
         "desc": "Reken de leeftijd van je hond of kat om naar mensenjaren. Voor honden telt ook de grootte mee.",
         "intro": "De oude regel ‘één hondenjaar is zeven mensenjaren’ klopt niet. Een hond is na één jaar al volwassen, en grote honden worden sneller oud dan kleine. Deze rekenhulp gebruikt de gangbare schatting die ook veel dierenartsen gebruiken."},
  "en": {"slug": "pet-age-in-human-years", "title": "How old is your dog or cat in human years?",
         "short": "Age in human years",
         "desc": "Convert your dog’s or cat’s age into human years. For dogs, size matters too.",
         "intro": "The old rule ‘one dog year is seven human years’ isn’t right. A dog is an adult after one year, and big dogs age faster than small ones. This calculator uses the common estimate that many vets use too."},
 },
 {
  "key": "travel", "emoji": "✈️",
  "nl": {"slug": "21-dagenregel", "title": "Wanneer mag je op reis? De 21-dagenregel berekenen",
         "short": "21-dagenregel voor reizen",
         "desc": "Bereken vanaf welke dag je hond, kat of fret binnen de EU de grens over mag na een eerste rabiësvaccinatie.",
         "intro": "Na een eerste rabiësvaccinatie moet je binnen de EU 21 dagen wachten voordat je met je hond, kat of fret de grens over mag. Vul de datum van de prik in, of de geboortedatum van je pup of kitten."},
  "en": {"slug": "21-day-rule", "title": "When can you travel? Work out the 21-day rule",
         "short": "21-day rule for travel",
         "desc": "Work out from which day your dog, cat or ferret may cross a border within the EU after a first rabies vaccination.",
         "intro": "After a first rabies vaccination you have to wait 21 days before crossing a border within the EU with your dog, cat or ferret. Enter the date of the shot, or your puppy’s or kitten’s date of birth."},
 },
 {
  "key": "food", "emoji": "🥣",
  "nl": {"slug": "voercalculator", "title": "Voercalculator: hoe lang doe je met een zak voer?",
         "short": "Voercalculator",
         "desc": "Bereken hoeveel dagen een zak voer meegaat, wanneer hij op is en wat het voer per dag en per maand kost.",
         "intro": "Vul in hoe groot de zak is en hoeveel je dier per dag eet. Dan zie je meteen hoe lang je ermee doet, wanneer je nieuw voer moet halen en wat het per dag kost."},
  "en": {"slug": "food-calculator", "title": "Food calculator: how long does a bag of food last?",
         "short": "Food calculator",
         "desc": "Work out how many days a bag of food lasts, when it runs out and what the food costs per day and per month.",
         "intro": "Enter the bag size and how much your pet eats per day. You’ll see right away how long it lasts, when to buy new food and what it costs per day."},
 },
]

TOOL_UI = {
 "age": {
  "nl": dict(species="Dier", dog="Hond", cat="Kat", size="Grootte", small="Klein (tot 10 kg)", medium="Middel (10–25 kg)",
             large="Groot (meer dan 25 kg)", age="Leeftijd in jaren", result="mensenjaren", stage=["Pup of kitten", "Jongvolwassen", "Volwassen", "Senior"],
             how="Zo rekenen we", how_text="Het eerste jaar telt als 15 mensenjaren, het tweede als 9. Daarna telt elk jaar als ongeveer 4 mensenjaren voor katten en kleine honden, 4,5 voor middelgrote en 5,25 voor grote honden. Het blijft een schatting: elk dier veroudert anders."),
  "en": dict(species="Pet", dog="Dog", cat="Cat", size="Size", small="Small (up to 10 kg)", medium="Medium (10–25 kg)",
             large="Large (over 25 kg)", age="Age in years", result="human years", stage=["Puppy or kitten", "Young adult", "Adult", "Senior"],
             how="How we calculate", how_text="The first year counts as 15 human years, the second as 9. After that, every year counts as about 4 human years for cats and small dogs, 4.5 for medium dogs and 5.25 for large dogs. It stays an estimate: every animal ages differently."),
 },
 "travel": {
  "nl": dict(mode_shot="Datum van de eerste rabiësprik", mode_birth="Of: geboortedatum van je pup of kitten",
             res_shot="Je mag de grens over vanaf", res_birth="Vroegst mogelijke reisdatum",
             birth_note="Een rabiësprik mag vanaf 12 weken. Daarna nog 21 dagen wachten: samen ongeveer 15 weken.",
             rules="De regels op een rij", rules_list=["Eerst een chip, dan pas de rabiësprik. Andersom telt de prik niet.",
             "Een Europees dierenpaspoort, afgegeven door je dierenarts.", "Na een eerste rabiësprik 21 dagen wachten. Bij een herhaalprik die op tijd is gegeven niet opnieuw.",
             "Naar Ierland, Finland, Malta of Noorwegen moet je hond 1 tot 5 dagen voor aankomst ook een lintwormbehandeling krijgen.",
             "Buiten de EU en naar het Verenigd Koninkrijk gelden andere regels. Kijk altijd op de site van de overheid van je bestemming."],
             blog="Lees ook: Op reis met je hond of kat", blog_slug="op-reis-met-hond-of-kat"),
  "en": dict(mode_shot="Date of the first rabies shot", mode_birth="Or: your puppy’s or kitten’s date of birth",
             res_shot="You may cross the border from", res_birth="Earliest possible travel date",
             birth_note="A rabies shot is allowed from 12 weeks. Then another 21 days of waiting: about 15 weeks in total.",
             rules="The rules at a glance", rules_list=["A microchip first, then the rabies shot. The other way round, the shot doesn’t count.",
             "A European pet passport, issued by your vet.", "Wait 21 days after a first rabies shot. Not again for a booster given on time.",
             "For Ireland, Finland, Malta or Norway, your dog also needs a tapeworm treatment 1 to 5 days before arrival.",
             "Outside the EU and for the United Kingdom, other rules apply. Always check the government website of your destination."],
             blog="Also read: Travelling with your dog or cat", blog_slug="travelling-with-your-dog-or-cat"),
 },
 "food": {
  "nl": dict(bag="Zak of doos (kg)", daily="Per dag (gram)", opened="Geopend op", price="Prijs van de zak (€, mag leeg)",
             days="dagen", runs_out="Op rond", per_day="Per dag", per_month="Per maand",
             tip="Tip: houd het makkelijk vol door een maatbekertje te gebruiken. Kijk op de verpakking hoeveel je dier per dag mag, en vraag je dierenarts als je dier te zwaar of te licht is."),
  "en": dict(bag="Bag or box (kg)", daily="Per day (grams)", opened="Opened on", price="Price of the bag (€, optional)",
             days="days", runs_out="Runs out around", per_day="Per day", per_month="Per month",
             tip="Tip: a measuring cup makes it easy to stick to the portion. Check the packaging for how much your pet should eat per day, and ask your vet if your pet is too heavy or too light."),
 },
}

# ---------------------------------------------------------------------------------------------- species
SPECIES = [
 {
  "key": "dog", "emoji": "🐶",
  "nl": {"slug": "hond", "name": "hond", "title": "Kwispelboek voor je hond: vaccinaties en ontworming",
         "h1": "Kwispelboek voor je hond",
         "desc": "Houd de zorg voor je hond bij: cocktail-enting, leptospirose, kennelhoest, rabiës, ontworming, vlooien en teken, gewicht en voer. Met herinneringen op tijd.",
         "lead": "Van pup tot senior: alle vaccinaties, ontworming, vlooien- en tekenbehandelingen, medicijnen, gewicht en voer van je hond op één plek.",
         "vacc": ["Cocktail-enting (DHP): elke 3 jaar", "Leptospirose: elk jaar", "Kennelhoest: elk jaar", "Rabiës: elke 3 jaar (verplicht voor reizen)"],
         "track": ["Ontworming, bijvoorbeeld elke 3 maanden", "Vlooien- en tekenbehandeling, elke maand of elke 3 maanden", "Gewicht in kilo’s, met een grafiek", "Dierenartsbezoeken met kosten", "Voer, en wanneer de zak op is"],
         "tips": ["Bij een pup geeft de dierenarts de eerste vaccinaties in een paar rondes. Zet ze er allemaal in, dan vergeet je de laatste niet.",
                  "Gaat je hond mee op reis? De reischecklist kijkt of chip, paspoort en rabiësprik op tijd in orde zijn.",
                  "Grote honden worden sneller oud. Weeg je hond regelmatig, dan zie je veranderingen op tijd."],
         "app": "Kwispelboek stelt de gangbare vaccinaties voor honden voor, met het juiste herhaalschema. Je krijgt een melding vooraf en op de dag zelf. Met de knoppen op het profiel maak je een overzicht voor de dierenarts, de oppas, een reis of een vermist-poster."},
  "en": {"slug": "dogs", "name": "dog", "title": "Wagbook for your dog: vaccinations, deworming and more",
         "h1": "Wagbook for your dog",
         "desc": "Keep track of your dog’s care: core vaccine, leptospirosis, kennel cough, rabies, deworming, fleas and ticks, weight and food. With reminders on time.",
         "lead": "From puppy to senior: all your dog’s vaccinations, deworming, flea and tick treatments, medication, weight and food in one place.",
         "vacc": ["Core vaccine (DHP): every 3 years", "Leptospirosis: every year", "Kennel cough: every year", "Rabies: every 3 years (required for travel)"],
         "track": ["Deworming, for example every 3 months", "Flea and tick treatment, every month or every 3 months", "Weight in kilos, with a chart", "Vet visits with costs", "Food, and when the bag runs out"],
         "tips": ["For a puppy, the vet gives the first vaccinations in a few rounds. Add them all, so you don’t forget the last one.",
                  "Taking your dog on holiday? The travel checklist checks whether microchip, passport and rabies shot are in order in time.",
                  "Big dogs age faster. Weigh your dog regularly and you’ll spot changes early."],
         "app": "Wagbook suggests the common vaccinations for dogs, with the right repeat schedule. You get a reminder in advance and on the day itself. With the buttons on the profile you make an overview for the vet, the sitter, a trip or a missing poster."},
 },
 {
  "key": "cat", "emoji": "🐱",
  "nl": {"slug": "kat", "name": "kat", "title": "Kwispelboek voor je kat: vaccinaties, ontworming en meer",
         "h1": "Kwispelboek voor je kat",
         "desc": "Houd de zorg voor je kat bij: kattenziekte en niesziekte, FeLV, rabiës, ontworming, vlooien, gewicht en voer. Met herinneringen op tijd.",
         "lead": "Binnenkat of buitenkat: vaccinaties, ontworming, vlooienbehandeling, medicijnen, gewicht en voer van je kat op één plek.",
         "vacc": ["Kattenziekte + niesziekte: elk jaar (of volgens je dierenarts)", "FeLV (leukose): elk jaar, vooral voor buitenkatten", "Rabiës: elke 3 jaar (verplicht voor reizen)"],
         "track": ["Ontworming, bijvoorbeeld elke 3 maanden", "Vlooienbehandeling, ook bij binnenkatten", "Gewicht, want katten verbergen ziek zijn goed", "Medicijnen, bijvoorbeeld een schildkliertablet", "Voer, en wanneer de zak op is"],
         "tips": ["Gebruik nooit een vlooienmiddel voor honden bij je kat. Sommige middelen voor honden zijn giftig voor katten.",
                  "Een kat die afvalt, kan ziek zijn. Een gewichtsgrafiek laat het op tijd zien.",
                  "Lelies zijn heel giftig voor katten, ook het stuifmeel. In de app staat bij Eerste hulp wat giftig is."],
         "app": "Kwispelboek stelt de gangbare vaccinaties voor katten voor en herinnert je aan ontworming en de vlooienbehandeling. Medicijnen geef je met een melding op het juiste tijdstip, met de knoppen ‘Gegeven’ en ‘Later’."},
  "en": {"slug": "cats", "name": "cat", "title": "Wagbook for your cat: vaccinations, deworming and more",
         "h1": "Wagbook for your cat",
         "desc": "Keep track of your cat’s care: cat flu and panleukopenia, FeLV, rabies, deworming, fleas, weight and food. With reminders on time.",
         "lead": "Indoor or outdoor cat: your cat’s vaccinations, deworming, flea treatment, medication, weight and food in one place.",
         "vacc": ["Cat flu + panleukopenia: every year (or as your vet advises)", "FeLV (feline leukaemia): every year, especially for outdoor cats", "Rabies: every 3 years (required for travel)"],
         "track": ["Deworming, for example every 3 months", "Flea treatment, indoor cats too", "Weight, because cats hide being ill", "Medication, for example a thyroid tablet", "Food, and when the bag runs out"],
         "tips": ["Never use a dog flea product on your cat. Some products for dogs are toxic to cats.",
                  "A cat that loses weight may be ill. A weight chart shows it in time.",
                  "Lilies are very toxic to cats, even the pollen. First aid in the app lists what’s toxic."],
         "app": "Wagbook suggests the common vaccinations for cats and reminds you about deworming and flea treatment. Medication comes with a reminder at the right time, with ‘Given’ and ‘Later’ buttons."},
 },
 {
  "key": "rabbit", "emoji": "🐰",
  "nl": {"slug": "konijn", "name": "konijn", "title": "Kwispelboek voor je konijn: vaccinatie, gewicht en meer",
         "h1": "Kwispelboek voor je konijn",
         "desc": "Houd de zorg voor je konijn bij: de jaarlijkse vaccinatie tegen myxomatose en RHD, ontworming, gewicht, voer en dierenartsbezoeken.",
         "lead": "Konijnen laten weinig merken als ze ziek zijn. Met Kwispelboek houd je de vaccinatie, het gewicht en het voer goed in de gaten.",
         "vacc": ["Myxomatose + RHD (1 en 2): elk jaar"],
         "track": ["De jaarlijkse vaccinatie, met een melding vooraf", "Gewicht: afvallen is bij konijnen vaak het eerste teken", "Voer en hooi, en wanneer het op is", "Dierenartsbezoeken, bijvoorbeeld voor de tanden", "Een dagboek: at hij minder, of minder keutels?"],
         "tips": ["Een konijn dat niet eet, moet dezelfde dag naar de dierenarts. Wacht niet af.",
                  "Konijnentanden groeien altijd door. Veel hooi helpt ze slijten.",
                  "Konijnen kunnen slecht tegen hitte. Zet het hok in de zomer in de schaduw."],
         "app": "Kwispelboek stelt de jaarlijkse vaccinatie voor konijnen voor en herinnert je op tijd. In het dagboek schrijf je op wat je opvalt, met een foto. Handig als de dierenarts vraagt sinds wanneer."},
  "en": {"slug": "rabbits", "name": "rabbit", "title": "Wagbook for your rabbit: vaccination, weight and more",
         "h1": "Wagbook for your rabbit",
         "desc": "Keep track of your rabbit’s care: the yearly vaccination against myxomatosis and RHD, deworming, weight, food and vet visits.",
         "lead": "Rabbits show little when they’re ill. With Wagbook you keep a good eye on the vaccination, weight and food.",
         "vacc": ["Myxomatosis + RHD (1 and 2): every year"],
         "track": ["The yearly vaccination, with a reminder in advance", "Weight: losing weight is often the first sign in rabbits", "Pellets and hay, and when they run out", "Vet visits, for example for the teeth", "A diary: is he eating less, or fewer droppings?"],
         "tips": ["A rabbit that stops eating needs to see a vet the same day. Don’t wait.",
                  "Rabbit teeth keep growing. Plenty of hay helps wear them down.",
                  "Rabbits don’t cope well with heat. Keep the hutch in the shade in summer."],
         "app": "Wagbook suggests the yearly vaccination for rabbits and reminds you in time. In the diary you write down what you notice, with a photo. Handy when the vet asks since when."},
 },
 {
  "key": "bird", "emoji": "🐦",
  "nl": {"slug": "vogel", "name": "vogel", "title": "Kwispelboek voor je vogel: gewicht in grammen en meer",
         "h1": "Kwispelboek voor je vogel",
         "desc": "Houd de zorg voor je parkiet, kanarie of papegaai bij: gewicht in grammen, dierenartsbezoeken, medicijnen, voer en een dagboek.",
         "lead": "Vogels verbergen ziek zijn heel goed. Een paar gram eraf kan al iets betekenen. Kwispelboek weegt vogels daarom in grammen.",
         "vacc": [],
         "track": ["Gewicht in grammen, met een grafiek", "Dierenartsbezoeken, bijvoorbeeld bij een vogeldierenarts", "Medicijnen, met een melding op tijd", "Voer, en wanneer het op is", "Een dagboek: rui, eten, ontlasting"],
         "tips": ["Weeg je vogel op een vast moment, bijvoorbeeld ’s ochtends voor het eten. Dan zijn de wegingen goed te vergelijken.",
                  "Zit je vogel bol en stil? Dat kan een teken van ziekte zijn. Bel een vogeldierenarts.",
                  "Teflonpannen die oververhit raken, geven dampen die giftig zijn voor vogels."],
         "app": "Voor vogels zijn er geen standaardvaccinaties, dus Kwispelboek stelt die niet voor. Je weegt in grammen en ziet in de grafiek meteen of je vogel afvalt."},
  "en": {"slug": "birds", "name": "bird", "title": "Wagbook for your bird: weight in grams and more",
         "h1": "Wagbook for your bird",
         "desc": "Keep track of your budgie’s, canary’s or parrot’s care: weight in grams, vet visits, medication, food and a diary.",
         "lead": "Birds hide being ill very well. A few grams less can already mean something. That’s why Wagbook weighs birds in grams.",
         "vacc": [],
         "track": ["Weight in grams, with a chart", "Vet visits, for example at an avian vet", "Medication, with a reminder on time", "Food, and when it runs out", "A diary: moulting, eating, droppings"],
         "tips": ["Weigh your bird at a fixed time, for example in the morning before eating. Then the weighings compare well.",
                  "Is your bird fluffed up and quiet? That can be a sign of illness. Call an avian vet.",
                  "Non-stick pans that overheat give off fumes that are toxic to birds."],
         "app": "There are no standard vaccinations for birds, so Wagbook doesn’t suggest them. You weigh in grams and the chart shows right away if your bird is losing weight."},
 },
]
NO_VACC = {"nl": "Voor vogels zijn er geen standaardvaccinaties. Je vogeldierenarts vertelt je wat nodig is.",
           "en": "There are no standard vaccinations for birds. Your avian vet will tell you what’s needed."}

# ---------------------------------------------------------------------------------------------- checklists
CHECKLISTS = [
 {
  "key": "puppy", "emoji": "🐶",
  "nl": {"slug": "puppy-in-huis", "title": "Checklist: puppy in huis", "h1": "Checklist: puppy in huis",
         "desc": "Een printbare checklist voor als er een puppy komt: spullen, de eerste dagen, de dierenarts en papieren.",
         "lead": "Er komt een puppy! Met deze lijst vergeet je niets, van de mand tot de eerste prik.",
         "groups": [
          ("Spullen in huis", ["Mand of bench met een zacht kleed", "Voer- en waterbak", "Hetzelfde voer als bij de fokker of het asiel", "Halsband of tuigje en een riem", "Penning met je telefoonnummer", "Kauwspeeltjes", "Poepzakjes", "Een borstel die past bij de vacht"]),
          ("Voor het huis", ["Snoeren en kabels weg of afgeschermd", "Giftige planten en schoonmaakmiddelen buiten bereik", "Een hekje bij de trap", "Een vaste plek om te plassen buiten"]),
          ("De eerste week", ["Vaste tijden voor eten, slapen en plassen", "Rustig wennen: niet meteen veel bezoek", "Kort alleen laten oefenen", "Puppycursus zoeken"]),
          ("Dierenarts en papieren", ["Kennismaken bij de dierenarts", "Vaccinatieschema afspreken: de rondes en de herhaling", "Ontwormingsschema afspreken", "Chip op jouw naam laten zetten", "Paspoort of vaccinatieboekje bewaren", "Eventueel een dierenverzekering"]),
         ]},
  "en": {"slug": "new-puppy", "title": "Checklist: a new puppy at home", "h1": "Checklist: a new puppy at home",
         "desc": "A printable checklist for when a puppy is coming: supplies, the first days, the vet and paperwork.",
         "lead": "A puppy is coming! With this list you won’t forget a thing, from the bed to the first shot.",
         "groups": [
          ("Supplies", ["Bed or crate with a soft blanket", "Food and water bowls", "The same food the breeder or shelter used", "Collar or harness and a lead", "Tag with your phone number", "Chew toys", "Poop bags", "A brush that suits the coat"]),
          ("Around the house", ["Cords and cables out of reach or covered", "Toxic plants and cleaning products out of reach", "A gate at the stairs", "A fixed spot to pee outside"]),
          ("The first week", ["Fixed times for eating, sleeping and peeing", "Settle in calmly: not lots of visitors right away", "Practise being alone for short times", "Find a puppy class"]),
          ("Vet and paperwork", ["Meet your vet", "Agree on the vaccination schedule: the rounds and the booster", "Agree on a deworming schedule", "Have the microchip registered in your name", "Keep the passport or vaccination booklet safe", "Consider pet insurance"]),
         ]},
 },
 {
  "key": "holiday", "emoji": "🧳",
  "nl": {"slug": "op-vakantie", "title": "Checklist: op vakantie met je huisdier", "h1": "Checklist: op vakantie met je huisdier",
         "desc": "Een printbare checklist voor op vakantie met je hond of kat: papieren, inpakken, de reis en op je bestemming.",
         "lead": "Samen op vakantie? Vink deze lijst af, dan ben je goed voorbereid.",
         "groups": [
          ("Ruim van tevoren", ["Regels van het land opzoeken op de site van de overheid", "Chip werkt en staat op jouw naam", "Europees dierenpaspoort", "Rabiësvaccinatie geldig (na een eerste prik: 21 dagen wachten)", "Lintwormbehandeling als je bestemming dat vraagt", "Bescherming tegen ziektes op je bestemming, vraag je dierenarts"]),
          ("Inpakken", ["Voer voor de hele reis, plus een paar dagen extra", "Voer- en waterbak", "Medicijnen voor de hele vakantie", "Riem, tuigje en een reservepenning", "Mand of kleed dat naar thuis ruikt", "Poepzakjes", "Een recente foto van je dier"]),
          ("Onderweg", ["Genoeg water en pauzes", "Nooit alleen in een warme auto", "Bench of gordel voor in de auto"]),
          ("Op je bestemming", ["Dierenarts in de buurt opgezocht", "Je telefoonnummer op de penning klopt", "Let op hitte, teken en giftige planten"]),
         ]},
  "en": {"slug": "holiday", "title": "Checklist: going on holiday with your pet", "h1": "Checklist: going on holiday with your pet",
         "desc": "A printable checklist for a holiday with your dog or cat: paperwork, packing, the trip and at your destination.",
         "lead": "Going on holiday together? Tick off this list and you’ll be well prepared.",
         "groups": [
          ("Well in advance", ["Look up the country’s rules on the government website", "Microchip works and is registered in your name", "European pet passport", "Valid rabies vaccination (after a first shot: wait 21 days)", "Tapeworm treatment if your destination requires it", "Protection against diseases at your destination, ask your vet"]),
          ("Packing", ["Food for the whole trip, plus a few extra days", "Food and water bowls", "Medication for the whole holiday", "Lead, harness and a spare tag", "Bed or blanket that smells of home", "Poop bags", "A recent photo of your pet"]),
          ("On the way", ["Enough water and breaks", "Never alone in a hot car", "Crate or harness belt in the car"]),
          ("At your destination", ["Looked up a vet nearby", "Your phone number on the tag is correct", "Watch out for heat, ticks and toxic plants"]),
         ]},
 },
]


# ---------------------------------------------------------------------------------------------- helpers
def other(lang):
    return "en" if lang == "nl" else "nl"


def p_tool(lang, t):
    return f'{TX[lang]["tools_path"]}{t[lang]["slug"]}/'


def p_species(lang, s):
    return f'{TX[lang]["species_path"]}{s[lang]["slug"]}/'


def p_list(lang, c):
    return f'{TX[lang]["lists_path"]}{c[lang]["slug"]}/'


def cta(b, lang):
    x = TX[lang]
    url = f'{b.PLAY_URL}&amp;hl={b.T[lang]["hl"]}'
    return f"""<div class="post-cta">
  <img src="/assets/img/kwispel-happy.svg" alt="{escape(b.T[lang]['kw_alt'])}" width="96" height="96" loading="lazy">
  <div><h2>{escape(x['cta_title'])}</h2><p>{escape(x['cta_text'])}</p>
  <a class="btn btn-primary" href="{url}" rel="noopener">{escape(x['cta_btn'])}</a></div>
</div>"""


def page(b, lang, title, desc, path, alt, trail, body, cls="legal article", extra_ld="", script=""):
    c_html, c_ld = b.crumbs(lang, trail)
    return (b.head(lang, title, desc, path, alt, lang, c_ld + extra_ld) + b.header(lang, path, alt, nav=False)
            + f'<main id="main" class="{cls}">\n{c_html}\n{body}\n</main>\n{script}' + b.footer(lang))


def links_list(items):
    return '<ul class="related">' + "".join(f'<li><a href="{h}">{escape(n)}</a></li>' for h, n in items) + "</ul>"


def also(lang, skip=None):
    """Links to the other extra pages ("Also handy")."""
    items = [(p_tool(lang, t), f'{t["emoji"]} {t[lang]["short"]}') for t in TOOLS if t is not skip]
    items += [(p_list(lang, c), f'{c["emoji"]} {c[lang]["title"]}') for c in CHECKLISTS if c is not skip]
    return f'<h2>{TX[lang]["also"]}</h2>' + links_list(items)


# ---------------------------------------------------------------------------------------------- tool pages
def tool_form(lang, key):
    u = TOOL_UI[key][lang]
    if key == "age":
        return f"""<form class="tool" onsubmit="return false">
  <fieldset class="seg"><legend>{u['species']}</legend>
    <label><input type="radio" name="sp" value="dog" checked> 🐶 {u['dog']}</label>
    <label><input type="radio" name="sp" value="cat"> 🐱 {u['cat']}</label></fieldset>
  <fieldset class="seg" id="sizes"><legend>{u['size']}</legend>
    <label><input type="radio" name="size" value="4" checked> {u['small']}</label>
    <label><input type="radio" name="size" value="4.5"> {u['medium']}</label>
    <label><input type="radio" name="size" value="5.25"> {u['large']}</label></fieldset>
  <label class="field">{u['age']}<input id="age" type="number" min="0" max="30" step="0.5" value="5" inputmode="decimal"></label>
  <output class="result" id="out" aria-live="polite"></output>
</form>
<h2>{u['how']}</h2><p>{u['how_text']}</p>"""
    if key == "travel":
        rules = "".join(f"<li>{escape(r)}</li>" for r in u["rules_list"])
        blog_path = ("/blog/" if lang == "nl" else "/en/blog/") + u["blog_slug"] + "/"
        return f"""<form class="tool" onsubmit="return false">
  <label class="field">{u['mode_shot']}<input id="shot" type="date"></label>
  <output class="result" id="out1" aria-live="polite"></output>
  <label class="field">{u['mode_birth']}<input id="birth" type="date"></label>
  <output class="result" id="out2" aria-live="polite"></output>
  <p class="hint">{escape(u['birth_note'])}</p>
</form>
<h2>{u['rules']}</h2><ul>{rules}</ul>
<p><a href="{blog_path}">{escape(u['blog'])} →</a></p>"""
    return f"""<form class="tool" onsubmit="return false">
  <div class="row2">
    <label class="field">{u['bag']}<input id="bag" type="number" min="0.1" step="0.1" value="12" inputmode="decimal"></label>
    <label class="field">{u['daily']}<input id="daily" type="number" min="1" step="1" value="300" inputmode="numeric"></label>
  </div>
  <div class="row2">
    <label class="field">{u['opened']}<input id="opened" type="date"></label>
    <label class="field">{u['price']}<input id="price" type="number" min="0" step="0.01" inputmode="decimal"></label>
  </div>
  <output class="result" id="out" aria-live="polite"></output>
</form>
<p>{escape(u['tip'])}</p>"""


def tool_script(lang, key):
    u = TOOL_UI[key][lang]
    loc = "nl-NL" if lang == "nl" else "en-GB"
    common = f"""var L='{loc}';function $(i){{return document.getElementById(i)}}
function fmt(d){{return d.toLocaleDateString(L,{{weekday:'long',day:'numeric',month:'long',year:'numeric'}})}}
function addDays(d,n){{var x=new Date(d);x.setDate(x.getDate()+n);return x}}
function parse(v){{if(!v)return null;var p=v.split('-');return new Date(+p[0],+p[1]-1,+p[2])}}
document.querySelectorAll('.tool input').forEach(function(i){{i.addEventListener('input',calc);i.addEventListener('change',calc)}});"""
    if key == "age":
        stages = json.dumps(u["stage"], ensure_ascii=False)
        return f"""<script>{common}
var S={stages};
function calc(){{var cat=document.querySelector('input[name=sp]:checked').value==='cat';
$('sizes').style.display=cat?'none':'';
var per=cat?4:parseFloat(document.querySelector('input[name=size]:checked').value);
var a=parseFloat(($('age').value||'').replace(',','.'));if(isNaN(a)||a<0){{$('out').innerHTML='';return}}
var h=a<=1?a*15:a<=2?15+(a-1)*9:24+(a-2)*per;
var st=a<1?0:a<3?1:a<(cat?11:(per>5?7:per>4?9:10))?2:3;
$('out').innerHTML='<b>'+Math.round(h)+'</b> {u['result']}<span>'+S[st]+'</span>'}}
calc();</script>"""
    if key == "travel":
        return f"""<script>{common}
function calc(){{var s=parse($('shot').value),b=parse($('birth').value);
$('out1').innerHTML=s?'{escape(u['res_shot'])}<b>'+fmt(addDays(s,21))+'</b>':'';
$('out2').innerHTML=b?'{escape(u['res_birth'])}<b>'+fmt(addDays(b,12*7+21))+'</b>':''}}
calc();</script>"""
    return f"""<script>{common}
var t=new Date();$('opened').value=t.toISOString().slice(0,10);
function money(v){{return v.toLocaleString(L,{{style:'currency',currency:'EUR'}})}}
function calc(){{var bag=parseFloat(($('bag').value||'').replace(',','.'))*1000,d=parseFloat($('daily').value),o=parse($('opened').value)||new Date();
if(!(bag>0&&d>0)){{$('out').innerHTML='';return}}var days=Math.floor(bag/d);
var h='<b>'+days+'</b> {u['days']}<span>{escape(u['runs_out'])} '+fmt(addDays(o,days))+'</span>';
var p=parseFloat(($('price').value||'').replace(',','.'));if(p>0){{var pd=p/(bag/d);h+='<span>{escape(u['per_day'])}: '+money(pd)+' · {escape(u['per_month'])}: '+money(pd*30.4)+'</span>'}}
$('out').innerHTML=h}}
calc();</script>"""


def tool_page(b, lang, t):
    o = other(lang)
    x = t[lang]
    path, alt = p_tool(lang, t), p_tool(o, t)
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (TX[lang]["tools"], TX[lang]["tools_path"]), (x["short"], path)]
    ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": x["title"], "description": x["desc"],
          "url": b.DOMAIN + path, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "inLanguage": lang,
          "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
          "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"}}
    body = f"""<p class="post-emoji" aria-hidden="true">{t['emoji']}</p>
<h1>{escape(x['title'])}</h1>
<p class="summary">{escape(x['intro'])}</p>
{tool_form(lang, t['key'])}
<p class="meta"><em>{escape(TX[lang]['disclaimer'])}</em></p>
{cta(b, lang)}
{also(lang, t)}"""
    return page(b, lang, f'{x["title"]} | {b.T[lang]["name"]}', x["desc"], path, alt, trail, body,
                extra_ld=f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n',
                script=tool_script(lang, t["key"]))


def hub(b, lang, kind):
    """Overview page of tools, species or checklists."""
    x = TX[lang]
    o = other(lang)
    if kind == "tools":
        name, path, alt, title, desc, lead = x["tools"], x["tools_path"], TX[o]["tools_path"], x["tools_title"], x["tools_desc"], x["tools_lead"]
        cards = [(p_tool(lang, t), t["emoji"], t[lang]["short"], t[lang]["desc"]) for t in TOOLS]
    elif kind == "species":
        name, path, alt, title, desc, lead = x["species"], x["species_path"], TX[o]["species_path"], x["species_title"], x["species_desc"], x["species_lead"]
        cards = [(p_species(lang, s), s["emoji"], s[lang]["h1"], s[lang]["desc"]) for s in SPECIES]
    else:
        name, path, alt, title, desc, lead = x["lists"], x["lists_path"], TX[o]["lists_path"], x["lists_title"], x["lists_desc"], x["lists_lead"]
        cards = [(p_list(lang, c), c["emoji"], c[lang]["title"], c[lang]["desc"]) for c in CHECKLISTS]
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (name, path)]
    grid = "".join(f'<a class="post-card" href="{h}"><span class="post-ico" aria-hidden="true">{e}</span>'
                   f'<h2>{escape(n)}</h2><p>{escape(d)}</p><span class="post-meta">{x["open"]} →</span></a>' for h, e, n, d in cards)
    body = f"""<div class="wrap">
<h1>{escape(name)}</h1>
<p class="lead" style="margin-top:12px">{escape(lead)}</p>
<div class="post-grid">{grid}</div>
</div>"""
    c_html, c_ld = b.crumbs(lang, trail)
    return (b.head(lang, title, desc, path, alt, lang, c_ld) + b.header(lang, path, alt, nav=False)
            + f'<main id="main" class="blog">\n<div class="wrap">{c_html}</div>\n{body}\n</main>\n' + b.footer(lang))


# ---------------------------------------------------------------------------------------------- species pages
def species_page(b, lang, s):
    o = other(lang)
    x = s[lang]
    t = TX[lang]
    path, alt = p_species(lang, s), p_species(o, s)
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (t["species"], t["species_path"]), (x["h1"], path)]
    vacc = ("<ul>" + "".join(f"<li>{escape(v)}</li>" for v in x["vacc"]) + f'</ul><p class="meta"><em>{escape(t["vacc_note"])}</em></p>'
            if x["vacc"] else f"<p>{escape(NO_VACC[lang])}</p>")
    others = [(p_species(lang, z), f'{z["emoji"]} {z[lang]["h1"]}') for z in SPECIES if z is not s]
    body = f"""<p class="post-emoji" aria-hidden="true">{s['emoji']}</p>
<h1>{escape(x['h1'])}</h1>
<p class="summary">{escape(x['lead'])}</p>
<h2>{t['vacc']}</h2>
{vacc}
<h2>{t['track']}</h2>
<ul>{''.join(f'<li>{escape(v)}</li>' for v in x['track'])}</ul>
<h2>{t['tips']}</h2>
<ul>{''.join(f'<li>{escape(v)}</li>' for v in x['tips'])}</ul>
<h2>{t['app']}</h2>
<p>{escape(x['app'])}</p>
{cta(b, lang)}
<h2>{t['also']}</h2>
{links_list(others + [(p_tool(lang, TOOLS[0]), f'{TOOLS[0]["emoji"]} {TOOLS[0][lang]["short"]}')])}"""
    return page(b, lang, f'{x["title"]} | {b.T[lang]["name"]}', x["desc"], path, alt, trail, body)


# ---------------------------------------------------------------------------------------------- checklists
def checklist_html(lang, c, printable=False):
    x = c[lang]
    groups = []
    for gi, (h, items) in enumerate(x["groups"]):
        lis = "".join(f'<li><label><input type="checkbox" data-k="{c["key"]}-{gi}-{ii}"> <span>{escape(it)}</span></label></li>'
                      for ii, it in enumerate(items))
        groups.append(f'<div class="cl-group"><h2>{escape(h)}</h2><ul class="checklist">{lis}</ul></div>')
    return "".join(groups)


def checklist_page(b, lang, c):
    o = other(lang)
    x = c[lang]
    t = TX[lang]
    path, alt = p_list(lang, c), p_list(o, c)
    pdf = f'{t["lists_path"]}{x["slug"]}.pdf'
    trail = [(b.T[lang]["name"], b.T[lang]["path"]), (t["lists"], t["lists_path"]), (x["title"], path)]
    body = f"""<p class="post-emoji" aria-hidden="true">{c['emoji']}</p>
<h1>{escape(x['h1'])}</h1>
<p class="summary">{escape(x['lead'])}</p>
<div class="actions no-print"><a class="btn btn-primary" href="{pdf}" download>{t['pdf']}</a><button class="btn btn-ghost" type="button" onclick="window.print()">{t['print']}</button></div>
{checklist_html(lang, c)}
<p class="meta no-print"><em>{escape(t['checked'])}</em> <button class="linkbtn" type="button" id="reset">{t['reset']}</button></p>
<div class="no-print">{cta(b, lang)}
{also(lang, c)}</div>"""
    script = """<script>(function(){var k='kb-cl-';document.querySelectorAll('.checklist input').forEach(function(i){
try{i.checked=localStorage.getItem(k+i.dataset.k)==='1'}catch(e){}
i.addEventListener('change',function(){try{localStorage.setItem(k+i.dataset.k,i.checked?'1':'0')}catch(e){}})});
var r=document.getElementById('reset');if(r)r.addEventListener('click',function(){document.querySelectorAll('.checklist input').forEach(function(i){i.checked=false;try{localStorage.removeItem(k+i.dataset.k)}catch(e){}})})})();</script>
"""
    return page(b, lang, f'{x["title"]} | {b.T[lang]["name"]}', x["desc"], path, alt, trail, body, script=script)


def checklist_print(b, lang, c):
    """A bare, print-only page used to render the PDF."""
    x = c[lang]
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{escape(x['title'])}</title>
<link rel="stylesheet" href="/assets/site.css?v={b.CSS_V}"><style>@page{{size:A4;margin:16mm 16mm 14mm}}body{{background:#fff}}
.sheet{{max-width:none;padding:0}}.sheet h1{{font-size:28px;margin:0 0 4px}}.sheet .lead{{margin:0 0 14px;font-size:14px}}
.cl-group{{break-inside:avoid}}.cl-group h2{{font-size:17px;margin:14px 0 6px}}.checklist li{{font-size:13.5px;padding:4px 0}}
.brandline{{display:flex;align-items:center;gap:10px;margin-bottom:14px;font-weight:900;color:#2B7A9E}}.brandline img{{width:34px;height:34px;border-radius:9px}}
.foot{{margin-top:18px;font-size:11px;color:#5B6B78}}</style></head><body><main class="legal sheet">
<div class="brandline"><img src="/assets/img/icon.webp" alt="">{b.T[lang]['name']} · {'kwispelboek.app' if lang == 'nl' else 'wagbook.app'}</div>
<h1>{escape(x['h1'])}</h1><p class="lead">{escape(x['lead'])}</p>
{checklist_html(lang, c, printable=True)}
<p class="foot">{escape(TX[lang]['cta_text'])}</p></main></body></html>"""


# ---------------------------------------------------------------------------------------------- build
def pages():
    """(nl_path, en_path, date) for the sitemap."""
    rows = [(TX["nl"][k], TX["en"][k], DATE) for k in ("tools_path", "species_path", "lists_path")]
    rows += [(p_tool("nl", t), p_tool("en", t), DATE) for t in TOOLS]
    rows += [(p_species("nl", s), p_species("en", s), DATE) for s in SPECIES]
    rows += [(p_list("nl", c), p_list("en", c), DATE) for c in CHECKLISTS]
    return rows


def llms_lines(lang, domain):
    out = [f"- [{t[lang]['title']}]({domain}{p_tool(lang, t).removeprefix('/en')}): {t[lang]['desc']}" for t in TOOLS]
    out += [f"- [{s[lang]['title']}]({domain}{p_species(lang, s).removeprefix('/en')}): {s[lang]['desc']}" for s in SPECIES]
    out += [f"- [{c[lang]['title']}]({domain}{p_list(lang, c).removeprefix('/en')}): {c[lang]['desc']}" for c in CHECKLISTS]
    return out


def build(b):
    for lang, w in (("nl", b.write), ("en", b.write_en)):
        def rel(path):
            return (path.removeprefix("/en") if lang == "en" else path).lstrip("/") + "index.html"
        w(rel(TX[lang]["tools_path"]), hub(b, lang, "tools"))
        w(rel(TX[lang]["species_path"]), hub(b, lang, "species"))
        w(rel(TX[lang]["lists_path"]), hub(b, lang, "lists"))
        for t in TOOLS:
            w(rel(p_tool(lang, t)), tool_page(b, lang, t))
        for s in SPECIES:
            w(rel(p_species(lang, s)), species_page(b, lang, s))
        for c in CHECKLISTS:
            w(rel(p_list(lang, c)), checklist_page(b, lang, c))
            # print source for the PDF (not linked, not in the sitemap)
            site = b.SITE if lang == "nl" else b.EN_SITE
            b.out(site / "_print" / f"{c[lang]['slug']}.html", checklist_print(b, lang, c))
    b.write("video/index.html", video_page(b))


# ---------------------------------------------------------------------------------------------- video page (NL only)
VIDEO = {
    "id": "1M8IMolNsa4",
    "path": "/video/",
    "upload": "2026-11-09T08:00:28-08:00",
    "duration": "PT1M28S",
    "thumb": "/assets/img/video-nl.webp",
    "name": "Kwispelboek – Nooit meer vergeten wanneer je huisdier ontwormd of gevaccineerd moet worden",
    "title": "Video: zo werkt Kwispelboek | Kwispelboek",
    "h1": "Zo werkt Kwispelboek",
    "crumb": "Video",
    "desc": "Bekijk in anderhalve minuut hoe Kwispelboek je helpt herinneren aan ontworming, vaccinaties, medicijnen en gewicht van je hond, kat of konijn.",
    "lead": "In anderhalve minuut zie je hoe je je dier toevoegt, zorg afvinkt en op tijd een herinnering krijgt.",
    "play": "Video afspelen",
    "consent": "De video wordt pas van YouTube geladen als je op afspelen drukt.",
    "watch": "Bekijk op YouTube",
    "points_h": "Wat je in de video ziet",
    "points": [
        "Je dier toevoegen, met foto, soort en geboortedatum",
        "Ontworming, vlooien en vaccinaties met een herinnering op tijd",
        "Afvinken op het scherm Vandaag, met een feestje van Kwispel",
        "Het profiel met zorg, gezondheid en paspoort per dier",
        "De agenda met alles wat eraan komt",
    ],
}


def video_page(b):
    v = VIDEO
    url = b.DOMAIN + v["path"]
    ld = {"@context": "https://schema.org", "@type": "VideoObject", "name": v["name"], "description": v["desc"],
          "thumbnailUrl": [b.DOMAIN + v["thumb"], f"https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg"],
          "uploadDate": v["upload"], "duration": v["duration"], "inLanguage": "nl",
          "embedUrl": f"https://www.youtube-nocookie.com/embed/{v['id']}",
          "contentUrl": f"https://www.youtube.com/watch?v={v['id']}", "url": url,
          "publisher": {"@type": "Organization", "name": "Grounded Studio", "url": "https://grounded-studio.app/"}}
    ld_html = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n'
    trail = [(b.T["nl"]["name"], b.T["nl"]["path"]), (v["crumb"], v["path"])]
    points = "".join(f"<li>{escape(p)}</li>" for p in v["points"])
    body = f"""<h1>{escape(v['h1'])}</h1>
<p class="lead">{escape(v['lead'])}</p>
<div class="video" id="video">
  <button type="button" class="video-play" aria-label="{escape(v['play'])}">
    <img src="{v['thumb']}" alt="{escape(v['name'])}" width="1280" height="720" loading="eager">
    <span class="video-btn" aria-hidden="true"></span>
  </button>
</div>
<p class="meta">{escape(v['consent'])} <a href="https://www.youtube.com/watch?v={v['id']}" rel="noopener">{escape(v['watch'])}</a></p>
<h2>{escape(v['points_h'])}</h2>
<ul>{points}</ul>
{cta(b, "nl")}
{also("nl")}"""
    script = (f"<script>document.querySelector('.video-play').addEventListener('click',function(){{"
              f"var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/{v['id']}?autoplay=1&rel=0';"
              f"f.title={json.dumps(v['name'], ensure_ascii=False)};f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';"
              f"f.allowFullscreen=true;var d=document.getElementById('video');d.innerHTML='';d.appendChild(f)}});</script>\n")
    html = page(b, "nl", v["title"], v["desc"], v["path"], b.T["en"]["path"], trail, body, extra_ld=ld_html, script=script)
    # Dutch only: no English alternate for this page.
    html = re.sub(r'<link rel="alternate" hreflang="en"[^>]*>\n', "", html)
    html = re.sub(r'(<link rel="alternate" hreflang="x-default" href=")[^"]*', r"\g<1>" + url, html)
    return html


def video_sitemap_row(b):
    v = VIDEO
    return f"""  <url>
    <loc>{b.DOMAIN}{v['path']}</loc>
    <lastmod>{b.page_lastmod(b.SITE, 'video/index.html', DATE)}</lastmod>
    <video:video>
      <video:thumbnail_loc>{b.DOMAIN}{v['thumb']}</video:thumbnail_loc>
      <video:title>{escape(v['name'])}</video:title>
      <video:description>{escape(v['desc'])}</video:description>
      <video:player_loc>https://www.youtube-nocookie.com/embed/{v['id']}</video:player_loc>
      <video:duration>88</video:duration>
      <video:publication_date>{v['upload']}</video:publication_date>
      <video:family_friendly>yes</video:family_friendly>
    </video:video>
  </url>"""
