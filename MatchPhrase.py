import csv

counter = 0
with open('iowa-liquor-sample.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        # check if 'single malt scotch' is in the category or description
        if row[11].lower() == "single malt scotch" or row[15].lower().find("single malt scotch") != -1:
            counter += 1
# print number of records with an occurrence of 'single malt scotch'
print counter
