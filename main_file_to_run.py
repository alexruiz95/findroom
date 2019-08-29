from fun import read_data2
from datetime import *
import csv
from fun import appointments_v2
from fun import Remove
from fun import room_list
from fun import group_rooms
from fun import grouped_times
from timeslots import get_slots
from fun import data_date
from fun import get_data_today_new
from fun import get_data_today_pop
from fun import get_data_today
data_o = read_data2()
day = 'Mo'
data1 = get_data_today_new(data_o,day)
from datetime import *
data2 = data_date(data1)
appoint = appointments_v2(data2)
room = room_list(appoint)
room = Remove(room)
rows = appoint
grouped_rooms = group_rooms(rows,room)
grouped_time = grouped_times(grouped_rooms)
from datetime import datetime, timedelta
#hours =  (datetime(1900, 1, 1, 1, 0), datetime(1900, 1, 1, 23, 0))
hours =  (datetime(1900, 1, 1, 1, 0), datetime(1900, 1, 1, 20, 0))

i = 0
for event in grouped_time:
    print(grouped_time[i][0][0][0])
    get_slots(hours, grouped_time[i][1], duration=timedelta(hours=2))
    i = i + 1