import random
import os

def print_vakje(tekst):
    """Print de tekst in een mooi vakje."""
    lengte = len(tekst) + 4
    print("+" + "-" * (lengte - 2) + "+")
    print(f"|  {tekst}  |")
    print("+" + "-" * (lengte - 2) + "+")

def raadspel():
    print_vakje("🚀 Welkom bij het Ruimte Raadspel! ⭐️")
    max_number = 20  # Maximale waarde van het getal
    max_guesses = 5  # Aantal pogingen
    number = random.randint(1, max_number)  # Genereer een willekeurig nummer

    print_vakje(f"Ik heb een magisch getal gekozen tussen 1 en {max_number}. 🌌")
    print_vakje(f"Je hebt {max_guesses} kansen om het te raden! 🌟")

    for attempt in range(1, max_guesses + 1):
        print(f"""\
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ ✨ Poging {attempt}: Wat is je gok? 💭     ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        guess = int(input("Voer je gok in: "))

        if guess < number:
            remaining_attempts = max_guesses - attempt
            print_vakje(f"Oh nee, dat is te laag! 📉 Je hebt nog {remaining_attempts} pogingen over. ⭐️")
        elif guess > number:
            remaining_attempts = max_guesses - attempt
            print_vakje(f"Oeps, dat is te hoog! 📈 Je hebt nog {remaining_attempts} pogingen over. ✨")
        else:
            print_vakje(f"🎉 Gefeliciteerd! Je hebt het magische getal {number} geraden in {attempt} pogingen! 🌟🚀")
            break
    else:
        print_vakje(f"Jammer! Het getal was {number}. Probeer het volgende keer opnieuw! 💔")

def galgje():
    bestandsnaam = 'woordenlijst.txt'

    if not os.path.exists(bestandsnaam):
        with open(bestandsnaam, 'w') as bestand:
            bestand.write("# makkelijk\n")
            bestand.write("planeet\nmaan\nster\nzon\n")
            bestand.write("\n# gemiddeld\n")
            bestand.write("sterrenstelsel\nkometen\nmeteoor\nruimtestation\n")
            bestand.write("\n# moeilijk\n")
            bestand.write("zonnestelsel\nastronaut\nsatelliet\nzwaartekracht\n")
        print_vakje(f"Het bestand '{bestandsnaam}' is aangemaakt met een standaard woordenlijst. 🌌")

    ruimte_stadia = [
        "🚀🌍🌑🌑🌑🌑🌑   - De raket staat klaar op de lanceerbasis.",
        "🚀🌕🌑🌑🌑🌑🌑   - De raket stijgt op! 🚀",
        "🚀🌕🌕🌑🌑🌑🌑   - De raket gaat richting de sterren! ✨",
        "🚀🌕🌕🌕🌑🌑🌑   - Halverwege naar de ruimte! 🌌",
        "🚀🌕🌕🌕🌕🌑🌑   - Bijna in de ruimte... 🌠",
        "🚀🌕🌕🌕🌕🌕🌑   - De raket heeft de ruimte bereikt! 🌍✨",
        "💥💥💥💥💥💥     - O nee! De raket is geëxplodeerd in de ruimte! 😢"
    ]

    woorden = {'makkelijk': [], 'gemiddeld': [], 'moeilijk': []}
    huidige_categorie = None

    with open(bestandsnaam, 'r') as bestand:
        for lijn in bestand:
            lijn = lijn.strip()
            if lijn.startswith('# makkelijk'):
                huidige_categorie = 'makkelijk'
            elif lijn.startswith('# gemiddeld'):
                huidige_categorie = 'gemiddeld'
            elif lijn.startswith('# moeilijk'):
                huidige_categorie = 'moeilijk'
            elif lijn and huidige_categorie:
                woorden[huidige_categorie].append(lijn)

    print_vakje("🌌 Welkom bij Galgje: Ruimte Editie! 🚀")
    naam = input("Wat is je naam, astronaut? 👨‍🚀 ")

    moeilijkheid = ""
    while moeilijkheid not in ['makkelijk', 'gemiddeld', 'moeilijk']:
        print("""\
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Kies een moeilijkheidsgraad:               ┃
        ┃ 1. Makkelijk 🪐                            ┃
        ┃ 2. Gemiddeld 🚀                           ┃
        ┃ 3. Moeilijk 🌌                            ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        moeilijkheid = input("Kies je moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()

    woord = random.choice(woorden[moeilijkheid])

    goed_geraden = set()
    fout_geraden = set()
    pogingen = 6

    while pogingen > 0:
        print("\n" + ruimte_stadia[6 - pogingen])
        woord_weergave = ' '.join([letter if letter in goed_geraden else '_' for letter in woord])
        print_vakje(f"Woord: {woord_weergave}")

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha():
            print_vakje("🚫 Ongeldige invoer, probeer opnieuw.")
            continue

        if gok in goed_geraden or gok in fout_geraden:
            print_vakje(f"🔄 Je hebt '{gok}' al geraden. Probeer een andere letter.")
            continue

        if gok in woord:
            goed_geraden.add(gok)
            print_vakje(f"🎉 Goed zo! '{gok}' zit in het woord. 🌟")
        else:
            fout_geraden.add(gok)
            pogingen -= 1
            print_vakje(f"❌ Helaas, '{gok}' zit niet in het woord. Je hebt nog {pogingen} pogingen over. 🌑")

        if all(letter in goed_geraden for letter in woord):
            print_vakje(f"🎊 Gefeliciteerd, {naam}! Je hebt het woord '{woord}' geraden! 🌟🚀")
            break
    else:
        print(ruimte_stadia[6])
        print_vakje(f"Helaas, je hebt geen pogingen meer. Het woord was '{woord}'. 😢")

    print_vakje("Bedankt voor het spelen! Tot de volgende keer! 🌌")

def hoofdmenu():
    print("""\
    ┏━━━━━━━━━━━━━━━━━━━━━✦✧✦━━━━━━━━━━━━━━━━━━━━━┓
             🌟 Hoofdmenu 🌌
    ┗━━━━━━━━━━━━━━━━━━━━━✦✧✦━━━━━━━━━━━━━━━━━━━━━┛
    
    Kies een spel:
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ 1. Raadspel 🌠                             ┃
    ┃ 2. Galgje: Ruimte Editie 🚀                ┃
    ┃ 3. Stoppen 🛑                              ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)

    keuze = input("Maak je keuze (1-3): ")
    return keuze

while True:
    keuze = hoofdmenu()
    if keuze == '1':
        print_vakje("🌟 Start Raadspel! 🚀")
        raadspel()
    elif keuze == '2':
        print_vakje("🌟 Start Galgje: Ruimte Editie! 🚀")
        galgje()
    elif keuze == '3':
        print_vakje("Bedankt voor het spelen! Tot de volgende keer! 🌟")
        break
    else:
        print_vakje("🚫 Ongeldige keuze, probeer het opnieuw.")

























