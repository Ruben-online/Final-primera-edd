class Estudiante:
    def __init__(self, codigo, nombre, apellido, carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera


class NodoEstudiante:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None
        self.derecha = None


def insertar_estudiante(raiz, estudiante):
    if raiz is None:
        return NodoEstudiante(estudiante)
    else:
        if estudiante.codigo < raiz.producto.codigo:
            raiz.izquierda = insertar_estudiante(raiz.izquierda, estudiante)
        else:
            raiz.derecha = insertar_estudiante(raiz.derecha, estudiante)
    return raiz


def preorden(raiz):
    if raiz:
        print(raiz.producto.nombre)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)


def inorden(raiz):
    if raiz:
        inorden(raiz.izquierda)
        print(raiz.producto.nombre)
        inorden(raiz.derecha)


def postorden(raiz):
    if raiz:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.producto.nombre)


def buscar_estudiante(raiz, codigo):
    if raiz is None or raiz.estudiante.codigo == codigo:
        return raiz
    if raiz.estudiante.codigo < codigo:
        return buscar_estudiante(raiz.derecha, codigo)
    return buscar_estudiante(raiz.izquierda, codigo)


def reemplazar_nodo(raiz, codigo, nuevo_producto):
    if raiz is None:
        return None
    if raiz.producto.codigo == codigo:
        raiz.producto = nuevo_producto
    elif raiz.producto.codigo < codigo:
        raiz.derecha = reemplazar_nodo(raiz.derecha, codigo, nuevo_producto)
    else:
        raiz.izquierda = reemplazar_nodo(raiz.izquierda, codigo, nuevo_producto)
    return raiz


def eliminar_estudiante(raiz, codigo):
    if raiz is None:
        return None
    if codigo < raiz.estudiante.codigo:
        raiz.izquierda = eliminar_estudiante(raiz.izquierda, codigo)
    elif codigo > raiz.estudiante.codigo:
        raiz.derecha = eliminar_estudiante(raiz.derecha, codigo)
    else:
        if raiz.izquierda is None:
            temp = raiz.derecha
            raiz = None
            return temp
        elif raiz.derecha is None:
            temp = raiz.izquierda
            raiz = None
            return temp
        temp = encontrar_minimo(raiz.derecha)
        raiz.estudiante = temp.estudiante
        raiz.derecha = eliminar_estudiante(raiz.derecha, temp.estudiante.codigo)
    return raiz


def encontrar_minimo(raiz):
    actual = raiz
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual


def mostrar_estudiantes(raiz):
    if raiz:
        mostrar_estudiantes(raiz.izquierda)
        print("Nombre:", raiz.estudiante.nombre)
        print("Apellido:", raiz.estudiante.apellido)
        print("Carrera:", raiz.estudiante.carrera)
        mostrar_estudiantes(raiz.derecha)
