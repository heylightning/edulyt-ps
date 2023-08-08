import csv

filename = './assests/maintained/district.csv'
districtList_districtCSV = []
with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[10] == 'A11'):
            pass
        else:
            if (int(row[10]) > 9000):
                districtList_districtCSV.append(int(row[0]))

filename_newClient = './assests/maintained/new_client.csv'
clientList_newClientCSV = []
with open(filename_newClient, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[3] == 'district_id'):
            pass
        else:
            if (int(row[3]) in districtList_districtCSV):
                clientList_newClientCSV.append(row[1])

filename_newDisposition = './assests/maintained/new_disposition.csv'
dispositionList_newDispositionCSV = []
with open(filename_newDisposition, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[1] == 'client_id'):
            pass
        else:
            if (row[1] in clientList_newClientCSV):
                dispositionList_newDispositionCSV.append(row[0])

filename_newCard = './assests/maintained/new_card.csv'
numCard = 0
with open(filename_newCard, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[1] == 'disp_id'):
            pass
        else:
            if (row[1] in dispositionList_newDispositionCSV):
                numCard += 1

print(numCard)
