import os
import os.path

def es69(dirs, profondita, estensioni):
    """
    Si definisca la funzione  ricorsiva (o che usa una vostra funzione ricorsiva)
    es69(dir, profondita, estensioni),
    che deve eliminare tutti i file che appartengono ad una delle estensioni indicate,
    solo se si trovano alla profondita' indicata, e che riceve come argomenti:
        dir: la directory in cui cercare (i file in questa directory si trovano a profondita 0)
        profondita: la profondita' in cui dobbiamo cancellare i file, contando da 0 per la directory 
        radice passata come argomento
        estensioni: una lista di stringhe "estensioni" (le ultime lettere del nome dei files che cerchiamo)
    La funzione deve tornare il numero totale di files presenti nelle directories di profondita' 
    minore o uguali a 'profondita',
    che NON sono stati cancellati

    NOTA: per eliminare un file usate la funzione os.remove

    Tests: date alcune directories contenenti file con estensioni diverse a diverse profondita', 
    si chiama la funzione e si controlla che i file contenuti nelle directories esistano/non esistano 
    a seconda del caso (senza usare una soluzione ricorsiva ma testando direttamente i path dei files 
    relativi alla dir iniziale)
    Test: che la funzione sia ricorsiva
    """
    count,rem = rec(dirs,profondita,0,estensioni,[],[])
    return len(count) - len(rem)

def rec(dirs,pro,liv,est,count,rem):
    print(dirs,liv,pro,rem)
    if os.path.isfile(dirs):
        if liv==pro:
            count.append(dirs)
            for es in est:
                if dirs[-len(es):]==es:
                    rem.append(dirs)
                    os.remove(dirs)
                    return count,rem
    elif os.path.isdir(dirs):
        if liv<=pro:
            for elem in os.listdir(dirs):
                if os.path.isdir(dirs+'/'+elem):
                    count,rem = rec(dirs+'/'+elem,pro,liv+1,est,count,rem)
                else: count, rem = rec(dirs+'/'+elem,pro,liv,est,count,rem)
    return count,rem
            
print(es69('t2', 3, ['jpg', 'png']))
            