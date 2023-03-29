def create_json_libro():
    titulo = input("Titulo:")
    autor = input("Autor: ")
    editorial = input("Editorial:")
    fecha_publicacion = input("Fecha Publicacion:")
    genero = input("Genero:")


    libro = {
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "fecha_publicacion": fecha_publicacion,
        "genero": genero,

    }
    return libro

def create_json_libro_update():
    print("============OPCIONES===========")
    print("1. Modificar todo el documento")
    print("2. Moficar un elemento del documento")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        return create_json_libro()
    elif opcion == "2":
        indice = input("Ingrese el indice a buscar: ")
        valor = input("Ingrese el valor a sustituir: ")
        libro = {indice: valor}
        return libro
    
    

