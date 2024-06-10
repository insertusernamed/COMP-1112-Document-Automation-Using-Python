import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Defining the scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Adding service account file
creds = ServiceAccountCredentials.from_json_keyfile_name("./key.json", scope)

# Authorizing the client
client = gspread.authorize(creds)

# Opening a Google Sheet
sheet = client.open("Example Spreadsheet 2").sheet1

# Writing data to specific cells
sheet.update_cell(1, 1, "Updated Value")
print("Updated cell (1, 1)")

# Adding a new row of data
new_row = ["New", "Row", "Data"]
sheet.append_row(new_row)
print("Added new row:", new_row)

# Writing a list of lists to the sheet
data = [
    ["Name", "Age", "City"],
    ["Daniel", 19, "Cookstown"],
    ["Jenna", 19, "Barrie"],
    ["Christian", 24, "Beeton"],
]
for row in data:
    sheet.append_row(row)
print("Appended multiple rows of data")
