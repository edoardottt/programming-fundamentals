import immagini


def es42(fImageIn, fcolori, fImageOut):
    """
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di alcuni pixel presenti in un immagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    """
    imin = immagini.load(fImageIn)
    with open(fcolori) as f:
        colori = f.readlines()
    colori = [item.split() for item in colori]
    cols = []
    for item in colori:
        a = (int(item[0]), int(item[1]), int(item[2]))
        b = (int(item[3]), int(item[4]), int(item[5]))
        cols.append((a, b))
    res = 0
    print(cols)
    for i in range(len(imin)):
        for j in range(len(imin[0])):
            for elem in cols:
                if imin[i][j] == elem[0]:
                    imin[i][j] = elem[1]
                    res += 1
                    break
    immagini.save(imin, fImageOut)
    return res


es42("scacchiera.png", "fcolori2.txt", "out2.png")
