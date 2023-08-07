# This is used for re-structuring data for faster compiling and processing.

import openpyxl
import csv

wb = openpyxl.load_workbook('assests/main.xlsx')

data_xlsx = [
    'New_Account', 'New_Card', 'District', 'Loan',
    'New_Client', 'New_Disposition', 'New_Transaction', 'Order'
]

for book in data_xlsx:
    sheet = wb[book]
    filename = f'./assests/maintained/{book.lower()}.csv'
    csv_file = open(filename, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    for row in sheet.iter_rows(values_only=True):
        csv_writer.writerow(row)

    csv_file.close()

    print(f'File {filename} created successfully')
