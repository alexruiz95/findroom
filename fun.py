def read_data():
	import csv
	with open('/Users/admin/Desktop/findroom/test_data_room2.csv','rb') as csvfile:
#		data = list(csv.reader(csvfile))
		return list(csv.reader(csvfile))
	#	return data
	#print(data)
	# return data

def read_data2():
	import csv
	with open("C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_room2.csv",newline='') as csvfile:
#		data = list(csv.reader(csvfile))
		return list(csv.reader(csvfile))

# a=data[1][2]
# b=datetime.strptime(a,'%I:%M%p;)
# 	print(b)


# def conv_time(data):
# 	for i in range(1,5):
# 		data[i][2]=datetime.strptime(data[i][2],'%I:%M%p;)
from datetime import *
# for i in range(1,len(data)):
# 	data[i][2]=datetime.strptime(data[i][2],'%I:%M%p')
# 	data[i][3]=datetime.strptime(data[i][3],'%I:%M%p')
# print(data)


def data_date(data):
	for i in range(1,len(data)):
		data[i][2]=datetime.strptime(data[i][2],'%I:%M%p')
		data[i][3]=datetime.strptime(data[i][3],'%I:%M%p')
	return data


def appointments(data_date):
	appointments = []
	for i in range(1,len(data_date)):
		appointments.append((data_date[1][2],data_date[1][3]))
	return appointments

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

# # Driver Code
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(Remove(duplicate))

def room_list(data):
	rooms = []
	for i in range(1,len(data)):
		rooms.append(data[i][0])
	rooms.sort()
	return rooms




def appointments_v2(data_date):
	for i in range(1,len(data_date)):
		data_date[i].append((data_date[i][2],data_date[i][3]))
	return data_date



# def group_rooms(appointments):
#
#
#
# data  = read_data()
# from datetime import *
# data2 = data_date(data)
# appoint = appointments_v2(data2)
# room = room_list(appoint)
# rooms = Remove(room)
# rows = appoint
#
#
# all_room_times = []

# if room in
# appoint[1][4]
# 1
# for slot in appoint:
# 	for slot_num in room:
# 		if slot in room:


# all_room_times = [[]]
# rows = appoint
# arows = [row for row in rows if '102' in row]

def group_rooms(rows,room):
	group_rooms = []
	for rm in room:
		group_rooms.append([row for row in rows if rm in row])
	return group_rooms


# grouped_times = []
# for rm in room:


# arows4 = [row for row in rows for rm in room if rm in row]

# rm_times = []
# tmp = []
# for group in grouped_rooms:
# 	tmp = []
# 	for rms in group:
# 		print(rms[0])
# 		#print(rms[4])
#
# 		tmp.append(rms[4])
# 		print(tmp)
# 	print('new')
# 	rm_times.append([group,tmp])
# 	print(rm_times)
#
# rm_times[0][0]

def grouped_times(grouped_rooms):
	rm_times = []
	for group in grouped_rooms:
		tmp = []
		for rms in group:
			#print(rms[0])
			# print(rms[4])

			tmp.append(rms[4])
			#print(tmp)
		#print('new')
		rm_times.append([group, tmp])
		#print(rm_times)
	return rm_times




#
# from fun import read_data2
# from datetime import *
# import csv
# from fun import appointments_v2
# from fun import Remove
# from fun import room_list
# from fun import group_rooms
# from fun import group_times
# data  = read_data()
# from datetime import *
# data2 = data_date(data)
# appoint = appointments_v2(data2)
# room = room_list(appoint)
# room = Remove(room)
# rows = appoint
# grouped_rooms = group_rooms(rows)
# grouped_time = grouped_times(grouped_rooms)
#
# from datetime import datetime, timedelta
# hours =  (datetime(1900, 1, 1, 1, 0), datetime(1900, 1, 1, 23, 0))
# get_slots(hours, rm_times[1][0], duration=timedelta(hours=1))

