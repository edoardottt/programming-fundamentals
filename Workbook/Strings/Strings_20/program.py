import immagini
import json


def es23(fileJson, filePng):
    """
    Abbiamo un file di tipo json contenente una matrice (lista di liste) M i cui elementi
    sono stringhe. La matrice e' il risultato della codifica di un'immagine.
    L'immagine ha ampiezza w e altezza h dove w e' il numero di colonne della matrice M e h
    il numero di righe. Il colore (r,g,b) del  pixel di coordinate x,y e' codificato con
    la stringa presente in M[y][x], piu' precisamente la stringa e' composta da 9 cifre.
    Le tre piu' significative sono la codifica di r, le tre centrali sono la codica di g e le tre
    meno significative la codifica di b.

    Scrivete la funzione es7(fileJson, filePng) che riceve come argomenti:
        :param fileJson: il path del file json dove si trova la matrice dell'immagine codificata
        :param filePng:  il path del file PNG dove salvare l'immagine decodificata.
        :return: il colore che appare piu' spesso tra quelli dei pixel dell'immagine (a parita'
        viene selezionato il colore che precede nell'ordinamento crescente
        rispetto alla prima, alla seconda e poi alla terza coordinata).
    """
    with open(fileJson) as f:
        imm = json.load(f)
    diz = {}
    for i in range(len(imm)):
        for j in range(len(imm[0])):
            imm[i][j] = decode(imm[i][j])
            if imm[i][j] not in diz:
                diz[imm[i][j]] = 1
            else:
                diz[imm[i][j]] += 1
    freq = {}
    for elem in diz:
        if diz[elem] not in freq:
            freq[diz[elem]] = [elem]
        else:
            freq[diz[elem]].append(elem)
    return sorted(freq[max(freq.keys())], key=lambda x: (x[0], x[1], x[2]))[0]


def decode(s):
    r = int(s[0:3])
    g = int(s[3:6])
    b = int(s[6:9])
    return r, g, b
