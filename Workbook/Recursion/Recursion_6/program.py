import os
import os.path


def es69(dirs, profondita, estensioni):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva) es69(dir, profondita, estensioni),
    che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
    solo se si trovano alla profondita' indicata, e che riceve come argomenti:
        dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
        profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory radice passata come argomento
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
    La funzione deve tornare il numero totale di files presenti nelle directories di profondita' minore o uguali a 'profondita',
    che NON sono stati cancellati

    NOTA: per eliminare un file usate la funzione os.remove

    Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non esistano a seconda del caso (senza usare una soluzione ricorsiva ma testando direttamente i path dei files relativi alla dir iniziale)
    Test: che la funzione sia ricorsiva
    """
    lista = recursion(dirs,profondita,estensioni,[],0)
    lista.append((dirs,0))
    tot = 0
    el = 0
    for elem in lista:
        if elem[1]<=profondita:
            for item in os.listdir(elem[0]):
                if os.path.isfile(elem[0]+'/'+item):
                    tot+=1
                    if elem[1]==profondita:
                        for est in estensioni:
                            lenn = len(est)
                            if item[-lenn:]==est:
                                el+=1
                                os.remove(elem[0]+'/'+item)
    return tot - el
                            
def recursion(d,p,c,l,pro):
    if pro==p: return []
    if os.path.isdir(d):
        if len(os.listdir(d))==0:
            return []
        else:
            for elem in os.listdir(d):
                path = d+'/'+elem
                if os.path.isdir(path):
                    l.extend([(path,pro+1)])
                recursion(path,p,c,l,pro+1)
    else: return []
    return l
            
es69('t2', 3, ['jpg', 'png'])