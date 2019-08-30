import csv
from read_other import sort_csv
from read_other import get_building_rooms

tmp_data = list(csv.reader(open("C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_3.csv", newline=''), delimiter='\t'))


data = sort_csv(tmp_data)
new_data = get_building_rooms(data,'TA')

import csv

with open('C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\rooms_unsure.csv', 'a',newline='') as csv_file:
    csv_app = csv.writer(csv_file)
    #csv_app.writerows(new_data)
    for room in new_data:
        csv_app.writerow(room[1:])

import pandas as pd

# this opens the csv and removes duplicates
df = pd.read_csv('C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\rooms_unsure.csv')
df.drop_duplicates(inplace=True)
df.to_csv('C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\rooms_unsure.csv', index=False)