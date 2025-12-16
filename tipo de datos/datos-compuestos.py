#Creando una lista se pueden modificar
lista = ["Ordenador", "Tele", 324, True]
#Creando una tupla, no se pueden modificar
tupla = ("Ordenador", "Tele", 324, True)

#Esto es valido
lista[3] = "Maquinola"

#Esto no es valido
#tupla[3] = "Maquinola"

#creando un conjunto (set)
conjunto = {"Ordenador", "Tele", 324, True}
#Conjunto no te deja acceder a los elementos por su indice, no almacena datos duplicados//print(conjunto[1])

#Creando un diccionario(dict)
diccionario = {
    'nombre' : "Ismael Cruz",
    'profesion' : "Vigilante de Seguridad",
    'estado_emocionado' : True,
    'dato_duplicado' : "Ismael Cruz"
}
print(diccionario["profesion"])