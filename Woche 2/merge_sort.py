def merge_sort(liste):
    # Basisfall: Wenn die Liste nur ein Element hat, ist sie bereits sortiert
    if len(liste) <= 1:
        return liste

    # Bestimme die Mitte der Liste
    mitte = len(liste) // 2

    # Teile die Liste in zwei Hälften
    linke_haelfte = merge_sort(liste[:mitte])
    rechte_haelfte = merge_sort(liste[mitte:])

    # Führe die sortierten Hälften zusammen
    return merge(linke_haelfte, rechte_haelfte)

def merge(linke_haelfte, rechte_haelfte):
    sortierte_liste = []
    i = 0  # Index für die linke Hälfte
    j = 0  # Index für die rechte Hälfte

    # Solange es Elemente in beiden Hälften gibt
    while i < len(linke_haelfte) and j < len(rechte_haelfte):
        # Füge das kleinere Element zur sortierten Liste hinzu
        if linke_haelfte[i] < rechte_haelfte[j]:
            sortierte_liste.append(linke_haelfte[i])
            i += 1
        else:
            sortierte_liste.append(rechte_haelfte[j])
            j += 1

    # Füge verbleibende Elemente aus der linken Hälfte hinzu (falls vorhanden)
    while i < len(linke_haelfte):
        sortierte_liste.append(linke_haelfte[i])
        i += 1

    # Füge verbleibende Elemente aus der rechten Hälfte hinzu (falls vorhanden)
    while j < len(rechte_haelfte):
        sortierte_liste.append(rechte_haelfte[j])
        j += 1

    return sortierte_liste

# Beispielhafte Verwendung der Funktion
unsortierte_liste = [38, 27, 43, 3, 9, 82, 10]
sortierte_liste = merge_sort(unsortierte_liste)
print("Sortierte Liste:", sortierte_liste)
