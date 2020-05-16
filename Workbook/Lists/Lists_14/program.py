def es25(n):
    '''
    Si definisca la funzione es25(n) che calcola la riga i-esima del triangolo di Tartaglia,
    ovvero la lista dei coefficienti della potenza i-esima del binomio (a+b).

    Si ricorda la definizione del triangolo di Tartaglia:
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
       ...........
    Tartaglia(0) = [1]   # caso base
    I numeri che appaiono in ciascuna riga del triangolo di Tartaglia si ottengono
    come somma di quelli sovrastanti nella riga precedente.
    Dove non troviamo una cifra consideriamo che si trovi un valore 0 (zero)
    '''
    return tartaglia(n)

def tartaglia(n):
    if n==0: return [1]
    else:
        lista = [0]
        lista.extend(tartaglia(n-1))
        lista.append(0)
        lista2 = []
        for i in range(1,len(lista)):
            lista2.append(lista[i]+lista[i-1])
        return lista2