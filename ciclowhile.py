#Ciclo mientras

#Declarar una variable centinela
#O Variable de control para evaluar
# La ejecución de mi ciclo 
#variableOservadora=100
i=0

#programar la estructura del ciclo mientras
# while(i<20):
#     print("estoy saltando cuerda",i)
#     i=i+1 #contador
# print("terminamos de saltar")

# while(i!=5):    
#     i=int(input("Digite una opción del menú:"))
#     if (i==1):
#         print("Hola cómo estás")
#     if (i==2):
#         print("chao amor")
#     if (i==3):
#         print("Ganador el ROJO")
#     if (i==4):
#         print("No llueve en Medallo")
#     if (i==5):
#         break
#     else:
#         print("Digita una opción válida")

# #MEÚ DE OPCIONES
# print("****MENÚ****")
# print("1. SUMAR 2 NÚMEROS")
# print("2. RESTAR 2 NÚMEROS")
# print("3. ENCONTRAR LA RAIZ CUADRADA DE UN NÚMERO")
# print("4. MULTIPLICAR 2 NÚMEROS")
# print("5. SALIR")


#Listas o arreglos de datos

#Útiles para almacenar más de 1 dato en una sola variable
# numeros=[1,2,3,4,5]
# nombres=["Juan", "Sara", "Carlos","Catalina"]

# print(numeros)
# print(numeros[1])

#Recorrer o iterar una lista (Arreglo de datos)

# for observador in nombres:
#     print(observador)

#Los diccionarios son variables especiales
#que me permiten almacenar multiples datos 
#de diferente TIPO EN UNA SOLA VARIABLE

empleado={
    'nombre' : 'Juan',
    'cedula' : 1017170603,
    'cargo': "Analista de datos",
    'salario': 5000000,
    'horasTrabajadas': 40,
    'aplicaSubsidioTransporte': False,
    'deudas':[1500000,800000]
}
print(empleado)
print(empleado['deudas'][1])

#Recorriendo un diccionario: 
for observadorAtributo,observadorValor in empleado.items():
    print(observadorAtributo)
    print(observadorValor)

    
