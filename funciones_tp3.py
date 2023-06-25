from data_stark import *
import re
import os

############ PUNTO 1 #############


def extraer_iniciales(nombre_heroe: str):
    iniciales = []

    nombre_heroe = nombre_heroe.replace("-", " ")
    nombre_heroe = nombre_heroe.replace("the", "")
    individual = nombre_heroe.split()

    for elemento in individual:
        elemento.lower()
        inicial = elemento[0].upper()

        iniciales.append(inicial)
    iniciales_string = ".".join(iniciales) + "."

    return iniciales_string


def definir_iniciales_nombre(heroe, iniciales):
    iniciales = extraer_iniciales(heroe["nombre"])
    heroe['iniciales'] = iniciales

    if type(heroe) == dict:
        if "nombre" in heroe:
            return True

    else:
        return False


def agregar_iniciales_nombre(lista_heroes):
    if type(lista_heroes) == list:
        if len(lista_heroes) > 0:

            for heroe in lista_heroes:
                if definir_iniciales_nombre(heroe["nombre"]) == True:
                    return True
                else:
                    print("El origen de datos no contiene el formato correcto")
                    return False

        else:
            return False
    else:
        return False


def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    if type(lista_heroes) == list:
        if len(lista_heroes) > 0:

            for heroe in lista_heroes:
                iniciales = extraer_iniciales(heroe["nombre"])
                definir_iniciales_nombre(heroe, iniciales)

                nombre = heroe['nombre']
                iniciales = heroe['iniciales']

                print(f"* {nombre} ({iniciales})")


############ PUNTO 2 #############

def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    if (type(id_heroe) == int) and (genero_heroe == "NB" or genero_heroe == "F" or genero_heroe == "M" and genero_heroe != " "):
        str_genero = f"{genero_heroe} - {id_heroe}"
        return str_genero
    else:
        print("N/A")


def agregar_codigo_heroe(heroe: dict, id_heroe: int):
    genero = heroe['genero']
    id = generar_codigo_heroe(id_heroe, genero)
    heroe['codigo_heroe'] = id
    return True


def stark_generar_codigos_heroes(lista_heroes: list):
    id = 1
    for heroe in lista_heroes:
        id += 1
        agregar_codigo_heroe(heroe, id)
    print(f"se asignaron {id} codigos")

    primer_heroe = lista_heroes[0]
    ultimo_heroe = lista_heroes[-1]
    print(f"El código del primer héroe es: {primer_heroe['codigo_heroe']}")
    print(f"El código del último héroe es: {ultimo_heroe['codigo_heroe']}")


############ PUNTO 3 #############

def sanitizar_entero(numero_str: str):

    numero_str = numero_str.strip()

    no_numerico = re.compile(r"\D+$")
    match = no_numerico.search(numero_str)

    if match:
        return -1
    else:
        numero = int(numero_str)
        if numero < 0:
            return -2
        else:
            return numero


def sanitizar_flotante(numero_str: str):
    numero_str = numero_str.strip()

    no_numerico = re.compile(r"\D+$")
    match = no_numerico.search(numero_str)

    float_str = re.compile(r"\d+\.\d+")
    match_float = float_str.search(numero_str)

    negativo = re.compile("^[-]")
    match_neg = negativo.search(numero_str)

    if match:
        return -1
    elif match_neg:
        return -2
    else:
        if match_float:
            numero_str = float(numero_str)
            return numero_str
        else:
            try:
                numero_str = int(numero_str)
                return numero_str
            except:
                return -3


def sanitizar_string(valor_str: str, valor_por_defecto: str):
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    if valor_por_defecto == "":
        valor_por_defecto = "-"

    digit = re.compile(r"\d")
    match_digit = digit.search(valor_str)

    barra = re.compile(r"\/")
    match_barra = barra.search(valor_str)

    if match_barra:
        valor_str.replace("/", " ")

    if valor_str == "" and valor_por_defecto != "":
        minuscula = valor_por_defecto.lower()
        return minuscula

    if match_digit:
        return "N/A"
    else:
        minuscula = valor_str.lower()
        return minuscula


def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:

    sanitizacion = False

    tipo_dato = tipo_dato.lower()

    if not (tipo_dato == "string" or tipo_dato == "entero" or tipo_dato == "flotante" or type(tipo_dato) == str):
        sanitizacion = False
        print("tipo de dato no reconocido")

    if clave not in heroe:
        sanitizacion = False
        print("La clave especificada no existe en el héroe")

    elif tipo_dato == "entero":
        heroe[clave] = sanitizar_entero(heroe[clave])
        sanitizacion = True
    elif tipo_dato == "flotante":
        heroe[clave] = sanitizar_flotante(heroe[clave])
        sanitizacion = True
    else:
        heroe[clave] = sanitizar_string(heroe[clave], "")
        sanitizacion = True

    return sanitizacion


def stark_normalizar_datos(lista_heroes: list) -> None:
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "string")
            sanitizar_dato(heroe, "color_pelo", "string")
            sanitizar_dato(heroe, "fuerza", "entero")
            sanitizar_dato(heroe, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("ERROR: Lista de heroes vacia")


############ PUNTO 4 #############

def generar_indice_nombres(lista_heroes: list):
    lista_palabra = []
    for heroe in lista_heroes:
        nombre_heroe = str(heroe["nombre"])
        individual = nombre_heroe.split()
        lista_palabra.extend(individual)
    return lista_palabra


def stark_imprimir_indice_nombre(lista_heroes):
    lista = generar_indice_nombres(lista_heroes)
    indice = '-'.join(lista)
    print(indice)


############ PUNTO 5 #############
def convertir_cm_a_mtrs(valor_cm: float):
    if valor_cm > 0:
        valor_mtrs = valor_cm/100
        return valor_mtrs
    else:
        return -1


def generar_separador(patron: str, largo: int, imprimir=True):

    if (len(patron) < 1 or len(patron) > 2) or (largo < 1 or largo > 235):
        return "N/A"

    separador = patron * largo

    if imprimir == False:
        return separador
    else:
        print(separador)


def generar_encabezado(titulo: str):
    generar_separador("*", 115)
    titulo = titulo.upper()
    print(titulo)
    generar_separador("*", 115)


def stark_codigos_heroes(lista_heroes: list):
    id = 0
    for heroe in lista_heroes:
        id += 1
        genero = heroe['genero']
        codigo = f"{genero} - {id}"
        heroe['codigo_heroe'] = codigo


stark_codigos_heroes(lista_personajes)


def imprimir_ficha_heroe(heroe: dict):
    nombre = heroe["nombre"]
    identidad = heroe["identidad"]
    empresa = heroe["empresa"]
    codigo = heroe["codigo_heroe"]
    altura = heroe["altura"]
    peso = heroe["peso"]
    genero = heroe["genero"]
    color_ojos = heroe["color_ojos"]
    color_pelo = heroe["color_pelo"]
    fuerza = heroe["fuerza"]

    generar_encabezado("principal")

    print(f"NOMBRE DEL HEROE: {nombre} ({extraer_iniciales(nombre)})")
    print(f"IDENTIDAD SECRETA: {identidad}")
    print(f"CONSULTORA: {empresa}")
    print(f"CODIGO HEROE: {codigo}")
    generar_encabezado("principal")
    print(f"ALTURA: {altura}")
    print(f"PESO: {peso}")
    print(f"FUERZA: {fuerza}")
    generar_encabezado("señas particuñares")
    print(f"COLOR DE OJOS: {color_ojos}")
    print(f"COLOR DE PELO: {color_pelo}")


def stark_navegar_fichas(lista_heroes: list):
    i = 0

    while True:

        heroe = lista_heroes[i]
        imprimir_ficha_heroe(heroe)

        print(" ")
        print("Opciones:")
        print("1. Héroe anterior")
        print("2. Siguiente héroe")
        print("S. Salir")
        print(" ")

        opcion = int(input("Ingrese el número de opción: "))
        print(" ")

        if opcion == 1:
            i -= 1
            if i < 0:
                i = len(lista_heroes) - 1
        elif opcion == 2:
            i += 1
            if i >= len(lista_heroes):
                i = 0
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.\n")

        imprimir_ficha_heroe(heroe)


############ PUNTO 6 #############
def imprimir_menu():
    print("""

1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir

____________________________________________________________

""")


def stark_menu_principal() -> str:
    imprimir_menu()
    opcion = input("ingrese una opcion: ")
    return opcion


def stark_marvel_app_3(lista: list):
    while True:
        os.system("cls")
        opcion = stark_menu_principal()
        if opcion == "1":
            stark_imprimir_nombres_con_iniciales(lista)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista)
        elif opcion == "3":
            stark_normalizar_datos(lista)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista)
        elif opcion == "5":
            stark_navegar_fichas(lista)
        elif opcion == "S" or opcion == "s":
            break
        os.system("pause")
