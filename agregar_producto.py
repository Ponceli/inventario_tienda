def agregar_producto_inventario(inventario):
  """
  Agrega un producto al inventario, verificando que la cantidad sea positiva.

  Args:
    inventario: Un diccionario que representa el inventario.

  Returns:
    El diccionario de inventario actualizado.
  """

  nombre_producto = input("Ingrese el nombre del producto: ")
  cantidad = int(input("Ingrese la cantidad del producto: "))

  # Verificamos que la cantidad sea positiva
  if cantidad > 0:
    inventario[nombre_producto] = cantidad
    print(f"Producto '{nombre_producto}' agregado al inventario con {cantidad} unidades.")
  else:
    print("La cantidad debe ser un número positivo.")

  return inventario

# Ejemplo de uso:
mi_inventario = {}
mi_inventario = agregar_producto_inventario(mi_inventario)