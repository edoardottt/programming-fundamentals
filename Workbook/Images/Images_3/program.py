import immagini

def es4(fimm, fimm1, h1, w1):
    '''    
    Si definisca la  funzione es4(fimm,fimm1) che, 
    - riceve gli  indirizzi fimm e fimm1 di due file .PNG. e due interi h1 e w1 maggiori di zero.
    - legge l'immagine da fimm e crea una seconda  immagine. L'immagine da creare 
      ha h1 volte la lunghezza di quella letta e w1 volte la larghezza di quella letta e si ottiene 
      sostituendo ad ogni pixel dell'immagine letta un rettangolo di pixels di altezza h e ampiezza w aventi 
      tutti il colore del pixel originario.
    - salva l'immagine creata all'indirizzo fimm.
    - restituisce la tupla con il colore che compare piu' spesso nell'immagine letta e in 
    caso di parita' di occorrenze massime il colore del pixel che viene prima lessicograficamente.
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    fimm = immagini.load(fimm)
    h = len(fimm)
    w = len(fimm[0])
    h2 = h*h1
    w2 = w*w1
    diz = {}
    m = [[0 for i in range(w2)] for j in range(h2)]
    for i in range(len(m)):
        for j in range(len(m[0])):
            ii = i//h1
            jj = j//w1
            m[i][j] = fimm[ii][jj]
            col = fimm[ii][jj]
            if col not in diz: diz[col] = 1
            else: diz[col]+=1
    immagini.save(m,fimm1)
    lista = []
    colmax = max(diz.values())
    for k in diz.keys():
        if diz[k]==colmax:
            lista.append(k)
    return sorted(lista)[0]