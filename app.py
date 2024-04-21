from google_sheet_actions import GoogleSheet
from datetime import date
import uuid

file_name_gs = "materiales-fibramax-6315a85d702f.json"
google_sheet = "prueba"
sheet_name = "Hoja"


# --------------------------------------


def generate_uid():
    # Generate a UUID
    unique_id = uuid.uuid4()
    # Convert the UUID to a string
    unique_id_str = str(unique_id)
    return unique_id_str


#Generate uid
uid = generate_uid()
#Init
google = GoogleSheet(file_name_gs, google_sheet, sheet_name)

date = date.today()
value =[["Marisso", str(date), "Quito", "lluvia", uid]]
range = google.get_last_row_range()
google.write_data(range,value)
#print(google.get_all_values())
