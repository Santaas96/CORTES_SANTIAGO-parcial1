from funciones import *

def desplegar_menu():
  """Muestra el menú principal."""
  print(f"\n-------------- Menu Parcial 1 --------------\n")
  print(f"1. Cargar archivo csv ingresando el nombre")
  print(f"2. Imprimir datos de los posts")
  print(f"3. Asignar estadisticas")
  print(f"4. Filtrar por mejores posts")
  print(f"5. Filtrar por haters")
  print(f"6. Informar promedio de followers")
  print(f"7. Ordenar los datos por nombre de user ascendente")
  print(f"8. Mostrar más popular")
  print(f"9. Salir del programa")
  print(f"\n-------------------------------------------------------\n")

posts = []

def main():
  while True:
    desplegar_menu()
    opcion_elegida = input("Seleccionar una opción: ").lower()

    match opcion_elegida:
      case "1":
        nombre_archivo = input("Selecciona nombre del archivo: ")
        cargar_csv(nombre_archivo, lambda archivo: crear_lista_posts(archivo, posts))
      case "2":
        aviso_sin_archivo_cargado(posts, imprimir_tabla_posts)
      case "3":
        aviso_sin_archivo_cargado(posts, asignar_valores)
      case "4":
        aviso_sin_archivo_cargado(posts, filtrar_mejores_en_csv)
      case "5":
        aviso_sin_archivo_cargado(posts, filtrar_haters_en_csv)
      case "6":
        aviso_sin_archivo_cargado(posts, mostrar_promedio_followers)
      case "7":
        aviso_sin_archivo_cargado(posts, guardar_users_ordenados_json)
      case "8":
        aviso_sin_archivo_cargado(posts, mostrar_mas_popular)
      case "9":
        break

main()