def read_data():
	import csv
	with open("C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_room2.csv",newline='') as csvfile:
#		data = list(csv.reader(csvfile))
		return list(csv.reader(csvfile))