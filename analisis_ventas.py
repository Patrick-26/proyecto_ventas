import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del CSV
datos = pd.read_csv('ventas_productos.csv')

# Calcular el precio total por producto
datos['precio_total'] = datos['cantidad'] * datos['precio']

# Crear un gráfico de barras del precio total por producto
plt.figure(figsize=(10, 6))
plt.bar(datos['producto'], datos['precio_total'], color='skyblue')
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')
plt.savefig('precio_total_por_producto.png')
plt.show()
