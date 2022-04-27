import csv
from dotenv import dotenv_values

config = dotenv_values()

def pull_from_file():
    tweetIds = []
    FILE_PATH = config['FILE_PATH']
    with open(FILE_PATH) as csv_file:
        print(f'opening {FILE_PATH}')
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            tweetIds.append(row[0])
    return tweetIds


            