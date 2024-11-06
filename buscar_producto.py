def buscar_producto(inventario, producto_buscado):
  """
  Busca un producto en un inventario y muestra su cantidad.

  Args:
    inventario: Un diccionario que representa el inventario.
    producto_buscado: El nombre del producto a buscar.
  """

  if producto_buscado in inventario:
    print(f"La cantidad de {producto_buscado} es: {inventario[producto_buscado]}")
  else:
    print(f"{producto_buscado} no se encuentra en el inventario.")