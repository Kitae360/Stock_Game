import csv
reader = csv.reader(open('companylist.csv'))

existing_stocks = {}
for row in reader:
    key = row[0]
    if key in existing_stocks:
        pass
    existing_stocks[key] = row[1:]
