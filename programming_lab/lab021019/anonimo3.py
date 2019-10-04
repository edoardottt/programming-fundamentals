
a=int(input("inserisci il valore di a"))
b=int(input("inserisci il valore di b"))
c=int(input("inserisci il valore di c"))
def calcola_x1(a,b,c):
     x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
     return(x1)
def calcola_x2(a,b,c):
     x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
     return(x2)
calcola_x1(a,b,c)
calcola_x2(a,b,c)
print(x1,x2,sep=",")
