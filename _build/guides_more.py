"""Five more guides (travel, fleas & ticks, weight, toxic food, lost pet).

Same rule as guides.py: every health or legal fact comes from a source listed with the guide,
read in full before writing. No numbers or schedules that are not in those sources.
"""

MORE_SRC = {
    "eu_travel": {"nl": ("Your Europe (Europese Unie) – Huisdieren meenemen op reis in de EU",
                         "https://europa.eu/youreurope/citizens/travel/carry/animal-plant/index_nl.htm"),
                  "en": ("Your Europe (European Union) – Travelling with pets and other animals in the EU",
                         "https://europa.eu/youreurope/citizens/travel/carry/animal-plant/index_en.htm")},
    "icatcare_perm": ("International Cat Care – Permethrin poisoning", "https://icatcare.org/advice/permethrin-poisoning/"),
    "wsava_bcs": ("WSAVA – Body Condition Score (hond en kat, 9-puntsschaal)",
                  "https://vmc.vet.osu.edu/sites/default/files/documents/wsava-bcs-chart-dogs-cats.pdf"),
    "aspca_food": ("ASPCA Animal Poison Control – People foods to avoid feeding your pets",
                   "https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets"),
    "knmvd_xyl": ("KNMvD – Zoetstoffen en xylitol bij de hond (tabellen)",
                  "https://www.knmvd.nl/app/uploads/2019/02/Referenties-en-tabellen-Xylitol.pdf"),
    "fda_lily": ("U.S. FDA – Lovely lilies and curious cats: a dangerous combination",
                 "https://www.fda.gov/animal-veterinary/animal-health-literacy/lovely-lilies-and-curious-cats-dangerous-combination"),
    "licg_lost": ("LICG – Vermiste of gevonden dieren", "https://www.licg.nl/vermiste-of-gevonden-dieren/"),
    "licg_chip": ("LICG – Chippen en registreren", "https://www.licg.nl/chippen-en-registreren/"),
    "chip_dog": ("Chip je dier (LICG) – Chip en registratie verplicht voor honden",
                 "https://www.chipjedier.nl/verplicht-voor-honden/chip-en-registratie-verplicht-voor-honden/"),
    "chip_cat": ("Chip je dier (LICG) – Toekomstige chipverplichting voor katten",
                 "https://www.chipjedier.nl/chip-je-kat/toekomstige-chipverplichting-voor-katten/"),
}

# Old blog articles whose topic moved into a guide: key -> guide key. The old URLs redirect.
MOVED = {"travel": "travel", "fleas": "fleas", "weight": "weight"}

G = "/gidsen/"
E = "/en/guides/"

MORE_GUIDES = [
    # ------------------------------------------------------------------ travel
    {
        "key": "travel", "emoji": "✈️", "sources": ["eu_travel"],
        "related": {"nl": [("/hulpmiddelen/21-dagenregel/", "Rekenhulp: de 21-dagenregel"),
                           ("/checklists/op-vakantie/", "Checklist: op vakantie met je huisdier"),
                           (G + "vlooien-en-teken-hond-kat/", "Vlooien en teken: hoe vaak behandelen?"),
                           (G + "vaccinatieschema-pup-kitten/", "Vaccinatieschema voor pup en kitten")],
                    "en": [("/en/tools/21-day-rule/", "Calculator: the 21-day rule"),
                           ("/en/checklists/holiday/", "Checklist: on holiday with your pet"),
                           (E + "fleas-and-ticks-dog-cat/", "Fleas and ticks: how often to treat?"),
                           (E + "puppy-kitten-vaccination-schedule/", "Puppy and kitten vaccination schedule")]},
        "nl": {
            "slug": "op-reis-met-huisdier-buitenland",
            "title": "Met hond of kat naar het buitenland: wat heb je nodig? | Kwispelboek",
            "h1": "Wat heb je nodig om met je hond of kat naar het buitenland te gaan?",
            "short": "Op reis met je huisdier",
            "desc": "Chip, Europees dierenpaspoort, rabiësvaccinatie en de 21-dagenregel: de EU-regels voor reizen met je hond of kat op een rij, met tabel en FAQ.",
            "intro": "Binnen de EU heeft je hond of kat drie dingen nodig: een chip, een Europees dierenpaspoort en een geldige vaccinatie tegen hondsdolheid (rabiës). De chip moet erin zitten vóór de rabiësprik. Die eerste prik mag vanaf 12 weken, en daarna wacht je minstens 21 dagen voordat je gaat reizen. Naar Finland, Ierland, Malta, Noorwegen en Noord-Ierland krijgt je hond ook een behandeling tegen lintworm.",
            "table": (["Wat", "Regel binnen de EU"], [
                ["Chip", "Verplicht, en aangebracht vóór de rabiësprik (een leesbare tatoeage van vóór 3 juli 2011 telt ook)"],
                ["Rabiësvaccinatie", "Eerste prik op minstens 12 weken oud"],
                ["Wachttijd", "Minstens 21 dagen na de eerste prik"],
                ["Herhaalprik", "Geven voordat de vorige verloopt; te laat telt als nieuwe eerste prik, met wachttijd"],
                ["Europees dierenpaspoort", "Verplicht voor honden, katten en fretten; levenslang geldig als de gegevens kloppen"],
                ["Lintworm (alleen honden)", "Naar Finland, Ierland, Malta, Noorwegen en Noord-Ierland: 24 tot 120 uur voor de reis"],
                ["Aantal dieren", "Maximaal 5, met uitzonderingen voor wedstrijden en tentoonstellingen"],
            ]),
            "sections": [
                ("Eerst de chip, dan de rabiësprik", [
                    "Volgens de EU-regels moet je hond of kat gechipt zijn. Een duidelijk leesbare tatoeage telt ook, maar alleen als die vóór 3 juli 2011 is aangebracht. De volgorde is belangrijk: een rabiësvaccinatie is alleen geldig als je dier op het moment van de prik al gechipt was. Is de prik eerder gegeven dan de chip, dan telt hij voor reizen niet.",
                ]),
                ("Rabiës en de 21-dagenregel", [
                    "Je dier moet minstens 12 weken oud zijn bij de eerste rabiësprik. Na die eerste prik wacht je minstens 21 dagen voordat je met je dier gaat reizen. Reken dus terug vanaf je vertrekdatum: een pup of kitten is op zijn vroegst rond 15 weken klaar om te reizen.",
                    "Een herhaalprik moet gegeven worden voordat de vorige vaccinatie verloopt. Ben je te laat, dan telt de nieuwe prik als een eerste vaccinatie en geldt de wachttijd van 21 dagen opnieuw. Houd de vervaldatum dus goed in de gaten.",
                    "Jonge dieren zonder volledige rabiësbescherming mogen alleen onder voorwaarden naar een klein aantal EU-landen. Nederland, België, Duitsland en Frankrijk staan daar niet bij.",
                ]),
                ("Het Europees dierenpaspoort", [
                    "Voor reizen binnen de EU hebben honden, katten en fretten een Europees dierenpaspoort nodig. Je dierenarts vult het in, met onder meer het chipnummer en de rabiësvaccinatie. Het paspoort blijft je hele leven geldig, zolang de gezondheidsgegevens erin actueel zijn. Let op: paspoorten die in Groot-Brittannië zijn afgegeven, zijn sinds 1 januari 2021 niet meer geldig in de EU.",
                ]),
                ("Lintworm: alleen voor sommige landen", [
                    "Ga je met je hond naar Finland, Ierland, Malta, Noorwegen of Noord-Ierland? Dan moet je hond behandeld worden tegen de lintworm Echinococcus multilocularis, 24 tot 120 uur (1 tot 5 dagen) voor de reis, en de dierenarts noteert dat in het paspoort. Reis je rechtstreeks tussen die landen, dan hoeft het niet.",
                ]),
                ("Buiten de EU", [
                    "Voor de meeste landen buiten de EU is meer nodig, zoals een bloedtest die laat zien dat de rabiësvaccinatie werkt. Volgens de EU wordt dat bloed op zijn vroegst 30 dagen na de vaccinatie afgenomen, en daarna wacht je nog 3 maanden voordat je met je dier de EU weer in mag. Begin dus maanden van tevoren en kijk altijd op de site van de overheid van je bestemming.",
                ]),
            ],
            "faq": [
                ("Heeft een kat ook een dierenpaspoort nodig?", "Ja. Binnen de EU geldt het Europees dierenpaspoort voor honden, katten en fretten, samen met de chip en de rabiësvaccinatie."),
                ("Hoe jong mag mijn pup mee op vakantie?", "De eerste rabiësprik mag vanaf 12 weken. Daarna wacht je minstens 21 dagen, dus rond 15 weken. Jongere dieren mogen alleen onder voorwaarden naar een paar landen; Nederland, België, Duitsland en Frankrijk horen daar niet bij."),
                ("Ik ben de herhaalprik tegen rabiës vergeten. Wat nu?", "Dan telt de nieuwe prik als een eerste vaccinatie, en wacht je weer minstens 21 dagen voordat je met je dier mag reizen."),
                ("Moet mijn hond ontwormd worden voor de reis?", "Alleen naar Finland, Ierland, Malta, Noorwegen en Noord-Ierland is een lintwormbehandeling verplicht, 24 tot 120 uur voor de reis. Je dierenarts noteert die in het paspoort."),
                ("Hoeveel huisdieren mag ik meenemen?", "Maximaal 5. Meer mag alleen als de dieren meedoen aan een wedstrijd, tentoonstelling of sportevenement en ouder zijn dan 6 maanden."),
            ],
            "app": "In Kwispelboek vul je je bestemming en reisdatum in. De reischecklist kijkt of chip, paspoort en rabiës op tijd in orde zijn en waarschuwt als de 21 dagen nog niet voorbij zijn.",
        },
        "en": {
            "slug": "travelling-abroad-with-pet",
            "title": "Travelling abroad with your dog or cat: what you need | Wagbook",
            "h1": "What do you need to travel abroad with your dog or cat?",
            "short": "Travelling with your pet",
            "desc": "Microchip, EU pet passport, rabies vaccination and the 21-day rule: the EU rules for travelling with your dog or cat, with a table and FAQ.",
            "intro": "Within the EU, your dog or cat needs three things: a microchip, an EU pet passport and a valid rabies vaccination. The chip must be in place before the rabies jab. That first jab is allowed from 12 weeks, and after it you wait at least 21 days before travelling. For Finland, Ireland, Malta, Norway and Northern Ireland, your dog also needs a tapeworm treatment.",
            "table": (["What", "Rule within the EU"], [
                ["Microchip", "Required, and implanted before the rabies jab (a legible tattoo from before 3 July 2011 also counts)"],
                ["Rabies vaccination", "First jab at least 12 weeks old"],
                ["Waiting time", "At least 21 days after the first jab"],
                ["Booster", "Give it before the previous one expires; late counts as a new first jab, with waiting time"],
                ["EU pet passport", "Required for dogs, cats and ferrets; valid for life if the details are up to date"],
                ["Tapeworm (dogs only)", "To Finland, Ireland, Malta, Norway and Northern Ireland: 24 to 120 hours before travel"],
                ["Number of pets", "At most 5, with exceptions for competitions and shows"],
            ]),
            "sections": [
                ("First the microchip, then the rabies jab", [
                    "Under EU rules your dog or cat must be microchipped. A clearly legible tattoo also counts, but only if it was applied before 3 July 2011. The order matters: a rabies vaccination is only valid if your pet was already microchipped when it was given. If the jab came before the chip, it doesn’t count for travel.",
                ]),
                ("Rabies and the 21-day rule", [
                    "Your pet must be at least 12 weeks old at the first rabies jab. After that first jab you wait at least 21 days before travelling with your pet. So count back from your departure date: a puppy or kitten is ready to travel at about 15 weeks at the earliest.",
                    "A booster must be given before the previous vaccination expires. If you are late, the new jab counts as a first vaccination and the 21-day wait applies again. So keep a close eye on the expiry date.",
                    "Young animals without full rabies protection may only travel to a small number of EU countries, under conditions. The Netherlands, Belgium, Germany and France are not among them.",
                ]),
                ("The EU pet passport", [
                    "To travel within the EU, dogs, cats and ferrets need an EU pet passport. Your vet fills it in, including the microchip number and the rabies vaccination. The passport is valid for life, as long as the health details in it are up to date. Note: passports issued in Great Britain are no longer valid in the EU since 1 January 2021.",
                ]),
                ("Tapeworm: only for some countries", [
                    "Taking your dog to Finland, Ireland, Malta, Norway or Northern Ireland? Then your dog must be treated against the tapeworm Echinococcus multilocularis 24 to 120 hours (1 to 5 days) before travelling, and the vet records it in the passport. Travelling directly between those countries, it isn’t needed.",
                ]),
                ("Outside the EU", [
                    "Most countries outside the EU require more, such as a blood test showing that the rabies vaccination works. According to the EU, that blood is taken no earlier than 30 days after vaccination, and then you wait another 3 months before you may bring your pet back into the EU. So start months ahead and always check the government website of your destination.",
                ]),
            ],
            "faq": [
                ("Does a cat need a pet passport too?", "Yes. Within the EU the pet passport applies to dogs, cats and ferrets, together with the microchip and the rabies vaccination."),
                ("How young can my puppy come on holiday?", "The first rabies jab is allowed from 12 weeks. Then you wait at least 21 days, so about 15 weeks. Younger animals may only travel to a few countries under conditions; the Netherlands, Belgium, Germany and France are not among them."),
                ("I forgot the rabies booster. What now?", "Then the new jab counts as a first vaccination, and you wait at least 21 days again before you may travel with your pet."),
                ("Does my dog need deworming before the trip?", "Only for Finland, Ireland, Malta, Norway and Northern Ireland is a tapeworm treatment required, 24 to 120 hours before travel. Your vet records it in the passport."),
                ("How many pets may I take?", "At most 5. More is only allowed if the animals take part in a competition, show or sports event and are older than 6 months."),
            ],
            "app": "In Wagbook you enter your destination and travel date. The travel checklist checks whether microchip, passport and rabies are in order in time and warns you if the 21 days haven’t passed yet.",
        },
    },
    # ------------------------------------------------------------------ fleas & ticks
    {
        "key": "fleas", "emoji": "🐛", "sources": ["esccap_nl", "icatcare_perm"],
        "related": {"nl": [(G + "hoe-vaak-ontwormen-hond-kat/", "Hoe vaak moet je je hond of kat ontwormen?"),
                           (G + "op-reis-met-huisdier-buitenland/", "Met je huisdier naar het buitenland"),
                           (G + "giftig-eten-hond-kat/", "Welk eten is giftig voor je hond of kat?"),
                           ("/voor/kat/", "Kwispelboek voor je kat")],
                    "en": [(E + "how-often-deworm-dog-cat/", "How often should you deworm your dog or cat?"),
                           (E + "travelling-abroad-with-pet/", "Travelling abroad with your pet"),
                           (E + "toxic-foods-dogs-cats/", "Which foods are toxic to dogs and cats?"),
                           ("/en/for/cats/", "Wagbook for your cat")]},
        "nl": {
            "slug": "vlooien-en-teken-hond-kat",
            "title": "Vlooien en teken bij hond en kat: hoe vaak behandelen? | Kwispelboek",
            "h1": "Hoe vaak moet je je hond of kat behandelen tegen vlooien en teken?",
            "short": "Vlooien en teken",
            "desc": "Vlooien zijn het hele jaar een risico, teken vooral in het seizoen. Wat ESCCAP adviseert, en waarom een vlooienmiddel voor honden gevaarlijk is voor katten.",
            "intro": "Hoe vaak je behandelt, hangt af van het middel en van het risico voor jouw dier; volg de bijsluiter en je dierenarts. Volgens de Europese parasitologen van ESCCAP zijn vlooien het hele jaar door een risico, en is tekenbestrijding nodig voor honden en katten die kans lopen op teken, vooral in het tekenseizoen. Gebruik nooit een vlooienmiddel voor honden bij een kat: sommige bevatten permethrine, en dat is voor katten zeer giftig.",
            "table": (["Onderwerp", "Wat de bronnen zeggen"], [
                ["Vlooien", "Het hele jaar door een risico; behandelen op basis van een risicobeoordeling"],
                ["Vlooienplaag in huis", "Zonder vaste bestrijding duurt het minstens 3 maanden voordat een plaag onder controle is; behandel ook de omgeving"],
                ["Teken", "Bestrijding nodig bij risico op teken; groter risico in het tekenseizoen, soms het hele jaar"],
                ["Hoe vaak", "Hangt af van het middel: volg de bijsluiter en je dierenarts"],
                ["Hondenmiddel bij een kat", "Nooit: permethrine is zeer giftig voor katten, al in een heel kleine hoeveelheid"],
                ["Bespreken", "Minstens elke 12 maanden met je dierenarts, bijvoorbeeld bij de jaarlijkse controle"],
            ]),
            "sections": [
                ("Vlooien: het hele jaar door", [
                    "ESCCAP schrijft dat vlooien het hele jaar door een risico zijn voor huisdieren, en dat je blootstelling moeilijk kunt vermijden. Of en hoe vaak je een vlooienmiddel gebruikt, beslis je op basis van een risicobeoordeling: komt je dier buiten, zijn er andere dieren in huis, heeft het eerder vlooien gehad?",
                    "Is er eenmaal een vlooienplaag, dan duurt het zonder vaste vlooienbestrijding minstens 3 maanden voordat die onder controle is. ESCCAP adviseert daarom om de behandeling van je dier te combineren met een behandeling van de omgeving, zoals manden, kleden en de plekken waar je dier ligt.",
                ]),
                ("Teken: vooral in het seizoen", [
                    "Tekenbestrijding is volgens ESCCAP nodig voor honden en katten die risico lopen op teken. Dat risico is groter in het tekenseizoen, maar in sommige landen kun je het hele jaar door teken tegenkomen.",
                    "Ga je met je hond naar Zuid-Europa? In gebieden waar leishmania voorkomt, adviseert ESCCAP honden te beschermen met een middel dat zandvliegen afweert, en in gebieden met hartworm een preventieve behandeling. Je dierenarts weet wat er op je bestemming nodig is.",
                ]),
                ("Hoe vaak? Dat hangt af van het middel", [
                    "Er is niet één schema voor elk dier. Druppels, tabletten en banden werken allemaal anders lang. Lees de bijsluiter en vraag je dierenarts welk middel past bij de leeftijd, het gewicht en de leefstijl van je dier. ESCCAP raadt aan de bestrijding van parasieten minstens elke 12 maanden met je dierenarts te bespreken.",
                ]),
                ("Pas op: hondenmiddel is gevaarlijk voor katten", [
                    "Sommige vlooienmiddelen voor honden bevatten permethrine. Volgens International Cat Care kan al een heel kleine hoeveelheid een kat ernstig ziek maken. Het gaat vaak mis als een baasje per ongeluk een hondenmiddel bij de kat gebruikt, of denkt dat een klein beetje wel kan. Een kat kan permethrine ook binnenkrijgen door tegen een behandelde hond aan te liggen.",
                    "Signalen zijn trillen, schokken, overgevoeligheid voor aanraking en geluid, en wankel lopen; in ernstige gevallen krijgt een kat aanvallen. Denk je dat je kat met permethrine in aanraking is gekomen? Neem dan meteen contact op met je dierenarts. Behandel je een hond met een middel met permethrine, houd hond en kat dan 72 uur uit elkaar.",
                ]),
            ],
            "faq": [
                ("Hoe vaak moet ik mijn hond behandelen tegen vlooien?", "Dat hangt af van het middel en het risico voor je hond. Volg de bijsluiter en het advies van je dierenarts. Vlooien zijn volgens ESCCAP het hele jaar door een risico."),
                ("Moet ik ook in de winter tegen vlooien behandelen?", "Vlooien zijn het hele jaar door een risico, dus de winter is geen reden om zonder meer te stoppen. Bespreek met je dierenarts wat voor jouw dier nodig is."),
                ("Mag ik een vlooienmiddel voor honden bij mijn kat gebruiken?", "Nee, nooit. Sommige hondenmiddelen bevatten permethrine, en al een heel kleine hoeveelheid kan een kat ernstig ziek maken. Gebruik alleen middelen die voor katten bedoeld zijn."),
                ("Hoe lang duurt het voordat een vlooienplaag weg is?", "Zonder vaste bestrijding minstens 3 maanden. Behandel daarom niet alleen je dier, maar ook de omgeving."),
                ("Mijn kat heeft tegen de behandelde hond aan gelegen. Is dat erg?", "Bij een middel met permethrine kan dat gevaarlijk zijn. Let op trillen of wankel lopen en bel meteen je dierenarts. Houd hond en kat na zo’n behandeling 72 uur uit elkaar."),
            ],
            "app": "In Kwispelboek zet je je vlooien- en tekenmiddel in met het schema dat bij jouw middel hoort. Je krijgt vooraf en op de dag zelf een melding, en afvinken plant meteen de volgende keer.",
        },
        "en": {
            "slug": "fleas-and-ticks-dog-cat",
            "title": "Fleas and ticks in dogs and cats: how often to treat? | Wagbook",
            "h1": "How often should you treat your dog or cat for fleas and ticks?",
            "short": "Fleas and ticks",
            "desc": "Fleas are a year-round risk, ticks mainly in season. What ESCCAP advises, and why a dog flea product can be dangerous for cats.",
            "intro": "How often you treat depends on the product and on the risk for your pet; follow the leaflet and your vet. According to the European parasitology experts at ESCCAP, fleas are a risk all year round, and tick control is needed for dogs and cats at risk of ticks, especially in tick season. Never use a dog flea product on a cat: some contain permethrin, which is highly toxic to cats.",
            "table": (["Topic", "What the sources say"], [
                ["Fleas", "A risk all year round; treat based on a risk assessment"],
                ["Flea infestation at home", "Without routine control it takes at least 3 months to get under control; treat the environment too"],
                ["Ticks", "Control needed when there is a risk of ticks; higher in tick season, sometimes all year"],
                ["How often", "Depends on the product: follow the leaflet and your vet"],
                ["Dog product on a cat", "Never: permethrin is highly toxic to cats, even in a very small amount"],
                ["Discuss", "At least every 12 months with your vet, for example at the yearly check-up"],
            ]),
            "sections": [
                ("Fleas: all year round", [
                    "ESCCAP writes that fleas are a risk to pets all year round, and that exposure is hard to avoid. Whether and how often you use a flea product is decided on a risk assessment: does your pet go outside, are there other pets at home, has it had fleas before?",
                    "Once there is an infestation, it takes at least 3 months to get it under control without routine flea control. ESCCAP therefore advises combining treatment of your pet with treatment of the environment, such as baskets, rugs and the places where your pet lies.",
                ]),
                ("Ticks: mainly in season", [
                    "According to ESCCAP, tick control is needed for dogs and cats at risk of ticks. That risk is higher in tick season, but in some countries you can meet ticks all year round.",
                    "Taking your dog to southern Europe? In areas where leishmaniasis occurs, ESCCAP advises protecting dogs with a product that repels sand flies, and in heartworm areas a preventive treatment. Your vet knows what your destination requires.",
                ]),
                ("How often? That depends on the product", [
                    "There is no single schedule for every pet. Spot-ons, tablets and collars all last a different length of time. Read the leaflet and ask your vet which product suits your pet’s age, weight and lifestyle. ESCCAP recommends discussing parasite control with your vet at least every 12 months.",
                ]),
                ("Careful: dog products are dangerous for cats", [
                    "Some flea products for dogs contain permethrin. According to International Cat Care, even a very small amount can make a cat seriously ill. It often goes wrong when an owner uses a dog product on the cat by mistake, or thinks a small amount will be fine. A cat can also pick up permethrin by lying against a treated dog.",
                    "Signs include tremors, twitching, oversensitivity to touch and sound, and wobbly walking; in severe cases a cat has seizures. Think your cat has been exposed to permethrin? Contact your vet immediately. If you treat a dog with a permethrin product, keep dog and cat apart for 72 hours.",
                ]),
            ],
            "faq": [
                ("How often should I treat my dog for fleas?", "That depends on the product and the risk for your dog. Follow the leaflet and your vet’s advice. According to ESCCAP, fleas are a risk all year round."),
                ("Should I treat for fleas in winter too?", "Fleas are a year-round risk, so winter is no reason to simply stop. Discuss with your vet what your pet needs."),
                ("Can I use a dog flea product on my cat?", "No, never. Some dog products contain permethrin, and even a very small amount can make a cat seriously ill. Only use products made for cats."),
                ("How long does it take to get rid of a flea infestation?", "Without routine control, at least 3 months. So treat not only your pet but also the environment."),
                ("My cat lay against the treated dog. Is that a problem?", "With a permethrin product it can be dangerous. Watch for tremors or wobbly walking and call your vet straight away. Keep dog and cat apart for 72 hours after such a treatment."),
            ],
            "app": "In Wagbook you set up your flea and tick treatment with the schedule that belongs to your product. You get a reminder in advance and on the day itself, and ticking it off plans the next one straight away.",
        },
    },
    # ------------------------------------------------------------------ weight
    {
        "key": "weight", "emoji": "⚖️", "sources": ["wsava_bcs"],
        "related": {"nl": [(G + "giftig-eten-hond-kat/", "Welk eten is giftig voor je hond of kat?"),
                           ("/hulpmiddelen/voercalculator/", "Rekenhulp: hoe lang doe je met een zak voer?"),
                           ("/hulpmiddelen/leeftijd-in-mensenjaren/", "Rekenhulp: leeftijd in mensenjaren"),
                           ("/voor/hond/", "Kwispelboek voor je hond")],
                    "en": [(E + "toxic-foods-dogs-cats/", "Which foods are toxic to dogs and cats?"),
                           ("/en/tools/food-calculator/", "Calculator: how long does a bag of food last?"),
                           ("/en/tools/pet-age-in-human-years/", "Calculator: pet age in human years"),
                           ("/en/for/dogs/", "Wagbook for your dog")]},
        "nl": {
            "slug": "gezond-gewicht-hond-kat",
            "title": "Gezond gewicht van je hond of kat: zo check je het | Kwispelboek",
            "h1": "Heeft je hond of kat een gezond gewicht? Zo check je het",
            "short": "Gezond gewicht",
            "desc": "Met de Body Condition Score van de WSAVA zie je of je hond of kat te dun, ideaal of te zwaar is. Uitleg per score, een tabel en tips om bij te houden.",
            "intro": "Dierenartsen kijken niet alleen naar de weegschaal, maar ook naar de lichaamsconditie: de Body Condition Score (BCS). De wereldwijde dierenartsenorganisatie WSAVA gebruikt een schaal van 1 tot 9. Een hond zit ideaal op 4 of 5, een kat op 5. Bij een ideale score voel je de ribben zonder dat er te veel vet over zit, en zie je van bovenaf een taille achter de ribben.",
            "table": (["Score", "Hond (WSAVA)", "Kat (WSAVA)"], [
                ["1–3: te dun", "Ribben, wervels en bekken goed zichtbaar of makkelijk voelbaar; geen voelbaar vet", "Ribben zichtbaar of makkelijk voelbaar; weinig tot geen vet"],
                ["4", "Ideaal: ribben makkelijk voelbaar met weinig vet; duidelijke taille", "Net te dun: ribben voelbaar met weinig vet; buikvet afwezig"],
                ["5", "Ideaal: ribben voelbaar zonder overtollig vet; taille van bovenaf, buik opgetrokken", "Ideaal: goed geproportioneerd, taille achter de ribben, weinig buikvet"],
                ["6", "Te zwaar: ribben voelbaar met wat extra vet; taille nog te zien", "Te zwaar: ribben voelbaar met wat extra vet; geen opgetrokken buik"],
                ["7–9", "Ribben moeilijk of niet voelbaar; geen taille; vet op rug en staartbasis", "Ribben moeilijk of niet voelbaar; ronde buik; geen taille"],
            ]),
            "sections": [
                ("Waarom niet alleen de weegschaal?", [
                    "Twee honden van hetzelfde gewicht kunnen er heel anders uitzien: de één is slank en gespierd, de ander heeft te veel vet. Daarom gebruiken dierenartsen naast het gewicht een Body Condition Score. De WSAVA heeft daarvoor een schaal van 1 tot 9 gemaakt, voor honden en voor katten apart.",
                    "Voor honden is een score van 4 of 5 ideaal. Voor katten is alleen 5 ideaal; een kat met score 4 zit volgens de WSAVA al net onder het ideaal.",
                ]),
                ("Zo check je je hond", [
                    "Voel met je handen langs de zijkant van de borst. Bij een ideale hond (score 5) voel je de ribben zonder overtollig vet erover. Kijk van bovenaf: je ziet een taille achter de ribben. Kijk van opzij: de buik is opgetrokken.",
                    "Bij score 6 voel je de ribben nog wel, maar met wat extra vet, en is de taille minder duidelijk. Bij score 7 voel je de ribben moeilijk, zit er duidelijk vet op de onderrug en bij de staartbasis, en is de taille weg of nauwelijks te zien. Bij score 3 of lager voel of zie je de ribben juist heel makkelijk, zonder vet.",
                ]),
                ("Zo check je je kat", [
                    "Een ideale kat (score 5) is goed geproportioneerd: je ziet een taille achter de ribben, je voelt de ribben onder een dun laagje vet en er is weinig buikvet. Bij score 6 zit er wat extra vet over de ribben en is de buik niet meer opgetrokken. Bij score 7 voel je de ribben niet makkelijk meer, is de taille nauwelijks te zien en is de buik duidelijk rond.",
                    "Katten met een lange vacht zijn lastiger te beoordelen op het oog. Voelen zegt dan meer dan kijken.",
                ]),
                ("Bijhouden: een lijn zegt meer dan één getal", [
                    "Eén weging of één score zegt weinig. Pas als je over een langere periode ziet hoe gewicht en conditie veranderen, wordt duidelijk of er iets aan de hand is. Weeg op een vast moment, bijvoorbeeld voor het eten, zodat de getallen goed te vergelijken zijn. Schrijf de score die je dierenarts geeft erbij.",
                    "Twijfel je of je dier een gezond gewicht heeft, of blijft het afvallen of aankomen zonder duidelijke reden? Vraag je dierenarts om de conditie te beoordelen. Die kan ook vertellen wat een goed streefgewicht is voor jouw dier.",
                ]),
            ],
            "faq": [
                ("Wat is een gezond gewicht voor mijn hond?", "Dat verschilt per hond. Kijk daarom ook naar de Body Condition Score: op de schaal van de WSAVA is 4 of 5 ideaal voor een hond. Je dierenarts kan een streefgewicht geven."),
                ("Hoe weet ik of mijn kat te dik is?", "Bij een ideale kat (score 5) zie je een taille achter de ribben en voel je de ribben onder een dun laagje vet. Voel je de ribben moeilijk en is de buik rond, dan zit je kat boven het ideaal."),
                ("Wat betekent een Body Condition Score van 7?", "Op de 9-puntsschaal van de WSAVA zit 7 duidelijk boven het ideaal: de ribben zijn moeilijk voelbaar, er zit vet op de rug en de taille is weg of nauwelijks te zien."),
                ("Hoe vaak moet ik mijn huisdier wegen?", "Daar is geen vaste regel voor. Weeg regelmatig op een vast moment, zodat je veranderingen ziet, en vraag je dierenarts hoe vaak het voor jouw dier zinvol is."),
                ("Wanneer moet ik met gewicht naar de dierenarts?", "Als je twijfelt over de conditie, of als je dier blijft afvallen of aankomen zonder duidelijke reden. Neem je metingen mee: een lijn zegt meer dan één getal."),
            ],
            "app": "In Kwispelboek voeg je met één tik een weging toe, in kilo’s of in grammen. Je ziet het verloop in een grafiek, en Kwispel geeft een seintje als het gewicht opvallend verandert.",
        },
        "en": {
            "slug": "dog-cat-healthy-weight",
            "title": "Is your dog or cat a healthy weight? How to check | Wagbook",
            "h1": "Is your dog or cat a healthy weight? Here’s how to check",
            "short": "Healthy weight",
            "desc": "With the WSAVA Body Condition Score you can see whether your dog or cat is too thin, ideal or overweight. Each score explained, with a table and tracking tips.",
            "intro": "Vets don’t just look at the scale, but also at body condition: the Body Condition Score (BCS). The global veterinary association WSAVA uses a scale from 1 to 9. A dog is ideal at 4 or 5, a cat at 5. At an ideal score you can feel the ribs without too much fat over them, and from above you see a waist behind the ribs.",
            "table": (["Score", "Dog (WSAVA)", "Cat (WSAVA)"], [
                ["1–3: too thin", "Ribs, spine and pelvis clearly visible or easy to feel; no palpable fat", "Ribs visible or easy to feel; little to no fat"],
                ["4", "Ideal: ribs easy to feel with little fat; clear waist", "Just under ideal: ribs palpable with minimal fat; no belly fat pad"],
                ["5", "Ideal: ribs palpable without excess fat; waist from above, tucked-up belly", "Ideal: well-proportioned, waist behind the ribs, little belly fat"],
                ["6", "Overweight: ribs palpable with slight excess fat; waist still visible", "Overweight: ribs palpable with slight excess fat; no tucked-up belly"],
                ["7–9", "Ribs hard or impossible to feel; no waist; fat on back and tail base", "Ribs hard or impossible to feel; rounded belly; no waist"],
            ]),
            "sections": [
                ("Why not just the scale?", [
                    "Two dogs of the same weight can look very different: one is lean and muscular, the other carries too much fat. That’s why vets use a Body Condition Score alongside weight. WSAVA made a scale from 1 to 9 for this, separately for dogs and cats.",
                    "For dogs a score of 4 or 5 is ideal. For cats only 5 is ideal; according to WSAVA a cat with a score of 4 is already just under ideal.",
                ]),
                ("How to check your dog", [
                    "Run your hands along the side of the chest. In an ideal dog (score 5) you feel the ribs without excess fat over them. Look from above: you see a waist behind the ribs. Look from the side: the belly is tucked up.",
                    "At score 6 you can still feel the ribs, but with some extra fat, and the waist is less obvious. At score 7 the ribs are hard to feel, there is clear fat on the lower back and tail base, and the waist is gone or barely visible. At score 3 or lower you feel or see the ribs very easily, without fat.",
                ]),
                ("How to check your cat", [
                    "An ideal cat (score 5) is well-proportioned: you see a waist behind the ribs, you feel the ribs under a thin layer of fat and there is little belly fat. At score 6 there is some extra fat over the ribs and the belly is no longer tucked up. At score 7 the ribs are no longer easy to feel, the waist is barely visible and the belly is clearly rounded.",
                    "Long-haired cats are harder to judge by eye. Feeling tells you more than looking.",
                ]),
                ("Tracking: a line says more than one number", [
                    "One weighing or one score says little. Only when you see how weight and condition change over a longer period does it become clear whether something is going on. Weigh at a fixed moment, for example before a meal, so the numbers compare well. Note the score your vet gives too.",
                    "Unsure whether your pet is a healthy weight, or does it keep losing or gaining weight without a clear reason? Ask your vet to assess its condition. Your vet can also tell you a good target weight for your pet.",
                ]),
            ],
            "faq": [
                ("What is a healthy weight for my dog?", "It differs per dog. So also look at the Body Condition Score: on the WSAVA scale, 4 or 5 is ideal for a dog. Your vet can give a target weight."),
                ("How do I know if my cat is overweight?", "In an ideal cat (score 5) you see a waist behind the ribs and feel the ribs under a thin layer of fat. If the ribs are hard to feel and the belly is round, your cat is above ideal."),
                ("What does a Body Condition Score of 7 mean?", "On the WSAVA 9-point scale, 7 is clearly above ideal: the ribs are hard to feel, there is fat on the back and the waist is gone or barely visible."),
                ("How often should I weigh my pet?", "There is no fixed rule. Weigh regularly at a fixed moment so you see changes, and ask your vet how often makes sense for your pet."),
                ("When should I see the vet about weight?", "If you are unsure about its condition, or if your pet keeps losing or gaining weight without a clear reason. Bring your measurements: a line says more than one number."),
            ],
            "app": "In Wagbook you add a weighing in one tap, in kilos or grams. You see the trend in a chart, and Kwispel gives you a heads-up when the weight changes noticeably.",
        },
    },
    # ------------------------------------------------------------------ toxic food
    {
        "key": "toxic", "emoji": "🍫", "sources": ["aspca_food", "knmvd_xyl", "fda_lily"],
        "related": {"nl": [(G + "vlooien-en-teken-hond-kat/", "Vlooien en teken: pas op met hondenmiddel bij katten"),
                           (G + "gezond-gewicht-hond-kat/", "Heeft je hond of kat een gezond gewicht?"),
                           ("/blog/winter-huisdier-strooizout-kerst/", "Winter: strooizout en kerstgevaren"),
                           ("/voor/konijn/", "Kwispelboek voor je konijn")],
                    "en": [(E + "fleas-and-ticks-dog-cat/", "Fleas and ticks: careful with dog products on cats"),
                           (E + "dog-cat-healthy-weight/", "Is your dog or cat a healthy weight?"),
                           ("/en/blog/winter-pets-road-salt-christmas/", "Winter: road salt and Christmas dangers"),
                           ("/en/for/rabbits/", "Wagbook for your rabbit")]},
        "nl": {
            "slug": "giftig-eten-hond-kat",
            "title": "Welk eten is giftig voor je hond of kat? | Kwispelboek",
            "h1": "Welk eten is giftig voor je hond of kat?",
            "short": "Giftig eten",
            "desc": "Chocolade, xylitol, druiven, ui, alcohol, avocado en lelies: wat is gevaarlijk voor je huisdier, waarom, en wat doe je als je dier ervan heeft gegeten?",
            "intro": "Sommig mensenvoer is gevaarlijk voor dieren. De bekendste zijn chocolade en koffie, de zoetstof xylitol, druiven en rozijnen, ui en knoflook, alcohol en macadamianoten. Avocado is vooral gevaarlijk voor vogels en konijnen, en lelies zijn zeer giftig voor katten. Heeft je dier iets gegeten? Onthoud wat en hoeveel, en bel meteen je dierenarts.",
            "table": (["Wat", "Waarom gevaarlijk", "Voor wie"], [
                ["Chocolade, koffie, cafeïne", "Methylxanthines: braken, diarree, hijgen, veel drinken en plassen", "Huisdieren"],
                ["Xylitol (zoetstof)", "Lage bloedsuiker en mogelijk leverschade; bij honden al vanaf 0,1 gram per kilo lichaamsgewicht flinke hypoglykemie", "Vooral honden"],
                ["Druiven en rozijnen", "Kunnen nierschade geven", "Honden"],
                ["Ui, knoflook, bieslook", "Maag-darmklachten en schade aan rode bloedcellen, met bloedarmoede", "Honden en katten"],
                ["Alcohol", "Braken, diarree, slecht coördineren, sufheid", "Huisdieren"],
                ["Avocado", "Schade aan hart en bloedvaten, soms dodelijk", "Vogels en konijnen"],
                ["Macadamianoten", "Zwakte, wankel lopen, braken, trillen, oververhitting", "Honden"],
                ["Rauw gistdeeg", "Rijst in de maag en geeft gasvorming", "Huisdieren"],
                ["Lelies", "Hele plant, ook stuifmeel en vaaswater: nierfalen", "Katten"],
            ]),
            "sections": [
                ("Chocolade en cafeïne", [
                    "Chocolade, koffie en andere producten met cafeïne bevatten methylxanthines. Volgens het gifinformatiecentrum van de ASPCA kunnen die bij huisdieren zorgen voor braken, diarree, hijgen, veel drinken en veel plassen. Hoe ernstig het is, hangt af van wat en hoeveel je dier heeft gegeten. Bel daarom altijd je dierenarts, ook als je denkt dat het om een klein stukje ging.",
                ]),
                ("Xylitol: klein beetje, grote gevolgen voor honden", [
                    "Xylitol is een zoetstof. De ASPCA waarschuwt dat het een lage bloedsuiker (hypoglykemie) kan geven en, afhankelijk van de hoeveelheid, leverschade. In tabellen van de KNMvD staat dat bij honden vanaf 0,1 gram xylitol per kilo lichaamsgewicht een flinke hypoglykemie kan ontstaan, en dat er bij hogere doses ook leverfunctiestoornissen bij kunnen komen. Voor een hond van 10 kilo gaat het dus al om 1 gram. Check daarom het etiket van suikervrije producten voordat je je hond iets geeft.",
                ]),
                ("Druiven, ui en andere keukenrisico’s", [
                    "Druiven en rozijnen kunnen bij honden nierschade geven. Ui, knoflook en bieslook kunnen maag-darmklachten en schade aan de rode bloedcellen veroorzaken, waardoor bloedarmoede ontstaat. Alcohol geeft braken, diarree, slecht coördineren en sufheid. Macadamianoten kunnen bij honden zorgen voor zwakte, wankel lopen, braken, trillen en oververhitting.",
                    "Ook minder bekende dingen kunnen problemen geven. Rauw gistdeeg rijst verder in de maag en geeft gasvorming. Botten kunnen het maag-darmkanaal beschadigen of verstoppen. Te veel zout geeft veel dorst en veel plassen. Melk en zuivel geven sommige dieren diarree. En rauw vlees en rauwe eieren kunnen bacteriën bevatten zoals Salmonella en E. coli, die zowel dieren als mensen ziek kunnen maken.",
                ]),
                ("Avocado voor vogels en konijnen", [
                    "Heb je een vogel of konijn? Volgens de ASPCA is avocado voor hen het gevaarlijkst: het kan schade aan hart en bloedvaten geven en zelfs dodelijk zijn. Geef ze dus geen stukjes avocado mee van je bord.",
                ]),
                ("Lelies: levensgevaarlijk voor katten", [
                    "De Amerikaanse FDA waarschuwt dat de hele lelieplant giftig is voor katten: stengel, bladeren, bloemen, stuifmeel en zelfs het water in de vaas. Een klein stukje blad, een paar stuifmeelkorrels die een kat uit zijn vacht likt, of een slokje vaaswater kan binnen 3 dagen leiden tot dodelijk nierfalen. Heb je een kat, zet dan geen lelies in huis, en ga meteen naar de dierenarts als je kat er toch aan heeft gezeten.",
                ]),
                ("Heeft je dier iets giftigs gegeten?", [
                    "Blijf rustig en onthoud wat je dier heeft gegeten en hoeveel, en wanneer. Neem de verpakking mee als je die hebt. Bel meteen je dierenarts, of buiten openingstijden de spoedkliniek. Wacht niet tot je dier klachten krijgt.",
                ]),
            ],
            "faq": [
                ("Hoeveel chocolade is gevaarlijk voor een hond?", "Dat hangt af van de soort chocolade, de hoeveelheid en het gewicht van je hond. Bel daarom altijd je dierenarts en vertel wat en hoeveel je hond heeft gegeten."),
                ("Waarom is xylitol zo gevaarlijk voor honden?", "Het kan bij honden een flinke daling van de bloedsuiker geven en bij hogere doses leverschade. Volgens tabellen van de KNMvD kan dat al vanaf 0,1 gram per kilo lichaamsgewicht."),
                ("Mag mijn hond een druif of rozijn?", "Nee. Druiven en rozijnen kunnen bij honden nierschade geven. Heeft je hond ze gegeten, bel dan je dierenarts."),
                ("Zijn lelies gevaarlijk voor katten?", "Ja, zeer. De hele plant is giftig, ook het stuifmeel en het vaaswater, en een kleine hoeveelheid kan binnen 3 dagen dodelijk nierfalen geven."),
                ("Mag mijn konijn of vogel avocado?", "Nee. Avocado is volgens de ASPCA vooral voor vogels en konijnen gevaarlijk, met schade aan hart en bloedvaten."),
                ("Wat doe ik als mijn dier iets giftigs heeft gegeten?", "Onthoud wat, hoeveel en wanneer, neem de verpakking mee en bel meteen je dierenarts of de spoedkliniek. Wacht niet op klachten."),
            ],
            "app": "In Kwispelboek staat bij Eerste hulp per diersoort wat giftig is, met één tik om je dierenarts of de spoedkliniek te bellen.",
        },
        "en": {
            "slug": "toxic-foods-dogs-cats",
            "title": "Which foods are toxic to dogs and cats? | Wagbook",
            "h1": "Which foods are toxic to your dog or cat?",
            "short": "Toxic foods",
            "desc": "Chocolate, xylitol, grapes, onion, alcohol, avocado and lilies: what is dangerous for your pet, why, and what to do if your pet has eaten it.",
            "intro": "Some human food is dangerous for animals. The best known are chocolate and coffee, the sweetener xylitol, grapes and raisins, onion and garlic, alcohol and macadamia nuts. Avocado is especially dangerous for birds and rabbits, and lilies are highly toxic to cats. Has your pet eaten something? Note what and how much, and call your vet straight away.",
            "table": (["What", "Why it’s dangerous", "For whom"], [
                ["Chocolate, coffee, caffeine", "Methylxanthines: vomiting, diarrhoea, panting, drinking and urinating a lot", "Pets"],
                ["Xylitol (sweetener)", "Low blood sugar and possibly liver damage; in dogs significant hypoglycaemia from 0.1 gram per kilo body weight", "Especially dogs"],
                ["Grapes and raisins", "Can cause kidney damage", "Dogs"],
                ["Onion, garlic, chives", "Stomach upset and damage to red blood cells, with anaemia", "Dogs and cats"],
                ["Alcohol", "Vomiting, diarrhoea, poor coordination, depression", "Pets"],
                ["Avocado", "Damage to heart and blood vessels, sometimes fatal", "Birds and rabbits"],
                ["Macadamia nuts", "Weakness, wobbliness, vomiting, tremors, overheating", "Dogs"],
                ["Raw yeast dough", "Rises in the stomach and causes gas", "Pets"],
                ["Lilies", "Whole plant, including pollen and vase water: kidney failure", "Cats"],
            ]),
            "sections": [
                ("Chocolate and caffeine", [
                    "Chocolate, coffee and other products with caffeine contain methylxanthines. According to the ASPCA Animal Poison Control Center, these can cause vomiting, diarrhoea, panting, excessive thirst and urination in pets. How serious it is depends on what and how much your pet ate. So always call your vet, even if you think it was only a small piece.",
                ]),
                ("Xylitol: a small amount, big consequences for dogs", [
                    "Xylitol is a sweetener. The ASPCA warns that it can cause low blood sugar (hypoglycaemia) and, depending on the amount, liver damage. Tables from the Dutch veterinary association KNMvD state that in dogs, significant hypoglycaemia can occur from 0.1 gram of xylitol per kilo body weight, and that higher doses can also affect the liver. For a 10 kilo dog that is just 1 gram. So check the label of sugar-free products before giving your dog anything.",
                ]),
                ("Grapes, onion and other kitchen risks", [
                    "Grapes and raisins can cause kidney damage in dogs. Onion, garlic and chives can cause stomach upset and damage to red blood cells, leading to anaemia. Alcohol causes vomiting, diarrhoea, poor coordination and depression. Macadamia nuts can cause weakness, wobbliness, vomiting, tremors and overheating in dogs.",
                    "Less obvious things can cause problems too. Raw yeast dough keeps rising in the stomach and causes gas. Bones can injure or block the digestive tract. Too much salt causes excessive thirst and urination. Milk and dairy give some pets diarrhoea. And raw meat and raw eggs can contain bacteria such as Salmonella and E. coli, which can make both pets and people ill.",
                ]),
                ("Avocado for birds and rabbits", [
                    "Have a bird or rabbit? According to the ASPCA, avocado is most dangerous for them: it can damage the heart and blood vessels and can even be fatal. So don’t share bits of avocado from your plate.",
                ]),
                ("Lilies: life-threatening for cats", [
                    "The US FDA warns that the whole lily plant is toxic to cats: stem, leaves, flowers, pollen and even the water in the vase. A small piece of leaf, a few pollen grains licked off the fur, or a sip of vase water can lead to fatal kidney failure within 3 days. If you have a cat, keep lilies out of the house, and go to the vet straight away if your cat has been near them.",
                ]),
                ("Has your pet eaten something toxic?", [
                    "Stay calm and note what your pet ate, how much and when. Bring the packaging if you have it. Call your vet straight away, or the emergency clinic outside opening hours. Don’t wait for symptoms.",
                ]),
            ],
            "faq": [
                ("How much chocolate is dangerous for a dog?", "That depends on the type of chocolate, the amount and your dog’s weight. So always call your vet and say what and how much your dog ate."),
                ("Why is xylitol so dangerous for dogs?", "It can cause a sharp drop in blood sugar in dogs and, at higher doses, liver damage. According to KNMvD tables this can happen from 0.1 gram per kilo body weight."),
                ("Can my dog have a grape or raisin?", "No. Grapes and raisins can cause kidney damage in dogs. If your dog has eaten them, call your vet."),
                ("Are lilies dangerous for cats?", "Yes, very. The whole plant is toxic, including pollen and vase water, and a small amount can cause fatal kidney failure within 3 days."),
                ("Can my rabbit or bird eat avocado?", "No. According to the ASPCA, avocado is especially dangerous for birds and rabbits, damaging the heart and blood vessels."),
                ("What do I do if my pet ate something toxic?", "Note what, how much and when, bring the packaging and call your vet or emergency clinic straight away. Don’t wait for symptoms."),
            ],
            "app": "In Wagbook, First aid shows what is toxic per species, with one tap to call your vet or emergency clinic.",
        },
    },
    # ------------------------------------------------------------------ lost pet
    {
        "key": "lost", "emoji": "🔎", "sources": ["licg_lost", "licg_chip", "chip_dog", "chip_cat"],
        "related": {"nl": [("/blog/qr-code-halsband-hond-kat/", "QR-code op de halsband: sneller weer thuis"),
                           (G + "op-reis-met-huisdier-buitenland/", "Met je huisdier naar het buitenland"),
                           ("/checklists/puppy-in-huis/", "Checklist: puppy in huis"),
                           ("/voor/kat/", "Kwispelboek voor je kat")],
                    "en": [("/en/blog/qr-code-pet-collar-tag/", "A QR code on the collar: home again faster"),
                           (E + "travelling-abroad-with-pet/", "Travelling abroad with your pet"),
                           ("/en/checklists/new-puppy/", "Checklist: new puppy"),
                           ("/en/for/cats/", "Wagbook for your cat")]},
        "nl": {
            "slug": "huisdier-vermist-wat-te-doen",
            "title": "Huisdier vermist: wat moet je doen? | Kwispelboek",
            "h1": "Huisdier vermist: wat moet je doen?",
            "short": "Huisdier vermist",
            "desc": "Hond of kat kwijt? Waar je een vermist dier meldt, hoe je zoekt, waarom de chipregistratie moet kloppen en wat je doet als je een dier vindt.",
            "intro": "Is je hond of kat vermist? Meld het bij het asiel of de dierenopvang van je gemeente, en ook bij de dierenambulance, de politie en Amivedi. Is je dier gechipt en geregistreerd, meld het dan ook bij de databank waar de chip staat. Laat het je eigen dierenarts en dierenartsen in de buurt weten, zoek in de buurt en deel het online. Zo raadt het LICG het aan.",
            "table": (["Stap", "Wat je doet"], [
                ["Melden", "Bij het asiel of de dierenopvang van je gemeente; ook bij politie, dierenambulance en Amivedi"],
                ["Chip", "Meld het vermiste dier bij de databank (het portaal) waar de chip geregistreerd staat"],
                ["Dierenartsen", "Laat het je eigen dierenarts en praktijken in de buurt weten"],
                ["Zoeken", "Vraag buren in schuren en garages te kijken, hang flyers op"],
                ["Online", "Facebookpagina’s voor vermiste dieren, buurt-apps en groepen"],
                ["Vooraf", "Houd je contactgegevens in de chipregistratie actueel; controleer via chipnummer.nl"],
            ]),
            "sections": [
                ("Meteen melden", [
                    "Volgens het LICG meld je een vermist dier bij de burgemeester. In de praktijk is dat het asiel of de dierenopvang die je gemeente daarvoor heeft aangewezen. Je kunt ook de politie, de dierenambulance en Amivedi inlichten. Is je dier gechipt en geregistreerd, meld het dan ook via het portaal, de databank waar de chip staat.",
                    "Laat het daarnaast weten aan je eigen dierenarts en aan andere dierenartsen in de buurt. Wordt je dier gevonden en daar binnengebracht, dan weten ze meteen dat je het zoekt.",
                ]),
                ("Zelf zoeken en het nieuws verspreiden", [
                    "Zoek zelf in de buurt en vraag buurtbewoners om in hun schuur en garage te kijken; dieren kruipen graag weg of raken per ongeluk ingesloten. Hang flyers op met een duidelijke foto en je telefoonnummer.",
                    "Deel het ook online: op Facebookpagina’s voor vermiste dieren in je regio, in buurt-apps en in groepen. Hoe meer mensen weten dat je dier zoek is, hoe groter de kans dat iemand het herkent.",
                ]),
                ("Waarom de chip zo belangrijk is", [
                    "Een chip helpt alleen als hij op jouw naam geregistreerd staat en je gegevens kloppen. Voor honden zijn chippen en registreren verplicht: dat geldt voor honden die vanaf 1 april 2013 geboren of geïmporteerd zijn. Pups die vanaf 1 november 2021 in Nederland geboren zijn, moeten binnen 7 weken na de geboorte gechipt worden. Krijgt een hond een nieuwe eigenaar, dan moet die hem binnen 2 weken op zijn eigen naam registreren.",
                    "Voor katten is chippen nu nog niet verplicht, maar de overheid heeft besloten dat het wel verplicht gaat worden. Het ministerie werkt dat nog uit. Het LICG raadt registratie nu al aan.",
                    "Verandert je adres of telefoonnummer, geef het dan direct door aan het portaal. Via chipnummer.nl kun je met het chipnummer controleren of en waar je dier geregistreerd staat. Let op: een chipregistratie geldt niet als eigendomsbewijs.",
                ]),
                ("Een dier gevonden?", [
                    "Vind je zelf een dier, meld het dan ook bij het asiel of de dierenopvang van de gemeente. Laat een dierenarts of de dierenambulance controleren of het gechipt en geregistreerd is; is dat zo, dan ben je verplicht contact op te nemen met de eigenaar. Meld het gevonden dier ook bij Amivedi en kijk of iemand het mist.",
                ]),
                ("Weer thuis", [
                    "Is je dier terug? Laat het iedereen weten bij wie je het als vermist hebt gemeld, ook bij de databank van de chip, zodat het daar niet meer als vermist staat.",
                ]),
            ],
            "faq": [
                ("Waar meld ik mijn vermiste kat of hond?", "Bij het asiel of de dierenopvang van je gemeente. Je kunt ook de politie, de dierenambulance en Amivedi inlichten, en bij een gechipt dier de databank van de chip."),
                ("Is chippen verplicht voor katten?", "Nu nog niet. De overheid heeft besloten dat chippen en registreren voor katten verplicht wordt; het ministerie werkt dat nog uit. Registreren wordt nu al aangeraden."),
                ("Hoe controleer ik of de chip van mijn dier goed geregistreerd is?", "Vul het chipnummer in op chipnummer.nl. Die site zoekt in de aangesloten Nederlandse databanken."),
                ("Ik heb een hond gevonden. Wat nu?", "Meld het bij het asiel of de dierenopvang, laat een dierenarts of de dierenambulance de chip controleren en meld het bij Amivedi. Is het dier gechipt, dan moet je contact opnemen met de eigenaar."),
                ("Is de chip een bewijs dat het dier van mij is?", "Nee. Volgens het LICG geldt een chipregistratie, net als een paspoort, niet als eigendomsbewijs."),
            ],
            "app": "Met Kwispelboek maak je in een minuut een vermist-poster met foto en je telefoonnummer, en print je een QR-sticker voor de halsband, zodat een vinder je meteen kan bellen.",
        },
        "en": {
            "slug": "lost-pet-what-to-do",
            "title": "Lost pet: what should you do? | Wagbook",
            "h1": "Lost pet: what should you do?",
            "short": "Lost pet",
            "desc": "Dog or cat missing? Where to report it, how to search, why the microchip registration must be right and what to do if you find a pet. Based on Dutch advice.",
            "intro": "Is your dog or cat missing? Report it to the shelter or animal centre in your area, and also to the animal ambulance, the police and the lost-and-found pet register. If your pet is microchipped and registered, also report it to the database where the chip is registered. Tell your own vet and vets nearby, search the area and share it online. This guide follows the advice of the Dutch pet information centre LICG; outside the Netherlands the organisations differ, but the steps are much the same.",
            "table": (["Step", "What to do"], [
                ["Report", "To the shelter or animal centre for your area; also police, animal ambulance and the lost-pet register (Amivedi in the Netherlands)"],
                ["Microchip", "Report the missing pet to the database where the chip is registered"],
                ["Vets", "Tell your own vet and practices nearby"],
                ["Search", "Ask neighbours to check sheds and garages, put up flyers"],
                ["Online", "Lost-pet Facebook pages, neighbourhood apps and groups"],
                ["Beforehand", "Keep your contact details in the chip registration up to date"],
            ]),
            "sections": [
                ("Report it straight away", [
                    "In the Netherlands, according to the LICG, you report a missing pet to the municipality. In practice that is the shelter or animal centre your municipality has appointed. You can also inform the police, the animal ambulance and Amivedi, the Dutch lost-and-found pet register. If your pet is microchipped and registered, report it through the database where the chip is registered too.",
                    "Also let your own vet and other vets nearby know. If your pet is found and brought in there, they will know straight away that you are looking for it.",
                ]),
                ("Search and spread the word", [
                    "Search the area yourself and ask neighbours to check their sheds and garages; pets like to hide or get shut in by accident. Put up flyers with a clear photo and your phone number.",
                    "Share it online too: on lost-pet Facebook pages for your region, in neighbourhood apps and in groups. The more people know your pet is missing, the bigger the chance someone recognises it.",
                ]),
                ("Why the microchip matters so much", [
                    "A microchip only helps if it is registered in your name and your details are correct. In the Netherlands, microchipping and registering is mandatory for dogs born or imported from 1 April 2013. Puppies born in the Netherlands from 1 November 2021 must be chipped within 7 weeks of birth, and a new owner must register the dog in their own name within 2 weeks.",
                    "For cats in the Netherlands, microchipping is not yet mandatory, but the government has decided it will be. The ministry is still working out the details. The LICG already recommends registration.",
                    "If your address or phone number changes, pass it on to the database straight away. In the Netherlands you can check whether and where your pet is registered at chipnummer.nl. Note: a chip registration is not proof of ownership.",
                ]),
                ("Found a pet?", [
                    "If you find a pet yourself, report it to the shelter or animal centre too. Have a vet or the animal ambulance check whether it is microchipped and registered; if it is, you must contact the owner. In the Netherlands, also report the found pet to Amivedi and check whether someone is missing it.",
                ]),
                ("Back home", [
                    "Is your pet back? Let everyone you reported it to know, including the chip database, so it is no longer listed as missing.",
                ]),
            ],
            "faq": [
                ("Where do I report my missing cat or dog?", "To the shelter or animal centre for your area. You can also inform the police and the animal ambulance, and, for a chipped pet, the chip database. In the Netherlands, also report it to Amivedi."),
                ("Is microchipping mandatory for cats?", "In the Netherlands not yet. The government has decided that microchipping and registering cats will become mandatory; the ministry is still working it out. Registration is already recommended."),
                ("How do I check my pet’s microchip registration?", "In the Netherlands, enter the chip number at chipnummer.nl. It searches the connected Dutch databases."),
                ("I found a dog. What now?", "Report it to the shelter or animal centre, have a vet or the animal ambulance check the chip, and report it to the lost-pet register. If the pet is chipped, you must contact the owner."),
                ("Is the microchip proof that the pet is mine?", "No. According to the LICG, a chip registration, like a passport, is not proof of ownership."),
            ],
            "app": "With Wagbook you make a missing poster with photo and your phone number in a minute, and print a QR sticker for the collar so a finder can call you straight away.",
        },
    },
]
