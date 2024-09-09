# Funktion zur Verschiebung eines einzelnen Zeichens
def verschiebung(zeichen, schluessel):
    # Berechne die Position des Zeichens relativ zu 'A'
    zahl = ord(zeichen)
    neueZahl = (zahl - ord('A') + schluessel) % 26 + ord('A')
    # Wandle die neue Zahl zurück in ein Zeichen
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

# Funktion zur Verschlüsselung eines gesamten Textes
def verschluesselung(text, schluessel):
    verschluesselter_text = ""
    for zeichen in text:
        if zeichen.isalpha() and zeichen.isupper():  # Nur Großbuchstaben verschlüsseln
            neuesZeichen = verschiebung(zeichen, schluessel)
            verschluesselter_text += neuesZeichen
        else:
            verschluesselter_text += zeichen  # Nicht-Buchstaben oder Kleinbuchstaben unverändert lassen
    return verschluesselter_text

# Funktionsaufrufe zum Testen
print(verschluesselung("HELLO WORLD", 3))  # Erwartet: "KHOOR ZRUOG"
print(verschluesselung("PYTHON", 7))       # Erwartet: "WFAOVU"
print(verschluesselung("CRYPTOGRAPHY", 10)) # Erwartet: "MZIZDYQBKRI"
print(verschluesselung("ZEBRA", 1))        # Test mit Z, Erwartet: "AFCSB"
print(verschluesselung("HELLO, CHATGPT!", 4)) # Test mit Sonderzeichen, Erwartet: "LIPPS, GLEXKTX!"
