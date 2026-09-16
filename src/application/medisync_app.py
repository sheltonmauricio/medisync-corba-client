from services.patient_service import PatientService
from services.queue_service import QueueService
from services.appointment_service import AppointmentService


class MediSyncApp:
    def __init__(self, corba_client):
        self.patient_service = PatientService(corba_client)
        self.queue_service = QueueService(corba_client)
        self.appointment_service = AppointmentService(corba_client)