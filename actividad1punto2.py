nombres="Agustin","Alan","Andrés","Ariadna","Bautista","CAROLINA","CESAR","David","Diego","Dolores","DYLAN","ELIANA","Emanuel","Fabián","Facundo","Facundo","FEDERICO","FEDERICO","GONZALO","Gregorio","Ignacio","Jonathan","Jonathan","Jorge","JOSE","JUAN","Juan","Juan","Julian","Julieta","LAUTARO","Leonel","LUIS","Luis","Marcos","María","MATEO","Matias","Nicolás","NICOLÁS","Noelia","Pablo","Priscila","TOMAS","Tomás","Ulises","Yanina"
eval1=[81,60,72,24,15,91,12,70,29,42,16,3,35,67,10,57,11,69,12,77,13,86,48,65,51,41,87,43,10,87,91,15,44,85,73,37,42,95,18,7,74,60,9,65,93,63,74]
eval2=[30,95,28,84,84,43,66,51,4,11,58,10,13,34,96,71,86,37,64,13,8,87,14,14,49,27,55,69,77,59,57,40,96,24,30,73,95,19,47,15,31,39,15,74,33,57,10]

lr = list(map(lambda n,m:n+m,eval1,eval2))
def reporte():
    """     Para los reportes primero se debe seleccionar sobre qué valores se hará el reporte y una vez seleccionado el mismo se le pedirá que indique un rango de valores e informar lxs estudiantes que estén dentro del rango seleccionado"""
print(reporte.__name__)
print(reporte.__doc__)

seleccionar={'1':"eval1",'2':"eval2",'3':"Suma de ambas notas",'4':"Salir"}
seleccionOrden = '0'
while (seleccionOrden != '4'):
    print("Seleccione una opcion:")
    for clave in seleccionar.keys():
        print(clave,seleccionar[clave])
    seleccionOrden=input()
    if seleccionOrden == '1':
        #Nota de la evaluacion 1
        print('Evaluacion 1:\n')
        for valor in range(0,len(lr)):
            print('El rango',valor,'esta',nombres[valor],'con la evaluacion 1=',eval1[valor])
    elif seleccionOrden == '2': 
        #Nota de la evaluacion 2
        print('Evaluacion 2:\n')
        for valor in range(0,len(lr)):
            print("El rango",valor,"esta",nombres[valor],"con la evaluacion 2=",eval2[valor])
    elif seleccionOrden == '3': 
        #Suma de ambas notas
        print('Suma de ambas notas:\n')
        for valor in range(0,len(lr)):
            print("El rango",valor,"esta",nombres[valor],"con la suma de ambas notas=",lr[valor])
    elif seleccionOrden == '4': 
        #Cambiar print por la llamada a la def
        print()
    else:
        print ("Numero no valido")
    print('-' * 40)