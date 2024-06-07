def each_list(funcion_procesadora, lista: list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  for i in range(len(lista)):
    lista[i] = funcion_procesadora(lista[i])

def map_list(funcion_procesadora, lista: list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    lista_retorno.append(funcion_procesadora(element))
  return lista_retorno

# Bubble sort
def sort_list(funcion_comparadora, lista:list) -> None:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  tam = len(lista)
  for x in range(tam - 1):
    for y in range(x + 1, tam):
      if (funcion_comparadora(lista[x], lista[y])):
        aux = lista[x]
        lista[x] = lista[y]
        lista[y] = aux

# Bubble sort mapping
def sorted_map_list(funcion_comparadora, lista:list) -> list:
  lista_retorno = map_list(lambda numero: numero, lista)
  sort_list(funcion_comparadora, lista)
  return lista_retorno

def filter_list(funcion_filtradora, lista: list) -> list:
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  lista_retorno = []
  for element in lista:
    if(funcion_filtradora(element)):
      lista_retorno.append(element)
  return lista_retorno

def reduce_list(funcion_reductora, lista: list, valor_inicial = None):
  if not isinstance(lista,list):
    raise TypeError("No es una lista")
  valor = valor_inicial if valor_inicial != None else lista[0]
  start_index = 0 if valor_inicial != None else 1
  for i in range(start_index, len(lista)):
    valor = funcion_reductora(valor, lista[i])
  return valor

def get_current_path(name: str) -> str:
  import os
  return os.path.join(os.path.dirname(__file__), name)