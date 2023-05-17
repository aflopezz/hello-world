def hashTabla(datosA, datosB):
    n = max(max(datosA), max(datosB)) + 1
    H = [0] * n
    for id in datosA:
        H[id] += 1
    for id in datosB:
        H[id] += 1
    return n, H

def interseccion(n, H):
    R = [id for id in range(n) if H[id] == 2]
    return R

def union(n, H):
    R = [id for id in range(n) if H[id] != 0]
    return R

### PROCESO PRINCIPAL ###
archivo = open("libros-A.csv", "r")
datosA = [int(line.split(',')[0]) for line in archivo.readlines()]
archivo.close()

archivo = open("libros-B.csv", "r")
datosB = [int(line.split(',')[0]) for line in archivo.readlines()]
archivo.close()

#prueba de Funciones Solicitadas:
n, H = hashTabla(datosA, datosB)
print(f"n: {n}")
print(f"{H}")
print()

L1 = interseccion(n, H)
print(f"Interseccion:")
print(f"{L1}")
print()

L2 = union(n, H)
print(f"Union:")
print(f"{L2}")
print()

