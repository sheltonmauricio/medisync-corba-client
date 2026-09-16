from corba_client import CorbaClient
from services.patient_service import PatientService
from services.appointment_service import AppointmentService


def main():
    print("A ligar ao MediSync CORBA Server...")

    client = CorbaClient()

    hello_service = client.get_hello_service()

    print("CORBA conectado com sucesso.")
    print("Resposta do servidor:", hello_service.sayHello())

    patient_service = PatientService(client)
    appointment_service = AppointmentService(client)

    patients = patient_service.list_patients()

    print(f"\nPacientes registados: {len(patients)}")

    for patient in patients:
        print(f"- ID: {patient.id} | Nome: {patient.fullName}")

    appointment = appointment_service.schedule_appointment(
        1,
        "Dr. Carlos",
        "2026-09-20 09:00",
        "Clínica Geral",
    )

    print("\nConsulta agendada:")
    print(f"ID: {appointment.id}")
    print(f"Paciente ID: {appointment.patientId}")
    print(f"Médico: {appointment.doctor}")
    print(f"Data: {appointment.appointmentDate}")
    print(f"Especialidade: {appointment.specialty}")

    appointments = appointment_service.list_appointments()

    print(f"\nTotal de consultas: {len(appointments)}")

    client.close()


if __name__ == "__main__":
    main()