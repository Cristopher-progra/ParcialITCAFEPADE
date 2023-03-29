from crud import *
from funcion import *
while True:
    print("================================")
    print("======MENU DE OPCIONES==========")
    print("================================")
    print("1. Consultar todos los libros:")
    print("2. Filtar por fecha publicacion:")
    print("3. Agregar un nuevo libro:")
    print("4. Modificar un libro:")
    print("5. Eliminar un libro:")
    print("6. Salir del sistema:")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        show_libro()
    elif opcion == "2":
        fecha_publicacion = input("Ingrese la fecha de publicacion: ")
        show_libro(fecha_publicacion)
    elif opcion == "3":
        libro = create_json_libro()
        create_libro(libro)
    elif opcion == "4":
        titulo = input("Ingrese el titulo del libro a modificar: ")
        libro = create_json_libro_update()
        update_libro(titulo, libro)

    elif opcion == "5":
        titulo=input('Ingresa el titulo del libro que decea eliminar:' )
        delete_libro(titulo)


    elif opcion == "6":

        break