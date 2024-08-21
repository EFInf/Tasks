def binaere_suche(liste, ziel):
    links = 0
    rechts = len(liste) - 1

    while links <= rechts:
        # Bestimme die Mitte der Liste (oder Teilliste)
        mitte = (links + rechts) // 2

        if liste[mitte] == ziel:
            return mitte

        elif liste[mitte] > ziel:
            rechts = mitte - 1  # Suche im linken Teil der Liste fortsetzen

        else:
            links = mitte + 1  # Suche im rechten Teil der Liste fortsetzen

    return -1  # Ziel nicht gefunden, Rückgabe von -1

sortierte_liste = [1, 3, 5, 7, 9, 11, 13, 15]
zielwert = 7

ergebnis = binaere_suche(sortierte_liste, zielwert)
if ergebnis != -1:
    print(f"Zielwert {zielwert} gefunden an Index {ergebnis}")
else:
    print(f"Zielwert {zielwert} nicht gefunden")
