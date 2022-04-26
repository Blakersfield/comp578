import csv

def pull_from_file():
    tweetIds = []
    with open('/Users/giovanniflores/Development/russo_ukraine_dataset/2022-02-22/2022-02-22_1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        line_count = 0
        for row in csv_reader:
            tweetIds.append(row[0])
            line_count += 1
            if line_count == 20:
                break
    return tweetIds


 # get tweet information by id
            