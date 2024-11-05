def menu_inventario():
  while True:
    print("Opciones del sistema")
    print("1)Agregar producto")
    print("2)Ver inventario")
    print("3)Buscar producto")
    print("4)Salir")

    input("Por favor ingrese una opcion:")

    try:
      opcion = int(opcion)
      if 1 <= opcion <= 4:
        return opcion
      else:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número entero.")
