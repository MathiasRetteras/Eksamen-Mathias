import json

# Gitt datastrukturer
varer = [['jakke', 609], ['bukse', 342], ['caps', 159], ['sokker', 45], ['truse', 101], ['ulltrøye', 200], ['hansker', 300]]
beholdning = {'jakke': 600, 'bukse': 500, 'caps': 1000, 'sokker': 2000, 'truse': 2500, 'ulltrøye': 0, 'hansker': 1}

# Funksjon for å finne prisen på en vare
def finn_pris(varer, let_etter):
    for vare in varer:
        if vare[0] == let_etter:
            return vare[1]
    return 0

# Funksjon for å oppdatere beholdningen av en vare
def oppdater_beholdning(beholdning, endringer):
    for endring in endringer:
        varenavn, antall = endring
        if varenavn in beholdning:
            beholdning[varenavn] += antall
    return beholdning

# Funksjon for å lagre beholdningen til en fil
def skriv_beholdning(beholdning, filnavn="beholdning.json"):
    with open(filnavn, 'w') as fil:
        json.dump(beholdning, fil)
    print(f"Beholdning lagret til {filnavn}")

# Funksjon for å lese beholdningen fra en fil
def les_beholdning(filnavn="beholdning.json"):
    try:
        with open(filnavn, 'r') as fil:
            beholdning = json.load(fil)
        print(f"Beholdning lest fra {filnavn}")
        return beholdning
    except FileNotFoundError:
        print(f"Filen {filnavn} ble ikke funnet")
        return {}

# Funksjon for å vise alle varer og deres priser
def vis_priser(varer):
    for vare in varer:
        print(f"Vare: {vare[0]}, Pris: {vare[1]}")

# Funksjon for å håndtere salg av en vare
def salg(beholdning, varenavn, antall):
    if varenavn in beholdning and beholdning[varenavn] >= antall:
        beholdning[varenavn] -= antall
        print(f"Solgte {antall} stk av {varenavn}")
        return True
    else:
        print(f"Ikke nok beholdning for {varenavn}")
        return False

# Funksjon for å legge til en ny vare
def legg_til_vare(varer, beholdning, varenavn, pris, antall):
    varer.append([varenavn, pris])
    beholdning[varenavn] = antall
    print(f"La til vare: {varenavn} med pris {pris} og antall {antall}")

# Meny for brukeren
def meny():
    global beholdning
    beholdning = les_beholdning()  # Les data fra fil ved oppstart
    while True:
        print("\n1. Kjøp vare")
        print("2. Oppdater pris på vare")
        print("3. Oppdater beholdning av vare")
        print("4. Vis priser")
        print("5. Legg til ny vare")
        print("6. Vis produkter")
        print("7. Lagre og avslutt")
        
        valg = input("Velg en handling (1-7): ")
        
        if valg == "1":
            varenavn = input("Skriv inn varenavn: ")
            antall = int(input("Skriv inn antall: "))
            salg(beholdning, varenavn, antall)
        
        elif valg == "2":
            varenavn = input("Skriv inn varenavn: ")
            ny_pris = int(input("Skriv inn ny pris: "))
            beholdning = oppdater_beholdning(beholdning, [[varenavn, ny_pris]])
            print(f"Oppdaterte prisen på {varenavn} til {ny_pris}")
        
        elif valg == "3":
            varenavn = input("Skriv inn varenavn: ")
            nytt_antall = int(input("Skriv inn nytt antall: "))
            beholdning = oppdater_beholdning(beholdning, [[varenavn, nytt_antall]])
            print(f"Oppdaterte beholdningen av {varenavn} til {beholdning[varenavn]}")
        
        elif valg == "4":
            vis_priser(varer)
        
        elif valg == "5":
            varenavn = input("Skriv inn navn på ny vare: ")
            pris = int(input("Skriv inn pris på ny vare: "))
            antall = int(input("Skriv inn antall på ny vare: "))
            legg_til_vare(varer, beholdning, varenavn, pris, antall)

        elif valg == "6":
            print("Vis produkter.")
            for vare in varer:
                print(f"Vare: {vare[0]}, Pris: {vare[1]}")

        elif valg == "7":
            skriv_beholdning(beholdning)  # Lagre data til fil før avslutning
            print("Avslutter programmet.")
            break
        
        else:
            print("Ugyldig valg, prøv igjen.")

# Eksempel på bruk av menyen
meny()
