import csv
from dotenv import dotenv_values
import os
import random

config = dotenv_values()

def file_collector():
    path = config['FILE_PATH']
    month = 2
    start_day = 22 
    end_day = 29 
    sample_size = 0.1
    start = 1
    
    full_ids = []
    for day in range(start_day, end_day):
        if day < 10:
            day = '0' + str(day)
        days_ids = []
        date = f'2022-0{month}-{day}'
        directory = path + date + '/' 
        files = next(os.walk(directory))[2]
        for f in files:
            if '.DS_Store' in f:
                files.remove(f)
        for i in range(start, len(files) + 1):
            full_path = directory + date + '_' + str(i) + '.csv'
            ids = pull_from_file(full_path)
            days_ids = days_ids + ids
        days_ids = random.sample(days_ids, int(len(days_ids) * sample_size))
        full_ids = full_ids + days_ids

    return full_ids


def pull_from_file(FILE_PATH):
    tweetIds = []
    with open(FILE_PATH) as csv_file:
        print(f'opening {FILE_PATH}')
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            tweetIds.append(row[0])
    return tweetIds



            