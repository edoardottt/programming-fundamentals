def es25(n):
    """
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
    """
    if n == 0:
        return [1]
    else:
        ls = []
        l = es25(n - 1)
        for i in range(len(l) + 1):
            if i == 0:
                ls.append(1)
            elif i == len(l):
                ls.append(1)
            elif 0 <= i - 1 <= len(l) - 1:
                ls.append(l[i] + l[i - 1])
            else:
                ls.append(1)
        return ls


print(es25(5))
