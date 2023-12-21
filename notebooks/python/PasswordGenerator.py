import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_special_chars=True):
    # Definiere die Zeichen, die für das Passwort verwendet werden sollen
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Überprüfe, ob die Auswahl gültig ist
    if not chars:
        print("Ungültige Auswahl. Bitte wähle mindestens eine Art von Zeichen.")
        return None

    # Begrenze die Länge des Passworts zwischen 4 und 16 Zeichen
    length = max(4, min(16, length))

    # Generiere das Passwort
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Beispielaufruf des Generators
length = int(input("Gib die gewünschte Passwortlänge ein (mindestens 4, maximal 16): "))
use_letters = input("Sollen Buchstaben verwendet werden? (Ja/Nein): ").lower() == 'ja'
use_numbers = input("Sollen Zahlen verwendet werden? (Ja/Nein): ").lower() == 'ja'
use_special_chars = input("Sollen Sonderzeichen verwendet werden? (Ja/Nein): ").lower() == 'ja'

password = generate_password(length, use_letters, use_numbers, use_special_chars)

if password:
    print("Generiertes Passwort:", password)