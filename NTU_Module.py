import time


class TimeSlot:
    def __init__(self, day, hour, minute, hour_end, minute_end):
        self.time_period_t_start = time.strptime(f"{day} {hour} {minute}", "%w %H %M")
        self.time_period_t_end = time.strptime(f"{day} {hour_end} {minute_end}", "%w %H %M")

    def getTime(self):
        return [self.time_period_t_start, self.time_period_t_end]


class Module:
    def __init__(self, name, schedule_dict, priority=0):
        self.schedule = schedule_dict
        self.name = name
        self.priority = priority

    @staticmethod
    def printTimeFormat(time_slot):
        day_dict = {
            6: "Sunday",
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday"
        }

        return f"{day_dict[int(time_slot[6])]}, {time_slot[3]}:{time_slot[4]}"

    def printSchedule(self):
        print(self.name)
        for index in self.schedule:
            print(f"index : {index}")

            # Prints Start time and End time for a certain class
            [print(f"t start : {self.printTimeFormat(time_slot_start)}, "
                   f"t end : {self.printTimeFormat(time_slot_end)}")
             for time_slot_start, time_slot_end in self.schedule[index]]

    def getSchedule(self):
        return {self.name: self.schedule}


class TimeTable:
    def __init__(self, module_list):
        module_name_list = []
        module_schedule_list = []
        for module_dict in module_list:
            # ['CE1103', 'CE1106', 'CE1107']
            module_name_list.append([name for name in module_dict.keys()][0])
            # [{'11608' : [time_struct1, time_struct2]}, {'11609': [...]} ]
            module_schedule_list.append([schedule for schedule in module_dict.values()][0])

        self.module_names = module_name_list
        self.module_schedule = module_schedule_list

    def printHeaders(self):
        print('| ', end='')
        for name in self.module_names:
            print(name, end=' | ')
        print("Clash")


if __name__ == "__main__":
    from BruteForceAlgo import *
    sample_schedule = {
        '11608': [TimeSlot(2, 8, 20, 10, 20).getTime(), TimeSlot(3, 13, 30, 14, 30).getTime()]
    }
    T1 = TimeSlot(2, 8, 20, 10, 20)
    print("-------")
    T1.getTime()

    ce1106 = Module('CE1106', sample_schedule)
    ce1106.printSchedule()

    print(ce1106.getSchedule()['CE1106'])

    # check for a certain time slot being in the schedule dictionary
    print(TimeSlot(3, 8, 20, 10, 20).getTime()[0][6])


    sample_schedule1 = {
        '11008': [TimeSlot(2, 8, 20, 10, 20).getTime(), TimeSlot(3, 13, 30, 14, 30).getTime()],
        '11009': [TimeSlot(2, 10, 20, 10, 20).getTime(), TimeSlot(3, 14, 30, 15, 30).getTime()],
    }

    sample_schedule2 = {
        '11608': [TimeSlot(3, 8, 20, 10, 20).getTime(), TimeSlot(5, 13, 30, 14, 30).getTime()],
        '11609': [TimeSlot(4, 10, 20, 10, 20).getTime(), TimeSlot(4, 14, 30, 15, 30).getTime()],
        '11708': [TimeSlot(2, 8, 20, 10, 20).getTime(), TimeSlot(2, 13, 30, 14, 30).getTime()]
    }

    sample_schedule3 = {
        '11604': [TimeSlot(1, 8, 20, 10, 20).getTime(), TimeSlot(5, 13, 30, 14, 30).getTime()],
        '11603': [TimeSlot(2, 8, 20, 10, 20).getTime(), TimeSlot(3, 13, 30, 14, 30).getTime()],
        '11610': [TimeSlot(3, 8, 20, 10, 20).getTime(), TimeSlot(1, 13, 30, 14, 30).getTime()]
    }

    ce1103 = Module('CE1103', sample_schedule1)
    ce1105 = Module('CE1105', sample_schedule2)
    ce1107 = Module('CE1107', sample_schedule3)
    ce1106 = Module('CE1106', sample_schedule1)

    time_table_list = [ce1103.getSchedule(), ce1105.getSchedule(), ce1106.getSchedule(), ce1107.getSchedule()]
    time_table = TimeTable(time_table_list)

    test_lst2 = permute_index(time_table.module_schedule)

    time_table.printHeaders()
    for idx_combination in test_lst2[0]:
        print(idx_combination)

