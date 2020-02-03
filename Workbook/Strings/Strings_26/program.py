def es33(fname1,fname2):
    ''' 
    Implementate la funzione es33(fname1,fname2) prende in input l'indirizzo di un  file di testo fname e
    costruisce un istogramma con le frequenze di alcuni dei caratteri presenti nel  file di testo. 
    Salva l'istogramma creato nel file di testo fname2 e restituisce il numero di linee di cui e' composto.
    L'istogramma contiene tante linee quanti sono i caratteri tra 'a' e 'z' presenti nel testo.
    Se un certo carattere x compare nel testo  y volte allora nell'istogramma ci sara' 
    una riga con una stringa composta dal carattere x ripetuto y volte. Le righe dell'istogramma 
    vanno ordinate per lunghezza decrescente dei caratteri che vi compaiono e 
    lessicograficamente a parita' di lunghezza.
    Ad esempio se il file fname1 contiene il testo 'Monti, Sterbini e Spognardi' allora
    il valore restituito dalla funzione sara' 11 e  l'istogramma sara'
    iiii
	nnn
	ee
	oo
	rr
	tt
	a
	b
	d
	g
	p
    '''
    with open(fname1) as f:
        text = f.read()
    ls = [item for item in text if 'a'<=item<='z']
    diz = {}
    for elem in set(ls):
        k = ls.count(elem)
        if k not in diz: diz[k] = [elem]
        else: diz[k].append(elem)
    res =''
    for k in sorted(diz,reverse=True):
        c = sorted(diz[k])
        for elem in c:
            res+=elem*k+'\n'
    res = res[:-1]
    with open(fname2,'w+') as f:
        f.write(res)
    return len(set(ls))
print(es33('ftesto3.txt', 'istogramma1.txt'))