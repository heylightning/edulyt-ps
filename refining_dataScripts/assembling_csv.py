import openpyxl
import csv

wb = openpyxl.load_workbook('assests/dict.xlsx')

data_xlsx = [
    'Sheet1'
]

for book in data_xlsx:
    sheet = wb[book]
    filename = f'./assests/maintained/dict/dict.csv'
    csv_file = open(filename, 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)

    for row in sheet.iter_rows(values_only=True):
        csv_writer.writerow(row)

    csv_file.close()

    print(f'File {filename} created successfully')
