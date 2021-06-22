def es20(stringa1):
    """
    Es 3: 4 punti
    Si consideri l'ordine alfabetico delle 21 lettere dell'alfabeto italiano:
    A – B – C – D – E – F – G – H – I – L – M – N – O – P – Q – R – S – T – U – V – Z
    definiamo valore di una lettera la posizione che occupa in quest'ordine a partire da 1
    (ad esempio il valore di A e' 1 mentre il valore di Z e' 21).
    La funzione  es3(stringa1) presa la stringa stringa1
    contenente parole sull'alfabeto italiano separate da uno spazio, restituisce la stringa
    che si ottine sostituendo a ciasuna parola presente in  stringa1
    la stringa numerica che si ottiene sommando  il valore delle lettere che compongono la parola.
    Non si distingue tra lettere maiuscole e minuscole).
    Ad esempio con stringa1='Angelo Monti Andrea Sterbini e Angelo Spognardi' la funzione restituira'
    la stringa '48 63 39 88 5 48 93'
    """
    diz = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "l": 10,
        "m": 11,
        "n": 12,
        "o": 13,
        "p": 14,
        "q": 15,
        "r": 16,
        "s": 17,
        "t": 18,
        "u": 19,
        "v": 20,
        "z": 21,
    }
    words = stringa1.split()
    result = ""
    for word in words:
        summ = 0
        for char in word:
            summ = summ + diz[char.lower()]
        result += str(summ) + " "
    result = result[:-1]
    return result
