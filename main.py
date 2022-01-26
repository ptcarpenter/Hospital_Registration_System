from Dept import Department
from SLL import SLL


AE_patient_list = SLL()

AE = Department('Accident and Emergency', AE_patient_list)

# All functionality is contained within the menu
# To store patient details after treating them, enter the filename 'Patients.db' when prompted
AE.display_menu()
