import csv
tmp_data = list(csv.reader(open("C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_3.csv", newline=''), delimiter='\t'))
# tmp_data[0][0].split(' ')
#
# tmp_data[:][0].split(' ')



# for day in tmp_data:
#     print(day[0].split('Regular'))


# A[1].replace(u'\xa0', u' ')
#
# A[1].replace(u'Â', u'')
#
# A[1].replace(u'Â\xa0Â\xa0', u'')


##
# A1=tmp_data[0]
# A2=A1[0].split('Regular ')
# A3=A2.pop(0)
# A4=A3[0].replace(u'Â\xa0Â\xa0', u'')
# #'MoWeFr 10:30AM - 11:20AM TA 0202B Layla Archer 08/26/2019 - 12/11/2019 Open  <>  <>  <>'
# A5=A4.split(' ')
# #['MoWeFr', '10:30AM', '-', '11:20AM', 'TA', '0202B', 'Layla', 'Archer', '08/26/2019', '-', '12/11/2019', 'Open', '', '<>', '', '<>', '', '<>']
# num_pop = A5.index('Layla')
# del A5[num_pop::]
# A5.remove('-')
# #['MoWeFr', '10:30AM', '11:20AM', 'TA', '0202B']
# # 102,MoWe,9:00AM,10:00AM
# test=[A5[4][1:],A5[0],A5[1],A5[2]]
def sort_csv(tmp_data):
    new_data =[]
    for day in tmp_data:
        A=day
        A= A[0].split('Regular ')
        A.pop(0)
        A = A[0].replace(u'Â\xa0Â\xa0', u'')
        A = A.split(' ')
        del A[6::]
        A.remove('-')
        # test = [A5[4][1:], A5[0], A5[1], A5[2]]
        new_data.append([A[3],A[4][1:], A[0], A[1], A[2]])
    return new_data
#data = sort_csv(tmp_data)


# def room_pop(new_data, building):
#     # x = datetime.utcnow()
#     # day = datetime.strftime(x, '%a')
#     # day = day[:2]
#     # day = 'Tu'
#     today = []
#     k = -1
#     for line in new_data:
#         k = k + 1
#         print(line)
#         if building not in line[0]:
#             print(line[0])
#             #pass
#             new_data.remove(k)
#         # today.append(line)
#         else:
#             pass
#             # data.pop(k)
#             # print('%d:poped:%s' % (k, line))
#
#     return new_data

def get_building_rooms(data,building):
    return [row for row in data if building in row]


# new_data = get_building_rooms(data,'TA')
# new_data = room_pop(new_data,'TA')
# new_data = room_pop(new_data,'TA')
# new_data = room_pop(new_data,'TA')
# print(new_data)
# for item in new_data:
# #     print(new_data)
# for item in new_data:
#     if 'TA' in item:

# import csv
#
# with open('C:\\Users\\alex\\PycharmProjects\\untitled8\\findroom\\test_data_room2.csv', 'a') as csv_file:
#     csv_app = csv.writer(csv_file)
#     #csv_app.writerows(new_data)
#     for room in new_data:
#         csv_app.writerow(room[1:])
