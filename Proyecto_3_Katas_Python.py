"""
1.
Escribe una función que reciba una cadena de texto como parámetro
y devuelva un diccionario con las frecuencias de cada letra en la cadena.
Los espacios no deben ser considerados.
"""
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
"""
3.
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original que
contengan la palabra objetivo.
"""

"""
4.
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
"""

"""
5.
Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5).
La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado.
Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.
"""

"""
6.
Escribe una función que calcule el factorial de un número de manera recursiva.
"""

"""
7.Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().
"""

"""
8.
Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera
adecuada y muestra un mensaje indicando si la división fue exitosa o no.
"""

"""
9.
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
"""

"""
10.
Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza
una excepción personalizada y maneja el error adecuadamente.
"""

"""
11.
Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico
o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente
"""

"""
12.
Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().
"""

"""
13.
Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
Las letras no pueden estar repetidas. Usa la función map().
"""

"""
14.
Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().
"""

"""
15.
Crea una función lambda que sume 3 a cada número de una lista dada.
"""

"""
16.
Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras
que sean más largas que n. Usa la función filter().
"""

"""
17.
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572.
Usa la función reduce().
"""

"""
18.
Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter
para extraer a los estudiantes con una calificación mayor o igual a 90.
"""

"""
19.
Crea una función lambda que filtre los números impares de una lista dada.
"""

"""
20.
Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().
"""

"""
21.
Crea una función que calcule el cubo de un número dado mediante una función lambda.
"""

"""
22.
Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().
"""

"""
23.
Concatena una lista de palabras. Usa la función reduce().
"""

"""
24.
Calcula la diferencia total en los valores de una lista. Usa la función reduce().
"""

"""
25.
Crea una función que cuente el número de caracteres en una cadena de texto dada.
"""

"""
26.
Crea una función lambda que calcule el resto de la división entre dos números dados.
"""

"""
27.
Crea una función que calcule el promedio de una lista de números.
"""

"""
28.
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
"""

"""
29.
Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
"""

"""
30.
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.
"""

"""
31.
Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista,
imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.
"""

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