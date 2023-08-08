import csv

filename = './assests/maintained/district.csv'
districtList_districtCSV = []
with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[14] == 'A15' or row[14] == '?'):
            pass
        else:
            if (int(row[14]) > 6000):
                districtList_districtCSV.append(int(row[0]))

filename_newAccount = './assests/maintained/new_account.csv'
accountList_newAccountCSV = []
with open(filename_newAccount, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[1] == 'district_id'):
            pass
        else:
            if (int(row[1]) in districtList_districtCSV):
                accountList_newAccountCSV.append(row[0])

filname_loan = './assests/maintained/loan.csv'
numLoanList = 0
with open(filname_loan, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[1] == 'account_id'):
            pass
        else:
            if (row[1] in accountList_newAccountCSV):
                numLoanList += 1

print(numLoanList)
