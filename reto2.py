
#entradas

Estacion=input("digite mes:")
Estaciones=Estacion.lower
  
#proceso

if(Estaciones=="enero"or Estaciones=="febrero" or Estaciones=="marzo"):
    print(f'el mes que seleccionaste es {Estaciones} y estas en Invierno')
elif(Estaciones=="abril" or Estaciones=="mayo" or Estaciones=="junio"):
   print(f'el mes que seleccionaste es {Estaciones} y estas en Primavera')
elif(Estaciones=="julio" or Estaciones=="agosto" or Estaciones=="septiembre"):
    print(f'el mes que seleccionaste es {Estaciones} y estas en Invierno')
elif(Estaciones=="octubre" or Estaciones=="noviembre" or Estaciones=="diciembre"):
    print(f'el mes que seleccionaste es {Estaciones} y estas en Invierno')
else:
    print("el mes que seleccionaste no es valido")
#salida