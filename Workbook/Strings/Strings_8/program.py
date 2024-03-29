def es63(fileParole, fileTerne):
    """
    Definite la funzione es63(fileParole,fileTerne) che prende in input:
    - il path FileParole ad un file di testo contenente parole, una parola per ogni riga,
    - il path fileTerne di un file di testo da creare.
    La funzione legge le parole presenti nel file di FileParole e crea
    un nuovo file di testo che salva all'indirizzo fileTerne e restituisce infine il
    numero totale di caratteri presenti nelle parole del file FileParole (ignorando spazi e accapi).
    Il file creato ha lo stesso numero di righe del file letto (una per ogni parola)
    ma le parole in ciascuna riga sono sostituite da terne di interi. Piu' precisamente in
    corrispondenza della generica parola s viene prodotta la stringa con la tupla
    (a,b,c) seguita da accapo,
    dove a e' la lunghezza della parola s, b e' il numero di vocali presenti nella
    parola s e c e' il numero di lettere maiuscole presenti nella parola s.

    Ad esempio se il file delle parole contiene le due parole 'PytHon' e 'fonDAMenti'
    la funzione deve creare e salvare in fileTerne un  file di due righe con le due
    terne (6,1,2) e (10,4,3) e restituire poi l'intero 16.
    """
    with open(fileParole) as f:
        words = f.readlines()
    words = [word.strip() for word in words if len(word) > 1]
    result = 0
    with open(fileTerne, "w+") as f:
        for word in words:
            result += len(word)
            tupla = (len(word), vocals_counter(word), upper_counter(word))
            tupla = str(tupla) + "\n"
            f.write(tupla)
    return result


def vocals_counter(word):
    result = 0
    for elem in word:
        if elem in "aeiouAEIOU":
            result += 1
    return result


def upper_counter(word):
    result = 0
    for elem in word:
        if elem == elem.upper():
            result += 1
    return result


es63("ftesto1.txt", "sfsfsf")
