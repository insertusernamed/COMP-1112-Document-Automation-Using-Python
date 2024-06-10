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

# Reading and printing all values in the sheet
all_values = sheet.get_all_values()
print("All values in the sheet:")
print(all_values)

# Reading and printing specific rows, columns, and cells
first_row = sheet.row_values(1)
print("First row:", first_row)

first_column = sheet.col_values(1)
print("First column:", first_column)

# Note: 2,1 means row 2, column 1. The format is (row, column)
specific_cell = sheet.cell(2, 1).value
print("Value of cell (2, 1):", specific_cell)
