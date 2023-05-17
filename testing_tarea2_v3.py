def cargar_datos(ruta_archivo):
    datos = {}
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            id_libro, nombre_libro, autor, anio = linea.strip().split(',')
            datos[int(id_libro)] = [nombre_libro, autor, anio]
    return datos

def hashTabla(datosA, datosB):
    n = max(max(datosA.keys()), max(datosB.keys())) + 1
    H = [0] * n
    for id in datosA:
        H[id] += 1
    for id in datosB:
        H[id] += 1
    return n, H

def interseccion(n, H, datosA, datosB):
    R = []
    for id in range(n):
        if H[id] == 2:
            info_libro = datosA[id] if id in datosA else datosB[id]
            R.append([id] + info_libro)
    return R

def union(n, H, datosA, datosB):
    R = []
    for id in range(n):
        if H[id] != 0:
            info_libro = datosA[id] if id in datosA else datosB[id]
            R.append([id] + info_libro)
    return R

### PROCESO PRINCIPAL ###
datosA = cargar_datos("libros-A.csv")
datosB = cargar_datos("libros-B.csv")

n, H = hashTabla(datosA, datosB)
print(f"n: {n}")
print(f"{H}")
print()

L1 = interseccion(n, H, datosA, datosB)
print(f"Interseccion:")
for libro in L1:
    print(libro)
print()

L2 = union(n, H, datosA, datosB)
print(f"Union:")
for libro in L2:
    print(libro)
print()
