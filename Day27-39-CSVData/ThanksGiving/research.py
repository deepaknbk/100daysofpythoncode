import collections
import csv
import os

Record = collections.namedtuple(
    'Record',
    'RespondentID,HouseholdIncome,USRegion,Menu'
)

def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'thanksgiving.csv')
    data =[]
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            record=parse_row(row)
            data.append(record)
        print(data)

def parse_row(row):
    record = Record(
        row['RespondentID'], \
        row['How much total combined money did all members of your HOUSEHOLD earn last year?'], \
        row['US Region'], \
        row['Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots']
    )
    return record