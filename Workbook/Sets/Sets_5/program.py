def es44(a, b):
    '''
    Si progetti la funzione es44(a,b) che,  in input due interi a e b restituisce 
    l'insieme dei primi a interi che hanno esattamente b divisori.
    Ad esempio per a=20 e b=2 la funzione deve restituire l'insieme dei primi 20 numeri primi
    (perche' solo i numeri primi hanno esattamente 2 divisori), vale a dire:
    {2, 3, 67, 5, 37, 7, 71, 41, 11, 43, 13, 47, 17, 19, 61, 53, 23, 59, 29, 31}
    '''
    goon = True
    insieme = set()
    i = 2
    while goon:
        divisori = set()
        for j in range(1,i+1):
            if i%j==0:
                divisori.add(j)
        if len(divisori)==b:
            insieme.add(i)
        i+=1
        if len(insieme)==a: goon=False
    return insieme

print(es44(2,4))