def equazione_positiva(a,b,c):
     x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
     return(x1)
def equazione_negativa(a,b,c):
     x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
     return(x2)



(-9+0.8569568250501305j) ma perchè mi da sto risultato?

​def equazione(a,b,c):
  radpos = ((-b)+(sqrt(b**2-4*a*c)))/2*a
 ​ radneg= ((-b)-(sqrt(b**2-4*a*c)))/2*a
  ​return radpos, radneg
