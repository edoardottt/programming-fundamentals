# -*- coding: utf-8 -*-
nome = input("Inserisci il nome ")
frutto = input("Inserisci il frutto ")
print(nome, "adora mangiare", frutto)
print(nome + " adora mangiare " + frutto)
print("%s adora mangiare %s" % (nome, frutto))
s = "{} adora mangiare {}"
print(s.format(nome, frutto))
