contatos = {
    "Eddard Stark":{
        "Celular":"123456",
        "email":"ned@winterfell.com"
    },
    "Jon Snow":{
        "Celular":"123654",
        "email":"ghost@watcher.com"
    }
}


for contato in contatos:
    print(f"{contato}: ")
    for cont, valor in contatos[contato].items():
        print(f"{cont} -- {valor}")
    print("\n")