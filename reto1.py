
#entradas

nivelAgua=int(input("digite el nivel de agua:"))
  
#proceso

if(nivelAgua>=0 and nivelAgua<20):
    print(f'el nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua>= 20 and nivelAgua<=400 ):
    print(f'el nivel de agua es {nivelAgua} y opera normalmente')
elif(nivelAgua>=400):
    print(f'el nivel de agua es {nivelAgua} llamen a fico')
else:
    print("el nivel de agua no es valido")
#salida

