zeichen = 'T'
schluessel = 10

zahl = ord(zeichen)  # 84 für 'T'
neueZahl = (zahl - ord('A') + schluessel) % 26 + ord('A')
neuesZeichen = chr(neueZahl)

print(neuesZeichen)  # Ausgabe: 'D'
