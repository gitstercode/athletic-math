import datetime
from tabulate import tabulate

class AtheleteClass(object):

    def __init__(self):
        self.athlets = input("Enter number of Athletes practicing: ")

    def looping(self):

        players_dict = {}

        for i in range(1, self.athlets + 1):

            name = raw_input("Enter the name of Athlete " + str(i) + ": ")

            times = []
            while True:
                inp = input("Enter " + name + "\'s timing for 1000 meters or -1 to quit (minutes, seconds): ")
                if inp == -1:
                    break
                times.append(inp)

            players_dict[name] = [self.calMin(times), self.calMax(times), self.calAvg(times)]

        whole_tablerdata = []

        for key, value in players_dict.iteritems():
            tablerdata = list()

            tablerdata.append(key)
            tablerdata.append(value[0])
            tablerdata.append(value[1])
            tablerdata.append(value[2])

            whole_tablerdata.append(tablerdata)

        print "   "
        print tabulate(whole_tablerdata, headers=["Athlete", "Min", "Max", "Avg"])

    def convert_tup_to_seconds(self, lists):
        seconds_list = []
        for i in lists:
            calSeconds = (i[0] * 60) + i[1]
            seconds_list.append(calSeconds)
        return seconds_list

    def secs_to_MS(self, secs):
        return datetime.datetime.fromtimestamp(secs).strftime('%M:%S')

    def calAvg(self, times):
        seconds_list = self.convert_tup_to_seconds(times)
        sum = 0
        for i in seconds_list:
            sum += i
            sec = sum / float(len(seconds_list))

        return self.secs_to_MS(sec)

    def calMax(self, times):
        seconds_list = self.convert_tup_to_seconds(times)
        sec = max(seconds_list)
        return self.secs_to_MS(sec)

    def calMin(self, times):
        seconds_list = self.convert_tup_to_seconds(times)
        sec = min(seconds_list)
        return self.secs_to_MS(sec)

obj = AtheleteClass()

obj.looping()