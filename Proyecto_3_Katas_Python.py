from functools import reduce

"""
1.
Escribe una función que reciba una cadena de texto como parámetro
y devuelva un diccionario con las frecuencias de cada letra en la cadena.
Los espacios no deben ser considerados.
"""
from logging import exception


def letras():
    texto = input("Texto: ")
    letras = {}    #Diccionario
    texto_editado = texto.replace(" ", "") #quitar espacios
    for let in texto_editado:
        if let in letras:
            letras[let] += 1
        else:
            letras[let] = 1
    print(letras)
#letras()
"""
2.
Dada una lista de números, obtén una nueva lista con el doble de cada valor.
Usa la función map().
"""
def diplicar():
    numeros = input("escribe numeros separados por comas: ")
    numlist = list(map(int, numeros.split(",")))
    multiplicados_list = list(map(lambda x: x * 2, numlist))
    print(multiplicados_list)
#diplicar()
"""
3.
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original que
contengan la palabra objetivo.
"""
def palabras():
    palabras = input("escribe palabras separadas por espacios: ")
    palist = palabras.split(" ")
    objetivo = input("Palabra objetivo: ")
    result = []
    for p in palist:
        if objetivo == p:
            result.append(p)
        else:
            continue
    print(result)
#palabras()
"""
4.
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""
def diflist():
    list1 = list(map(int, input("Lista numeros 1 separada por comas: ").split(",")))
    list2 = list(map(int, input("Lista numeros 2 separada por comas: ").split(",")))
    print(list(map(lambda x, y: x - y, list1, list2)))
#diflist()
"""
5.
Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5).
La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado.
Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""
def medianotas():
    notas = list(map(int, input("Notas de los estudiantes separados por comas: ").split(",")))
    aproado = 5
    media = sum(notas) / len(notas)
    if media >= aproado:
        resultado = "Aprobado"
    else:
        resultado = "Suspenso"
    print(resultado, " con media de ", media )
#medianotas()
"""
6.
Escribe una función que calcule el factorial de un número de manera recursiva.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorizar():
    n = int(input("Que numero queres factorizar: "))
    resultado = factorial(n)
    print("El resultado es: ",resultado)

#factorizar()
"""
7.Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""
def cambiotuplas():
    tuplas_lista = []
    print("Escribe las tuplas separadas por comas poniendo ':)' al final para terminar")
    while True:
        tupla = input("Tupla: ")
        if tupla == ":)":
            break
        tuplas = tuple(tupla.split(","))
        tuplas_lista.append(tuplas)
    resultado = list(map(lambda t: " ".join(t), tuplas_lista))
    print(resultado)
#cambiotuplas()
"""
8.
Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera
adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""
def dividiendo():
    try:
        numero1 = float(input("Primer numero: "))
        numero2 = float(input("Segundo numero: "))
        resultado = numero1 / numero2
    except ValueError:
        print("introduce numeros")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    else:
        print("El resultado es: ", resultado)
#dividiendo()
"""
9.
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
"""
def filtro_animales():
    ilegal = ["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]
    animalesimput = input("Introduce los animales separados por comas: ").lower()
    animales = list(map(str.strip, animalesimput.split(",")))
    legal = list(filter(lambda m: m not in ilegal, animales))
    print(legal)
#filtro_animales()
"""
10.
Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza
una excepción personalizada y maneja el error adecuadamente.
"""
class errorlistavavia(Exception):
    pass
def promedio():
    lista = list(map(int, input("Lista numeros separada por comas: ").split(",")))
    try:
        if not lista:
            raise errorlistavavia("Lista VACIA no se puede calcular.")
        promedio = sum(lista) / len(lista)
        print(promedio)

    except errorlistavavia as e:
        print("error: ", e)
#promedio()
"""
11.
Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico
o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente
"""
def edad():
    try:
        edad = int(input("Edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("Edad no valida")
        print("Edad: ", edad)
    except ValueError as e:
        print("error", e)
#edad()
"""
12.
Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
"""
def frase():
    frase = input("Frease: ")
    palabras = frase.split()
    long = list(map(len, palabras))
    print(long)
#frase()
"""
13.
Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
Las letras no pueden estar repetidas. Usa la función map().
"""
def caracteres():
    caracters = set(input("Introduce un conjunto de caracteres: "))
    result = list(map(lambda x: (x.upper(), x.lower()), caracters))
    print(result)
#caracteres()

"""
14.
Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
"""
def especific():
    palabras = input("Palabras separadas por comas: ").split(",")
    letra = input("Letra inicial: ")
    palabras = [p.strip() for p in palabras]
    result = list(filter(lambda x: x.startswith(letra), palabras))
    print(result)
#especific()
"""
15.
Crea una función lambda que sume 3 a cada número de una lista dada.
"""
def suma3():
    numeros = input("Introduce numeros separados por comas; ").split(",")
    numeros = list(map(int, numeros))
    resul = list(map(lambda x: x + 3, numeros))
    print(resul)
#suma3()
"""
16.
Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras
que sean más largas que n. Usa la función filter().
"""
def palargas():
    texto = input("Introduce una frase: ")
    n = int(input("Introduce un numero entero: "))
    palabras = texto.split()
    res = list(filter(lambda palabra: len(palabra) > n, palabras))
    print("Resultado: ", res)
#palargas()
"""
17.
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572.
Usa la función reduce().
"""
def numdelist():
    numeros = input("Introduce los digitos del numero separados por espacios: ")
    lista = list(map(int, numeros.split()))
    bumero = reduce(lambda acc, digito: acc * 10 + digito, lista)
    print(bumero)
#numdelist()
"""
18.
Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter
para extraer a los estudiantes con una calificación mayor o igual a 90.
"""
def buenosestudiantes():
    estudiantes = []
    cuantosestu = int(input("Cuantos estudiantes hay: "))
    for i in range(cuantosestu):
        print("Estudiante ", i + 1)
        nombre = input("nombre: ")
        edad = int(input("Eda: "))
        nota = float(input("nota: "))
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "nota": nota
        }
        estudiantes.append(estudiante)
    aprobados = list(filter(lambda e: e["nota"] >= 90, estudiantes))
    print(aprobados)
#buenosestudiantes()
"""
19.
Crea una función lambda que filtre los números impares de una lista dada.
"""
def impares():
    entrada = input("Numeros separados por espacios: ")
    numeros = list(map(int, entrada.split()))
    impar = list(filter(lambda x: x % 2 != 0, numeros))
    print(impar)
#impares()
"""
20.
Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
"""
def filtrar():
    elementos = input("mete numeros y palabras separados por espacios: ")
    elements = []
    for e in elementos.split():
        if e.isdigit():
            elements.append(int(e))
        else:
            elements.append(e)
    enteros = list(filter(lambda x: isinstance(x, int), elements))
    print(enteros)
#filtrar()


"""
21.
Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""
def cubo():
    numero = int(input("Numero para el cubo: "))
    cubo = (lambda x: x ** 3)(numero)
    print(cubo)
#cubo()
"""
22.
Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""
def productos():
    entrada = input("numeros separados por espacios: ")
    numero = list(map(int, entrada.split()))
    produc = reduce(lambda x, y: x * y, numero)
    print(produc)
#productos()
"""
23.
Concatena una lista de palabras. Usa la función reduce().
"""
def concatpalabras():
    entrada = input("palabras separadas por espacios: ")
    palabras = entrada.split()
    resul = reduce(lambda x, y: x + y, palabras)
    print(resul)
#concatpalabras()
"""
24.
Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""
def totaldif():
    entrada = input(" numeros separados por espacios: ")
    num = list(map(int, entrada.split()))
    res = reduce(lambda x, y: x -y, num)
    print(res)
#totaldif()
"""
25.
Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""
def concar():
    text = input("introdce un texto: ")
    cant = len(text)
    print(cant)
#concar()
"""
26.
Crea una función lambda que calcule el resto de la división entre dos números dados.
"""
def resto():
    num1 = int(input("introduce un numero: "))
    num2 = int(input("introduce un segundo numero: "))
    res = (lambda x, y: x % y)(num1, num2)
    print(res)
#resto()
"""
27.
Crea una función que calcule el promedio de una lista de números.
"""
def promedio():
    entrada = input("numeros separados por espacios: ")
    numeros = list(map(float, entrada.split()))
    promedio = sum(numeros) / len(numeros)
    print(promedio)
#promedio()
"""
28.
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""
def dupe():
    entrada = input("introduce cualquier cosa separada por comas: ")
    elementos = entrada.split()
    vistos = set()
    for e in elementos:
        if e in vistos:
            print(e)
            return
        vistos.add(e)
    print("No hay dupes")
#dupe()
"""
29.
Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""
def masc():
    entrada = input("valor a enmascarar: ")
    texto = str(entrada)
    if len(texto) <= 4:
        resul = texto
    else:
        resul = "#" * (len(texto) - 4) + texto[-4:]
        print(resul)
#masc()
"""
30.
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""
def anagramas():
    pal1 = input("primera palabra: ")
    pal2 = input("segunda palabra: ")
    if sorted(pal1) == sorted(pal2):
        print("son anagramas")
    else:
        print("no son anagramas")
#anagramas()
"""
31.
Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista,
imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""
def nombre():
    entrada = input("nombres separados por eespacios: ")
    nombres = entrada.split()
    buscanombre = input("nombre que buscar: ")
    if buscanombre in nombres:
        print("se ha encontrado el nombre: ", buscanombre)
    else:
        raise ValueError("el nombre no fue encontrado")
nombre()
"""
32.
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra;
de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
"""

"""
33.
Crea una función lambda que sume elementos correspondientes de dos listas dadas.
"""

"""
34.
Crea la clase Arbol
Define un árbol genérico con un tronco y ramas como atributos.
Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
Código a seguir:

-Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
-Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
-Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
-Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
-Implementar el método quitar_rama para eliminar una rama en una posición específica.
-Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

Caso de uso:
        a. Crear un árbol.
        b. Hacer crecer el tronco una unidad.
        c. Añadir una nueva rama.
        d. Hacer crecer todas las ramas una unidad.
        e. Añadir dos nuevas ramas.
        f. Retirar la rama situada en la posición 2.
        g. Obtener información sobre el árbol.
"""

"""
35.
Crea la clase UsuarioBanco
Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
Código a seguir:

-Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
-Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
-Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
-Implementar agregar_dinero para aumentar el saldo del usuario.
Caso de uso:
        a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
        b. Agregar 20 unidades al saldo de Bob.
        c. Transferir 80 unidades de Bob a Alicia.
        d. Retirar 50 unidades del saldo de Alicia.
"""

"""
36.
Crea una función llamada procesar_texto
Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
Código a seguir:

-Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
-Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
-Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
-Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

Caso de uso:
Verificar el funcionamiento completo de procesar_texto.
"""

"""
37.
Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.
"""

"""
38.
Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
Reglas:
        0 - 69: insuficiente
        70 - 79: bien
        80 - 89: muy bien
        90 - 100: excelente
"""

"""
39.
Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y
datos (una tupla con los datos necesarios para calcular el área de la figura).
"""

"""
40.
Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
    a. Solicitar al usuario el precio original de un artículo.
    b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
    c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
    d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
    e. Mostrar el precio final de la compra, considerando o no el descuento.
    f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.
"""