import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Defining the scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Adding the service account file
creds = ServiceAccountCredentials.from_json_keyfile_name("./key.json", scope)

# Authorizing the client
client = gspread.authorize(creds)

# Opening a Google Sheet
sheet = client.open("Example Spreadsheet").sheet1

# Printing the first row of the sheet
print(sheet.row_values(1))
