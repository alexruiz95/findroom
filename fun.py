
def read_data():
	import csv
	with open('/Users/admin/Desktop/test_data_room2.csv','rb') as csvfile:
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
