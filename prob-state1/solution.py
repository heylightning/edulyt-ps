import csv

filename = './assests/maintained/district.csv'
districtList = []
districtOBJ = {}
with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[2] == 'Prague'):
            districtOBJ = {
                'district_id': row[0],
                'region': row[2],
            }
            districtList.append(districtOBJ)
        elif (row[2] == 'south Moravia' or row[2] == 'north Moravia'):
            districtOBJ = {
                'district_id': row[0],
                'region': row[2],
            }
            districtList.append(districtOBJ)

filename_newAccount = './assests/maintained/new_account.csv'
newAccountList = []
newAccountOBJ = {}
with open(filename_newAccount, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        newAccountOBJ = {
            'account_id': row[0],
            'district_id': row[1],
        }
        newAccountList.append(newAccountOBJ)

temp = []
f1List = [
    ['account_id', 'district_id', 'region']
]
for running in newAccountList:
    for jogging in districtList:
        if (running['district_id'] == jogging['district_id']):
            temp = [
                running['account_id'],
                running['district_id'],
                jogging['region']
            ]
            f1List.append(temp)
            temp = []

transactionOBJ = {}
transactionList = []
filename_transaction = './assests/maintained/new_transaction.csv'
month = [
    'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
    'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
]


def getMonth(monthNum):
    return month[int(monthNum) - 1]


with open(filename_transaction, 'r', newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        if (row[3] == 'CREDIT'):
            monthNum = str(row[2])[2:4]
            monthName = getMonth(monthNum)
            transactionOBJ = {
                'account_id': row[1],
                'month': monthName,
                'amount': row[5],
            }
            transactionList.append(transactionOBJ)

f2List = []
temp = []

for a in range(len(transactionList)):
    for b in range(len(f1List)):
        if (transactionList[a]['account_id'] == f1List[b][0]):
            temp = [
                transactionList[a]['account_id'],
                f1List[b][2],
                transactionList[a]['month'],
                transactionList[a]['amount'],
            ]
            f2List.append(temp)
            temp = []

scripted_dataFilename = './assests/scripted_data/prob_state1.csv'

with open(scripted_dataFilename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['account_id', 'region', 'month', 'amount'])
    for row in f2List:
        csv_writer.writerow(row)

print(f'File {scripted_dataFilename} created successfully')
