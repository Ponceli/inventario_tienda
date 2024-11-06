def mostrar_inventario(inventario):
  """
  Muestra los productos y sus cantidades en el inventario.

  Args:
    inventario: Un diccionario donde las claves son los productos y los valores son las cantidades.
  """

  if not inventario:
    print("El inventario está vacío.")
  else:
    print("Inventario:")
    for producto, cantidad in inventario.items():
      print(f"  {producto}: {cantidad}")