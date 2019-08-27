
def read_data():
	import csv
	with open('/Users/admin/Desktop/findroom/test_data_room2.csv','rb') as csvfile:
#		data = list(csv.reader(csvfile))
		return list(csv.reader(csvfile))
	#	return data
	#print(data)
	# return data


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

rooms = []
for i in range(1,len(data)):
	rooms.append(data[i][0])
#return rooms

rooms.sort()


def appointments_v2(data_date):
	for i in range(1,len(data_date)):
		data_date[i].append((data_date[1][2],data_date[1][3]))
	return appointments




 









