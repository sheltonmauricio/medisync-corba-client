from corba_client import CorbaClient
from application.medisync_app import MediSyncApp


def main():
    print("A ligar ao MediSync CORBA Server...")

    client = CorbaClient()

    hello_service = client.get_hello_service()

    print("CORBA conectado com sucesso.")
    print("Resposta do servidor:", hello_service.sayHello())

    app = MediSyncApp(client)

    patients = app.patient_service.list_patients()

    print(f"\nPacientes registados: {len(patients)}")

    for patient in patients:
        print(
            f"- ID: {patient.id} | "
            f"Nome: {patient.fullName}"
        )

    print(
        "\nTamanho actual da fila:",
        app.queue_service.get_queue_size(),
    )

    appointments = app.appointment_service.list_appointments()

    print(
        "Consultas registadas:",
        len(appointments),
    )

    client.close()


if __name__ == "__main__":
    main()