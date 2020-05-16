import albero

def es66(tree):
    """
    Es  17: 9 punti - ricorsivo

    Si definisca la funzione es66, ricorsiva (o che fa uso di vostre funzioni ricorsive) che:
    - riceve come argomento un AlberoBinario (definito nel file albero.py)

    Calcola la "larghezza massima" dell'albero,  ovvero la differenza tra 
    la posizione del nodo che si trova piu' a destra nell'albero
    e la posizione del nodo che si trova piu' a sinistra.
    Per calcolare la posizione di un nodo rispetto alla radice (che assumiamo sia a posizione 0)
    basta sottrarre 1 (uno) ogni volta che si scende su un sottoalbero sinistro
    ed aggiungere 1 (uno) ogni volta che si scende su un sottoalbero destro.
    Esempio: se l'albero e' quello qui sotto a sinistra le posizioni saranno quelle nell'albero a destra
             1           .            0         .
            / \          .           / \        .
           2   3         .         -1   1       .
          / \            .        /  \          .
        4    5           .      -2    0         .
       /    /            .      /    /          .
      6    7             .    -3    -1          .
       \    \            .      \    \          .
        8    9           .      -2    0         .
    Il nodo piu' a sinistra (6) e' a posizione -3
    mentre quello piu' a destra (3) e' a posizione 1
    Quindi la funzione torna il valore 4=1-(-3)
    """
    ins = rec(tree,0,set())
    return abs(max(ins) - min(ins))

def rec(t,v,lista):
    if t.sx==None and t.dx==None: 
        t.valore = v
        lista.add(v)
    elif t.sx==None:
        t.valore = v
        lista.add(v)
        rec(t.dx,v+1,lista)
    elif t.dx==None:
        t.valore = v
        lista.add(v)
        rec(t.sx,v-1,lista)
    else:
        t.valore = v
        lista.add(v)
        rec(t.sx,v-1,lista)
        rec(t.dx,v+1,lista)
    return lista
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        