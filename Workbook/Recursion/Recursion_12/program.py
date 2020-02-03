import albero
def es1(tree1,tree2):
    '''
    Es 1: 6 punti
    Si definisca la funzione es1(tree1,tree2) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che:
    - riceve come argomenti 'tree1' e 'tree2' due alberi  formati da nodi di tipo 
      AlberoBinario definito nella libreria albero.py allegata
    - Genera un albero di tipo AlberoBinario
    - torna come risultato la radice dell'albero generato.
    I due alberi in input hanno identica struttura ma l'informazione contenuta nel campo 
    valore dei nodi corrispondenti puo' essere diversa. L'albero da generare deve avere  
    la stessa struttura dei due alberi in input e il valore dei nodi del nuovo albero viene 
    calcolato in base alla seguente regola.
    Siano   x e y i due nodi corrispondenti di tree1 e 
    tree2 rispettivamente, 
    - si effettua la somma dei valori  dei  nodi presenti nel sottoalbero in tree1 radicato in x. 
    - si effettua la somma dei valori dei  nodi presenti nel sottoalbero in  tree2 radicato in y.
    -si assegna al nodo corrispondente la somma delle due somme ottenute. 
    Esempio: se tree1 e tree2 sono i due alberi sotto a sinistra allora tree3 sara' 
    l'albero sotto a destra
    
    ATTENZIONE: È VIETATO USARE LE FUNZIONE DELLA CLASSE AlberoBinario

             1              7            90           |
            /\             /\            /\           |
           2  3           1  3          76  6         |
          / \            / \           / \            |
        4    5          4   6        36  37           |
       /    /          /   /         /   /            |
      6    7          5   2         28 26             |
     /     \         /    \        /    \             |
     8      9       9      8      17    17            | 
     

     I due alberi in input non vanno modificati
    '''
    radice = recursion(tree1,tree2)
    return radice
    
def recursion(t1,t2):
    if t1.sx==None and t2.dx==None:
        val = t1.valore+t2.valore
        nodo = albero.AlberoBinario(val,None,None)
        return nodo
    elif t1.sx==None:
        val = t1.valore + t2.valore
        figlio = recursion(t1.dx,t2.dx)
        val = val + figlio.valore
        nodo = albero.AlberoBinario(val,None,figlio)
        return nodo
    elif t1.dx==None:
        val = t1.valore + t2.valore
        figlio = recursion(t1.sx,t2.sx)
        val = val + figlio.valore
        nodo = albero.AlberoBinario(val,figlio,None)
        return nodo
    else:
        val = t1.valore + t2.valore
        nodosx = recursion(t1.sx,t2.sx)
        nododx = recursion(t1.dx,t2.dx)
        val = val + nodosx.valore + nododx.valore
        nodo = albero.AlberoBinario(val,nodosx,nododx)
        return nodo
    
    
lista1 = [1, [2, [4, [6, [8, None, None], None], None], [5, [7, None, [9, None, None]], None]], [3, None, None]]
lista2 = [7, [1, [4, [5, [9, None, None], None], None], [6, [2, None, [8, None, None]], None]], [3, None, None]]
lista3 = [90, [76, [36, [28, [17, None, None], None], None], [37, [26, None, [17, None, None]], None]], [6, None, None]]
    
tree1 = albero.AlberoBinario.fromList(lista1)
tree2 = albero.AlberoBinario.fromList(lista2)
print(es1(tree1,tree2))
    
    
