def cargar_datos(archivo):
    datos = {}
    with open(archivo, 'r') as f:
        for linea in f:
            id, nombre, autor, anio = linea.strip().split(',')
            datos[id] = [nombre, autor, anio]
    return datos

def hashTabla(datosA, datosB):
    # Cargamos los datos
    datosA = cargar_datos(datosA)
    datosB = cargar_datos(datosB)
    
    # Creamos los sets (tabla hash) para cada biblioteca
    hash_A = set(datosA.keys())
    hash_B = set(datosB.keys())
    
    # Unimos los sets en una sola tabla hash
    hash_total = hash_A.union(hash_B)
    
    # Retornamos el tamaño y la tabla hash
    return len(hash_total), hash_total

def interseccion(n, H):
    # Cargamos los datos
    datosA = cargar_datos('libros-A.csv')
    datosB = cargar_datos('libros-B.csv')
    
    # Creamos los sets (tabla hash) para cada biblioteca
    hash_A = set(datosA.keys())
    hash_B = set(datosB.keys())
    
    # Calculamos la intersección de los sets
    interseccion = hash_A.intersection(hash_B)
    
    # Retornamos la intersección
    return sorted(list(interseccion))

def union(n, H):
    # Retornamos la tabla hash, que ya es la unión de las dos bibliotecas
    return sorted(list(H))

# Ejemplo de uso
n, H = hashTabla('libros-A.csv', 'libros-B.csv')
print("Interseccion:", interseccion(n, H))
print("Union:", union(n, H))

