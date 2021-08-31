def conversor (tipo_pesos, valor_dolar):
    pesos= input("¿Cuantos pesos "+ tipo_pesos+" tienes?: ")
    pesos=float(pesos)
    pesos=int(pesos)
    dolares_venta=pesos/valor_dolar
    dolares_venta=round(dolares_venta,2)
    pesos=str(pesos)
    valor_dolar=str(valor_dolar)
    dolares_venta=str(dolares_venta)
    print("Si quieres cambiar tus $"+ pesos +" a dolares la cotizacion estaria en: "+valor_dolar+" Venta: USD "+ dolares_venta)
    


menu=""""
Bienvenido al conversor de monedas💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: 
"""
opcion=input(menu)

if opcion=="1":
    conversor("colombianos",3830.98)
elif opcion=="2":
    conversor("argentinos",174)
elif opcion=="3":
   conversor("mexicano",19.86)
else:
    print("Ingresa una opción correcta por favor: ")

 