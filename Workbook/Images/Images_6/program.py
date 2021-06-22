import immagini


def es15(fimm1, fimm2, fimm3):
    """
    Es 3: 6 punti
    Si definisca la  funzione es3(fimm1,fimm2,fimm3) che,
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo
      di un file (fimm3) da creare.
    - legge le due immagini DI DIMENSIONI DIVERSE e crea la terza immagine da salvare all'indirizzo fimm3.
      La terza immagine si ottiene dalle prime due. Ha ampiezza  massima tra
      le ampiezze  di fimm1 e fimm2 ed  altezza massima tra le altezze di fimm1 e fimm2.
      Per quanto riguarda i colori dei pixel della nuova immagine:
      il pixel [y][x] avra' colore nero (vale a dire (0,0,0)) se presente in entrambe
      le immagini originarie o in nessuna delle due. In caso contrario assumera' il   colore
      del pixel dell'unica immagine originaria in cui e' presente.
      (guardate le immagini di test per chiarimenti)
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel di colore nero presenti  nell'immagine creata.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    """
    imm1 = immagini.load(fimm1)
    imm2 = immagini.load(fimm2)
    w1 = len(imm1[0])
    h1 = len(imm1)
    w2 = len(imm2[0])
    h2 = len(imm2)
    maxw = max([w1, w2])
    maxh = max([h1, h2])
    black = (0, 0, 0)
    count = 0
    imm3 = [[0 for i in range(maxw)] for j in range(maxh)]
    for i in range(len(imm3)):
        for j in range(len(imm3[0])):
            if nero(i, j, w1, h1, w2, h2):
                imm3[i][j] = black
                count += 1
            else:
                col = colore(imm1, imm2, i, j, w1, h1, w2, h2)
                if col == black:
                    count += 1
                imm3[i][j] = col
    immagini.save(imm3, fimm3)
    return count


def nero(i, j, w1, h1, w2, h2):
    im1 = i < h1 and j < w1
    im2 = i < h2 and j < w2
    if im1 and im2:
        return True
    if not (im1 or im2):
        return True
    return False


def colore(imm1, imm2, i, j, w1, h1, w2, h2):
    if i < h1 and j < w1:
        co = imm1[i][j]
    else:
        co = imm2[i][j]
    return co
