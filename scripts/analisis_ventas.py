import pandas as pd
import matplotlib.pyplot as plt

# Lectura CSV
datos = pd.read_csv("datos/ventas.csv")

print("datos cargados: ")
print(datos.head())

# Calcular ventas totales
ventas_totales = datos["cantidad"] * datos["precio"]
datos["total"] = ventas_totales

print("\nVentas totales:")
print(datos["total"].sum())

# Producto (+) vendido
producto_mas_vendido = datos.groupby("producto")["cantidad"].sum()

print("\nProducto más vendido:")
print(producto_mas_vendido.idxmax())

# Ventas p/ producto
ventas_por_producto = datos.groupby("producto")["total"].sum()

# Grafico
ventas_por_producto.plot(kind="bar")

plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")

# Guardar gf
plt.savefig("resultados/grafico_ventas.png")

print("\nGrafico generado correctamente.")
