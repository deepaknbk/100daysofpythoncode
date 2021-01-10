import csv
import os
import collections

Record = collections.namedtuple(
    'Record',
    'date,actual_mean_temp,actual_min_temp,actual_max_temp,'
    'average_min_temp,average_max_temp,record_min_temp,record_max_temp,'
    'record_min_temp_year,record_max_temp_year,actual_precipitation,'
    'average_precipitation,record_precipitation'
)

data=[]

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record=parse_row(row)
            data.append(record)
    print(data)



def parse_row(row):
    row['actual_max_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['actual_precipitation'] = float(row['actual_precipitation'])

    record = Record(
        **row
    )
    return record

def get_hottest_days():
    pass