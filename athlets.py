import datetime
from tabulate import tabulate

athlets = input("Enter number of Athletes practicing: ")

players_dict = {}

def convert_tup_to_seconds(list):
    seconds_list = []
    for i in list:
        calSeconds = (i[0] * 60) + i[1]
        seconds_list.append(calSeconds)
    return seconds_list

def secs_to_MS(secs):
    return datetime.datetime.fromtimestamp(secs).strftime('%M:%S')

def calAvg(times):
    seconds_list = convert_tup_to_seconds(times)
    sum = 0
    for i in seconds_list:
        sum += i
        sec = sum/float(len(seconds_list))

    return secs_to_MS(sec)

def calMax(times):
    seconds_list = convert_tup_to_seconds(times)
    sec = max(seconds_list)
    return secs_to_MS(sec)

def calMin(times):
    seconds_list = convert_tup_to_seconds(times)
    sec = min(seconds_list)
    return secs_to_MS(sec)

for i in range(1, athlets+1):

    name = raw_input("Enter the name of Athlete " + str(i) + ": ")


    times = []
    while True:
        inp = input("Enter " + name + "\'s timing for 1000 meters or -1 to quit (minutes, seconds): ")
        if inp == -1:
            break
        times.append(inp)

    players_dict[name] = [calMin(times), calMax(times), calAvg(times)]

whole_tablerdata = []

for key, value in players_dict.iteritems():
    tablerdata = []

    tablerdata.append(key)
    tablerdata.append(value[0])
    tablerdata.append(value[1])
    tablerdata.append(value[2])

    whole_tablerdata.append(tablerdata)

print "   "
print tabulate(whole_tablerdata, headers=["Athlete","Min", "Max", "Avg"])