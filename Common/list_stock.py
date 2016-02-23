import csv
reader = csv.reader(open('../Common/companylist.csv'))

existing_stocks = {}
for row in reader:
    key = row[0]
    if key in existing_stocks:
        pass
    existing_stocks[key] = row[1]

test_stocks = {"YHOO": 35.23, "DASS": 32.00, "JOKA": 21.43}
