from search_tree import *
from Binarie_search_Tree_View import *

raiz = None

while True:
    print("Centro Educativo Naciones")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Listar estudiantes")
    print("5. Salir")

    main_menu = input("Ingrese una opción (1-5): ")

    if main_menu == "1":
        codigo = int(input("Ingrese el carnet del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        carrera = input("Ingrese el carrera del estudiante: ")
        nuevo_estudiante = Estudiante(codigo, nombre, apellido, carrera)
        raiz = insertar_estudiante(raiz, nuevo_estudiante)
        print("Estudiante insertado correctamente.")


    elif main_menu == "2":
        codigo_buscar = int(input("Ingrese el código del estudiante que desea buscar: "))
        estudiante_encontrado = buscar_estudiante(raiz, codigo_buscar)
        if estudiante_encontrado:
            print("Estudiante encontrado:")
            print("Codigo:", estudiante_encontrado.estudiante.codigo)
            print("Nombre:", estudiante_encontrado.estudiante.nombre)
            print("Apellido:", estudiante_encontrado.estudiante.apellido)
            print("Carrera:", estudiante_encontrado.estudiante.carrera)
        else:
            print("Estudiante no encontrado.")


    elif main_menu == "3":
        codigo_eliminar = int(input("Ingrese el código del estudiante a eliminar: "))
        raiz = eliminar_estudiante(raiz, codigo_eliminar)
        print("Estudiante eliminado correctamente.")

    elif main_menu == "8":
        print("\nTotal de estudiantes")
        mostrar_estudiantes(raiz)

    elif main_menu == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")

