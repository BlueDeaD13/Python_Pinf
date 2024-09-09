def verschiebung(zeichen, schluessel):
    # Berechne die Position des Zeichens relativ zu 'A'
    zahl = ord(zeichen)
    neueZahl = (zahl - ord('A') + schluessel) % 26 + ord('A')
    # Wandle die neue Zahl zurück in ein Zeichen
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

# Funktionsaufrufe zum Testen
print(verschiebung('P', 7))  # Erwartet: 'W'
print(verschiebung('A', 3))  # Erwartet: 'D'
print(verschiebung('T', 10)) # Erwartet: 'D'
print(verschiebung('Z', 1))  # Test mit Z, Erwartet: 'A'
print(verschiebung('B', 25)) # Test mit großem Schlüssel, Erwartet: 'A'
