ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1000.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 20.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1000.0},
    {"fecha": "2024-01-02", "producto": "Teclado", "cantidad": 3, "precio": 50.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 20.0}
]


ingresos_totales = 0

#for venta in ventas:
#    ingresos_totales += venta["cantidad"] * venta["precio"]

#print("Ingresos totales:", ingresos_totales)

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

print(ventas_por_producto)


producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad:", ventas_por_producto[producto_mas_vendido])

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]

    if producto in precios_por_producto:
        suma, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (suma + precio * cantidad, total_cantidad + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)


promedios = {}

for producto, (suma, cantidad) in precios_por_producto.items():
    promedios[producto] = suma / cantidad

print(promedios)

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print(ingresos_por_dia)

resumen_ventas = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingreso = cantidad * venta["precio"]

    if producto not in resumen_ventas:
        resumen_ventas[producto] = {
            "cantidad_total": 0,
            "ingresos_totales": 0
        }

    resumen_ventas[producto]["cantidad_total"] += cantidad
    resumen_ventas[producto]["ingresos_totales"] += ingreso

# agregar precio promedio
for producto in resumen_ventas:
    resumen_ventas[producto]["precio_promedio"] = (
        resumen_ventas[producto]["ingresos_totales"] /
        resumen_ventas[producto]["cantidad_total"]
    )

print(resumen_ventas)