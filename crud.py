from parameters import  collection


def show_libro(id= None):
    if id is None:
        documents = collection.find()
        for document in documents:
            print(document)
    else:
        query = {"fecha_publicacion":id}
        document = collection.find_one(query)
        print(document)

def create_libro(libro):
    result = collection.insert_one(libro)
    print(result.inserted_id)


def update_libro(titulo, json_update):
    query = {"titulo": titulo}
    new_values = {"$set": json_update}
    result = collection.update_one(query, new_values)
    print(result.modified_count)

def delete_libro(titulo):
    query = {"titulo":titulo}
    countdlete = collection.delete_one(query)
    print("se a eliminado" + str (countdlete.deleted_count))
