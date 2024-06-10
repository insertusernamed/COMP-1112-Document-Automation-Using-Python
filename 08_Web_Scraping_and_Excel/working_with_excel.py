import openpyxl
import os

# changing the working directory to the current file's directory so that the excel files will be created in the same directory as the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create a new Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Data"

# Write data to the Excel sheet
data = [
    ["Name", "Age", "City"],
    ["Daniel", 19, "Cookstown"],
    ["Jenna", 19, "Barrie"],
    ["Christian", 24, "Beeton"],
]

for row in data:
    sheet.append(row)

# Save the workbook
workbook.save("example.xlsx")

# Read data from an Excel file
workbook = openpyxl.load_workbook("example.xlsx")
sheet = workbook["Data"]

# Print the contents of the sheet
for row in sheet.iter_rows(values_only=True):
    print(row)

# Modify data in the Excel sheet
sheet["B2"] = 20  # Change Daniel's age from 19 to 20

# Save the modified workbook
workbook.save("example_modified.xlsx")
