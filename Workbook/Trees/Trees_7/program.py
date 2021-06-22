import albero


def es6(percorsi):
    """
    Si definisca la funzione es6(testo) ricorsiva (o che fa uso di funzioni o
    metodi ricorsive/i) che:
    - riceve come argomento:
       - un insieme di stringhe che hanno la proprietà che ciascuna è stata
       ottenuta a partire dallo stesso albero binario
          (in cui ciascun nodo contiene un solo carattere), risalendo da ciascuna
          foglia fino alla radice e concatenando
          i valori dei nodi
          NOTA l'albero è localmente ordinato da sinistra a destra, ovvero:
          - ciascun figlio sinistro contiene un carattere minore di quello del padre
          - ciascun figlio destro contiene un carattere maggiore di quello del padre
    - ricostruisce l'albero originale e lo torna come risultato

    Esempio: se l'albero da ricostruire è
                      i
                      |
              |-----------------|
              h                 m
              |                 |
          |--------|        |------|
          c        j        k      p
          |        |               |
       |-----|  |-----|         |-----|
       a     f  g     k         m     q

    L'insieme di stringhe è
       { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }

    ATTENZIONE: è VIETATO usare i metodi della classe AlberoBinario

    """
    ls = list(percorsi)
    root = albero.AlberoBinario(ls[0][-1])
    for per in ls:
        root = create(root, per[:-1])
    return root


def create(root, per):
    if per == "":
        return root
    elif per[-1] < root.valore:
        if root.sx:
            create(root.sx, per[:-1])
        else:
            sx = albero.AlberoBinario(per[-1])
            root.sx = sx
            create(root.sx, per[:-1])
    else:
        if root.dx:
            create(root.dx, per[:-1])
        else:
            dx = albero.AlberoBinario(per[-1])
            root.dx = dx
            create(root.dx, per[:-1])
    return root
