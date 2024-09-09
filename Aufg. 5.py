# Verschlüsseln
verschluesselter_text = verschluesselung("HELLO WORLD", 3)
print(verschluesselter_text)  # Erwartet: "KHOOR ZRUOG"

# Entschlüsseln mit dem negativen Schlüssel
entschluesselter_text = verschluesselung(verschluesselter_text, -3)
print(entschluesselter_text)  # Erwartet: "HELLO WORLD"

# Weitere Beispiele
verschluesselter_text = verschluesselung("PYTHON", 7)
print(verschluesselter_text)  # Erwartet: "WFAOVU"

entschluesselter_text = verschluesselung(verschluesselter_text, -7)
print(entschluesselter_text)  # Erwartet: "PYTHON"

# Funktion zur Entschlüsselung eines Textes
def entschluesselung(text, schluessel):
    return verschluesselung(text, -schluessel)

# Funktionsaufrufe zum Testen
verschluesselter_text = verschluesselung("HELLO WORLD", 3)
print(verschluesselter_text)  # Erwartet: "KHOOR ZRUOG"

entschluesselter_text = entschluesselung(verschluesselter_text, 3)
print(entschluesselter_text)  # Erwartet: "HELLO WORLD"

# Weitere Beispiele
verschluesselter_text = verschluesselung("PYTHON", 7)
print(verschluesselter_text)  # Erwartet: "WFAOVU"

entschluesselter_text = entschluesselung(verschluesselter_text, 7)
print(entschluesselter_text)  # Erwartet: "PYTHON"
