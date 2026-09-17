from application.medisync_app import MediSyncApp


def main():
    print("A ligar ao MediSync CORBA Server...")

    app = MediSyncApp()

    try:
        print("CORBA conectado com sucesso.")

        patients = app.list_patients()

        print(f"\nPacientes registados: {len(patients)}")

        for patient in patients:
            print(
                f"- ID: {patient.id} | "
                f"Nome: {patient.fullName}"
            )

        print("\nTamanho actual da fila:")
        print(app.get_queue_size())

        appointments = app.list_appointments()

        print(
            "\nConsultas registadas:",
            len(appointments),
        )

    finally:
        app.close()


if __name__ == "__main__":
    main()