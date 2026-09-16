from corba_client import CorbaClient
from services.patient_service import PatientService


def main():
    print("A ligar ao MediSync CORBA Server...")

    client = CorbaClient()

    hello_service = client.get_hello_service()

    print("CORBA conectado com sucesso.")
    print("Resposta do servidor:", hello_service.sayHello())

    patient_service = PatientService(client)

    patient = patient_service.register_patient(
        "João Manuel",
        "2000-05-10",
        "Masculino",
        "+258 84 000 0000",
    )

    print("Paciente registado:")
    print(f"ID: {patient.id}")
    print(f"Nome: {patient.fullName}")
    print(f"Data de nascimento: {patient.birthDate}")
    print(f"Género: {patient.gender}")
    print(f"Telefone: {patient.phone}")

    client.close()


if __name__ == "__main__":
    main()