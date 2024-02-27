

import math
 
# Cada elemento de este diccionario contiene una posicion del camino, y como 
# valor tiene una lista con el calculo del camino mas corto, y el origen del
# mismo
valores={
    #Estos numeros son las ciudades, pero con numeros
    #"0":[math.inf,""],
    #"1":[math.inf,""],
    #"2":[math.inf,""],
    #"3":[math.inf,""],
    #"4":[math.inf,""],
    #"5":[math.inf,""],
    #"6":[math.inf,""],
    #"7":[math.inf,""],
    #"8":[math.inf,""],
    #"9":[math.inf,""],
    #"10":[math.inf,""],
    #"11":[math.inf,""],
    #"12":[math.inf,""],
    #"13":[math.inf,""],
    #"14":[math.inf,""],
    #"15":[math.inf,""],
    #"16":[math.inf,""],
    #"17":[math.inf,""],
    #"18":[math.inf,""],
    #"19":[math.inf,""]
    #ESTAS SON LAS CIUDADES
    "Arad":[math.inf,""],
    "Zerind":[math.inf,""],
    "Timisoara":[math.inf,""],
    "Oradea":[math.inf,""],
    "Lugoj":[math.inf,""],
    "Sibiu":[math.inf,""],
    "Mehadia":[math.inf,""],
    "Rimmicu Vilcea":[math.inf,""],
    "Fagaras":[math.inf,""],
    "Dobreta":[math.inf,""],
    "Craiova":[math.inf,""],
    "Pitesti":[math.inf,""],
    "Bucharest":[math.inf,""],
    "Giurgiu":[math.inf,""],
    "Urziceni":[math.inf,""],
    "Vaslui":[math.inf,""],
    "Hirsova":[math.inf,""],
    "Lasi":[math.inf,""],
    "Eforie":[math.inf,""],
    "Neamt":[math.inf,""]
}
 
# aquí establecemos cada uno de los caminos en una sola dirección y el coste
# que tiene cada camino
caminos=[
    #["0","1",75],
    #["0","2",118],
    #["0","5",140],
    #["1","3",71],
    #["2","4",118],
    #["3","5",151],
    #["4","6",70],
    #["5","7",80],
    #["5","8",99],
    #["6","9",75],
    #["7","10",146],
    #["7","11",97],
    #["8","12",211],
    #["9","10",120],
    #["10","11",138],
    #["11","12",101],
    #["12","13",90],
    #["12","14",85],
    #["14","15",142],
    #["14","16",98],
    #["15","17",92],
    #["16","18",86],
    #["17","19",87],
    
    ["Arad","Zerind",75],
    ["Arad","Timisoara",118],
    ["Arad","Sibiu",140],
    ["Zerind","Oradea",71],
    ["Timisoara","Lugoj",118],
    ["Oradea","Sibiu",151],
    ["Lugoj","Mehadia",70],
    ["Sibiu","Rimmicu Vilcea",80],
    ["Sibiu","Fagaras",99],
    ["Mehadia","Dobreta",75],
    ["Rimmicu Vilcea","Craiova",146],
    ["Rimmicu Vilcea","Pitesti",97],
    ["Fagaras","Bucharest",211],
    ["Dobreta","Craiova",120],
    ["Craiova","Pitesti",138],
    ["Pitesti","Bucharest",101],
    ["Bucharest","Giurgiu",90],
    ["Bucharest","Urziceni",85],
    ["Urziceni","Vaslui",142],
    ["Urziceni","Hirsova",98],
    ["Vaslui","Lasi",92],
    ["Hirsova","Eforie",86],
    ["Lasi","Neamt",87],
]
 
def setValores(origen,destino,valor):
    """
    Función que actualiza el valor del diccionario valores, actualizando
    el valor al mas bajo y indicando de de que punto viene el camino mas corto
    Tiene que recibir:
        origen -> punto inicial
        destino -> punto final
        valor -> valor de ese tramo + el valor que tiene el origen
    Devuelve True o False, dependiendo si ha disminuido el valor entre dos puntos
    """
    if valor<valores[destino][0]:
 
        # guardamos el nuevo valor mas bajo
        valores[destino][0]=valor
 
        # guardamos de donde viene el valor mas bajo
        valores[destino][1]=origen
        return True
    return False
print("-----------------------------------------------------")
print("╦═╗╦ ╦╔╦╗╔═╗  ╔╦╗╔═╗╔═╗  ╔═╗╔═╗╦═╗╔╦╗╔═╗")
print("╠╦╝║ ║ ║ ╠═╣  ║║║╠═╣╚═╗  ║  ║ ║╠╦╝ ║ ╠═╣")
print("╩╚═╚═╝ ╩ ╩ ╩  ╩ ╩╩ ╩╚═╝  ╚═╝╚═╝╩╚═ ╩ ╩ ╩\n")
#Imprimir las ciudades
print("-----------------------------------------------------")
print("LAS CIUDADES SON LAS SIGUIENTES")
print("-----------------------------------------------------")
for i in valores:
    print (i)


#imprimir distancia de las ciudades
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
#print("LAS DISTANCIAS ENTRE LAS CIUDADES SON LAS SIGUIENTES")
#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
#for j in caminos:
#    print (j)
# definimos el inicio y el destino
print("-----------------------------------------------------")
print("Escriba la ciudad de inicio: ")
inicio=input()
print("Escriba la ciudad llegada: ")
final=input()
 
valores[inicio][0]=0
 
# realizamos un bucle hasta que no haya ningun otro cambio de valores
while True:
    cancel=True
 
    # recorremos cada uno de los caminos
    for i in caminos:
 
        # enviamos los datos del camino
        if setValores(i[0],i[1],valores[i[0]][0]+i[2]):
            cancel=False
 
        # enviamos los datos del camino de forma invertida
        if setValores(i[1],i[0],valores[i[1]][0]+i[2]):
            cancel=False
 
    # finalizamos el bucle cuando ya no hay ningun cambio en los valores
    if cancel:
        break
 
# iniciamos la busqueda del camino mas corto
camino=[final]
 
while True:
    if camino[-1]==inicio:
        break
    camino.append(valores[camino[-1]][1])
print()
print("La ruta mas corta desde la ciudad '{}' y la ciudad '{}' es: {}".format(inicio, final, camino[::-1]))
