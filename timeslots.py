from datetime import datetime, timedelta

def get_slots(hours, appointments, duration=timedelta(hours=1)):
    slots = sorted([(hours[0], hours[0])] + appointments + [(hours[1], hours[1])])
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
        assert start <= end, "Cannot attend all appointments"
        while start + duration <= end:
           # print("{:%H:%M} - {:%H:%M}".format(start, start + duration))
            print("{:%H:%M %p} - {:%H:%M %p}".format(start, start + duration))
            start += duration