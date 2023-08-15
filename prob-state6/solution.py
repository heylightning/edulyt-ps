import csv

filename = './assests/maintained/district.csv'
districtList_districtCSV = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if (row[11] == 'A12' or row[12] == 'A13' or row[11] == '?' or row[12] == '?'):
            pass
        elif (float(row[11]) > 2.0 or float(row[12]) > 2.0):
            districtList_districtCSV.append(row[0])

filename_newAccount = './assests/maintained/new_account.csv'
accountList_newAccountCSV = []
with open(filename_newAccount, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if (row[1] == 'district_id'):
            pass
        else:
            if (row[1] in districtList_districtCSV):
                accountList_newAccountCSV.append(row[0])

filename_order = './assests/maintained/order.csv'
amount = 0
with open(filename_order, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if (row[1] == 'account_id'):
            pass
        else:
            if (row[1] in set(accountList_newAccountCSV)):
                amount += float(row[4])

print(amount)
