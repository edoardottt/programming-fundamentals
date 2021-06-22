import albero


def es14(tree, x):
    """
      Es 2: 6 punti
      Si definisca la funzione es14(tree,x) ricorsiva (o che fa uso di funzioni o metodi ricorsive/i) 
      che riceve come argomenti:
      -  'tree' un  albero  formato da nodi di tipo AlberoBinario definito nella libreria 
          albero.py allegata
      - un intero x
      - calcola il numero di nodi che nell'albero che hanno valore divisibile per x 
      - torna come risultato il numero calcolato

      ATTENZIONE: E' VIETATO USARE I METODI DELLA LIBRERIA albero

      Esempio: se x = 2 e l'albero e':

              7
              /\
            1  3
            / \
          4    6
        /    /
        5    2
      /     \
      9       8

  Nell'albero ci sono 3 nodi con valore divisibile per 2+livello (sono i nodi a valore 3,4 e 5)
  cosi'  la funzione tornera' il valore 3.
  """
    ins = rec(tree, x, 0, 0)
    return ins


def rec(tree, x, l, c):
    if tree.sx == None and tree.dx == None:
        if tree.valore % (x + l) == 0:
            c += 1
        return c
    elif tree.sx == None:
        if tree.valore % (x + l) == 0:
            c += 1
        return rec(tree.dx, x, l + 1, c)
    elif tree.dx == None:
        if tree.valore % (x + l) == 0:
            c += 1
        return rec(tree.sx, x, l + 1, c)
    else:
        if tree.valore % (x + l) == 0:
            c += 1
        c1 = rec(tree.sx, x, l + 1, 0)
        c2 = rec(tree.dx, x, l + 1, 0)
        return c + c1 + c2


lista = [
    9,
    [2, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]],
    [4, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]],
]
tree = albero.AlberoBinario.fromList(lista)
print(es14(tree, 1))
