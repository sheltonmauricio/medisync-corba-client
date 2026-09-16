from corba_client import CorbaClient
from services.patient_service import PatientService
from services.queue_service import QueueService


def main():
    print("A ligar ao MediSync CORBA Server...")

    client = CorbaClient()

    hello_service = client.get_hello_service()

    print("CORBA conectado com sucesso.")
    print("Resposta do servidor:", hello_service.sayHello())

    patient_service = PatientService(client)
    queue_service = QueueService(client)

    patients = patient_service.list_patients()

    print(f"\nPacientes registados: {len(patients)}")

    for patient in patients:
        print(f"- ID: {patient.id} | Nome: {patient.fullName}")

    print("\nA adicionar pacientes à fila...")

    queue_service.add_to_queue(1)
    queue_service.add_to_queue(2)

    print(
        "Tamanho da fila:",
        queue_service.get_queue_size(),
    )

    next_patient = queue_service.get_next_patient()

    print("Próximo paciente:", next_patient)

    print(
        "Tamanho da fila após atendimento:",
        queue_service.get_queue_size(),
    )

    client.close()


if __name__ == "__main__":
    main()