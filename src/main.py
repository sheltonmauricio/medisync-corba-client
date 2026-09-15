from corba_client import connect


def main():
    print("A ligar ao MediSync CORBA Server...")

    orb, hello_service = connect()

    print("CORBA conectado com sucesso.")
    print("Resposta do servidor:", hello_service.sayHello())

    orb.destroy()


if __name__ == "__main__":
    main()