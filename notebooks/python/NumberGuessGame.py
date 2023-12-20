import random

def zahlen_ratespiel():
    # Zufallszahl zwischen 1 und 100 wählen
    zielzahl = random.randint(1, 100)
    
    # Spieler hat maximal 10 Versuche
    versuche = 0
    
    while versuche < 10:
        try:
            # Spieler gibt einen Rateversuch ein
            ratezahl = int(input("Rate eine Zahl zwischen 1 und 100: "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue
        
        # Überprüfen, ob die geratene Zahl korrekt ist
        if ratezahl == zielzahl:
            print("Herzlichen Glückwunsch! Du hast die Zahl richtig geraten.")
            break
        elif ratezahl < zielzahl:
            print("Die gesuchte Zahl ist höher.")
        else:
            print("Die gesuchte Zahl ist niedriger.")
        
        # Versuchszähler erhöhen
        versuche += 1
    
    if versuche == 10:
        print(f"Leider hast du die Zahl nicht in 10 Versuchen erraten. Die gesuchte Zahl war {zielzahl}.")
    
    # Spiel neu starten
    neu_starten = input("Möchtest du das Spiel neu starten? (Ja/Nein): ")
    if neu_starten.lower() == 'ja':
        zahlen_ratespiel()
    else:
        print("Vielen Dank fürs Spielen!")

# Spiel starten
zahlen_ratespiel()
