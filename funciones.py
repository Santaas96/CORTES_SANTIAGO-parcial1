import json
import random
from utiles import filter_list, get_current_path, map_list, reduce_list, sort_list

def aviso_sin_archivo_cargado(lista: list, funcion) -> None:
  """_summary_

  Args:
    lista (list): Lista a procesar si esta misma no esta vacia
    funcion (func): Funcion que procesa al lista si no esta vacia
  """
  if len(lista) > 0:
    funcion(lista)
  else:
    print("\n********** No olvides cargar el archivo primero **********")

def crear_lista_posts(archivo, lista_objetivo: list) -> None:
  """_summary_

  Args:
    archivo (file): Archivo csv abierto
    lista_objetivo (list): Lista vacia para popular con datos del archivo abierto
  """
  for linea in archivo:
    usuario = {}
    linea = linea.strip("\n").split(",")
    id, user, likes, dislikes, followers = linea
    usuario["id"] = int(id)
    usuario["user"] = user
    usuario["likes"] = int(likes)
    usuario["dislikes"] = int(dislikes)
    usuario["followers"] = int(followers)
    lista_objetivo.append(usuario)
  print("\n Archivo Cargado Exitosamente!\n")

def cargar_csv(ruta: str, procesadora_archivo) -> None:
  """_summary_

  Args:
    ruta (str): Ruta para abrir archivo csv
    procesadora_archivo (func): Funcion procesadora de los datos del archivo abierto
  """
  with open(get_current_path(ruta), "r", encoding="utf-8") as csv:
    encabezado = csv.readline().strip("\n").split(",")
    procesadora_archivo(csv)

def mostrar_usuario(usuario: dict) -> None:
  """_summary_

  Args:
    usuario (str): Diccionario de usuario para mostrar en consola
  """
  print(f'{usuario["id"]:3}\t{usuario["user"]:10}\t{usuario["likes"]:5}\t{usuario["dislikes"]:5}\t{usuario["followers"]:5}')

def imprimir_tabla_posts(lista: list) -> None:
  """_summary_

  Args:
    lista (str): Lista de Diccionarios de usuario para mostrar en consola
  """
  print("\n   ***Lista datos de posts por usuario***\n")
  print("  ID    Usuario            Likes Dislikes Followers")
  print("----------------------------------------------------")
  for i in range(len(lista)):
    mostrar_usuario(lista[i])
  print()

def generar_valor_aleatorio(desde: int, hasta: int) -> int:
  """_summary_

  Args:
    desde (int): Entero desde donde se calculara el numero random
    hasta (int): Entero hasta donde se calculara el numero random
  Returns:
      int: Entero random entre los datos indicados
  """
  return random.randint(desde, hasta)

def asignar_valores(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de usuarios para posteriormente asignarles valores random
  """
  for item in lista:
    item["likes"] = generar_valor_aleatorio(500, 3000)
    item["dislikes"] = generar_valor_aleatorio(300, 3500)
    item["followers"] = generar_valor_aleatorio(10000, 20000)
  print("\n Valores Asignados Exitosamente!\n")

def crear_nuevo_csv(datos: list, nombre_nuevo_archivo: str) -> None:
  """_summary_

  Args:
    datos (list): Lista de diccionarios para guardar en csv
    nombre_nuevo_archivo (str): Nombre del nuevo archivo csv a crear
  """
  with open(get_current_path(nombre_nuevo_archivo), "w", encoding="utf-8") as csv:
    separacion = ","
    csv.write(f"{separacion.join(list(datos[0].keys()))}\n")
    for item in datos:
      valores_item = list(item.values())
      for i in range(len(valores_item)):
        if isinstance(valores_item[i], int) or isinstance(valores_item[i], float):
          valores_item[i] = str(valores_item[i])
      csv.write(f"{separacion.join(valores_item)}\n")

def filtrar_mejores_en_csv(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para filtrar por mas likeados y guardar en csv
  """
  lista_filtrada = filter_list(lambda user: user["likes"] > 2000, lista)
  crear_nuevo_csv(lista_filtrada, "mejores_posts.csv")
  print("\n Archivo Generado Exitosamente!\n")

def filtrar_haters_en_csv(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para filtrar por mas hateados y guardar en csv
  """
  lista_filtrada = filter_list(lambda user: user["likes"] < user["dislikes"], lista)
  crear_nuevo_csv(lista_filtrada, "haters.csv")
  print("\n Archivo Generado Exitosamente!\n")

def calcular_promedio(lista: list, campo: str) -> float:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para calcular el promedio de uno de sus campos
    campo (str): Campo al que se le va a calcular el promedio
  Returns:
    float: Flotante fruto del calculo del promedio
  """
  floats_list = map_list(lambda sh: float(sh[campo]), lista)
  return reduce_list(lambda ant, act: ant + act, floats_list)

def mostrar_promedio_followers(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para mostrar su promedio de followers por usuario
  """
  promedio = calcular_promedio(lista, "followers")
  print(f"\nFollowers promedio: {round(promedio/len(lista),2)}\n")

def guardar_lista_json(lista: list, nombre_archivo: str) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para guardar en archivo json
    nombre_archivo (str): Nombre del archivo json destino
  """
  with open(get_current_path(nombre_archivo), "w", encoding="utf-8") as archivo:
    json.dump(lista, archivo, indent=2)
  print("\n Archivo Generado Exitosamente!\n")

def guardar_users_ordenados_json(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios para ordenar y posteriormente guardar en archivo json
  """
  sort_list(lambda a, b: a["user"] > b["user"], lista)
  guardar_lista_json(lista, "asc_users.json")

def calcular_mayor(lista: list, campo: str):
  """_summary_

  Args:
    lista (list): Lista de diccionarios para calcular el mayor de unos de sus campos
    campo (str): Campo al que se le va a calcular el mayor
  """
  return reduce_list(lambda ant, act: ant if float(ant[campo]) > float(act[campo]) else act, lista)

def mostrar_mas_popular(lista: list) -> None:
  """_summary_

  Args:
    lista (list): Lista de diccionarios en donde se va a mostrar el que tenga mas likes por consola
  """
  user_posteo_mas_likes = calcular_mayor(lista, "likes")
  print(f'Usuario mas popular: {user_posteo_mas_likes["user"]} / {round(float(user_posteo_mas_likes["likes"]),2)}')


