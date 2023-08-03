import csv

filename = './assests/maintained/data/new_client.csv'

client_idfnew_client = []
with open(filename, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if (row[4] == 'FEMALE' and row[6] == 'MIDDLE AGED'):
            client_idfnew_client.append(row[1])

filename_newDisposition = './assests/maintained/data/new_disposition.csv'

disp_idfnew_disposition = []
with open(filename_newDisposition, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if (row[1] in client_idfnew_client):
            disp_idfnew_disposition.append(row[0])

filename_newCard = './assests/maintained/data/new_card.csv'

number_of_cards = 0
with open(filename_newCard, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if (row[1] in disp_idfnew_disposition):
            number_of_cards += 1

print(number_of_cards)
