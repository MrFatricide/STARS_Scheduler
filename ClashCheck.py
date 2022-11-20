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


def lessonClash(lesson, other_lesson_list, debug=0):
    """
    -   lesson : [t start, t end]
    -   other_lesson_list : [ [t start, t end], [t start, t end] ]
        -   e.g. ce1106 index 11608 has tut on mon 10am, lab tues 2pm etc
    -   checks whether the weekday(e.g. Mon, Tues etc) are the same
    -   checks through the whole list to see whether it clashes
    -   other_lesson[t start] < lesson[t start] < other_lesson[t end] = clash
    """
    for other_lesson in other_lesson_list:
        if other_lesson[0][6] == lesson[0][6] and other_lesson[0] <= lesson[0] < other_lesson[1]:
            if debug:
                print(f"clashed {printTimeFormat(lesson[0])}\n"
                      f"{printTimeFormat(other_lesson[0])}, "
                      f"{printTimeFormat(other_lesson[1])}")
            return 1
    return 0


def time_clash_check(module_schedule, combination_tuple, debug=0):
    schedule_list = []
    clash_count = 0
    for mod, index in enumerate(combination_tuple):
        # Current Module would be [t_start, t_end]
        # where t_start < any other mod start < t_end for no clash
        current_mod = module_schedule[mod][index]

        # Check for Clash
        # If start time of the current module is between
        # the start and end time of any other module
        # increment the clash count
        for list_index, schedule in enumerate(schedule_list):
            for lesson in current_mod:
                clashed = lessonClash(lesson, schedule, debug)
                clash_count += clashed

                if debug and clashed:
                    print(list_index, len(schedule_list))
                    print("-------------------------")

        # Append to overall combination list
        schedule_list.append(current_mod)

    if debug:
        print(f"clash count : {clash_count}\n")
    return clash_count


if __name__ == '__main__':
    from NTU_Module import *

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
        '11603': [TimeSlot(2, 8, 20, 10, 20).getTime(), TimeSlot(3, 14, 00, 15, 30).getTime()],
        '11610': [TimeSlot(3, 8, 20, 10, 20).getTime(), TimeSlot(1, 13, 30, 14, 30).getTime()]
    }

    ce1103 = Module('CE1103', sample_schedule1)
    ce1105 = Module('CE1105', sample_schedule2)
    ce1106 = Module('CE1106', sample_schedule1)
    ce1107 = Module('CE1107', sample_schedule3)

    time_table_list = [ce1103.getSchedule(), ce1105.getSchedule(), ce1106.getSchedule(), ce1107.getSchedule()]
    time_table = TimeTable(time_table_list)

    test_lst2 = time_clash_check(time_table.module_schedule, ('11008', '11608', '11009', '11603'), debug=1)
