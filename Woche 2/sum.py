# Teilmenge-Summenproblem

def teil_menge_summe(s,A):
    # b speichert, ob eine Zahl erzeugt konnte
    b = [False]*(s+1)
    b[0] = True # Null kann immer erzeugt werden

    for i in A:
        for j in reversed(range(s+1)):
            if b[j] and j+i<=s:
                b[j+i] = True
    return b[s]

A = [3, 24, 4, 12, 5, 2]
print(teil_menge_summe(9,A)) # bestimmt, ob die Zahl 9 erzeugt werden kann

