import csv
from read_other import sort_csv
from read_other import get_building_rooms

tmp_data = list(csv.reader(open("C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_3.csv", newline=''), delimiter='\t'))


data = sort_csv(tmp_data)
new_data = get_building_rooms(data,'TA')

import csv

with open('C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_room2.csv', 'a',newline='') as csv_file:
    csv_app = csv.writer(csv_file)
    #csv_app.writerows(new_data)
    for room in new_data:
        csv_app.writerow(room[1:])

