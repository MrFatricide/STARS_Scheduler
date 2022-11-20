# Code permutates through all combinations of indexes
# Reference : https://stackoverflow.com/questions/2853212/all-possible-permutations-of-a-set-of-lists-in-python
import time
import itertools
from ClashCheck import *


def permute_index(module_schedule, debug=0):
    """
    -   takes in timetable class(from NTU_Module)
    -   returns dictionary of (combination, clash)
    -   dict[0] means all combination with no clash
    -   dict[1] means all combination with 1 clash etc
    """
    index_lst = []
    permutation_dict = {}
    for mod in module_schedule:
        index_lst.append(list(index for index in mod.keys()))

    # Permutation of all possible indices
    permuted_index_lst = list(itertools.product(*index_lst))

    for combination in permuted_index_lst:
        # Function to check is from BruteForceAlgo.py
        clash = time_clash_check(module_schedule, combination, debug)
        try:
            permutation_dict[clash].append((combination, clash))

        # If Dictionary key doesn't exist, create list
        except KeyError:
            permutation_dict[clash] = [(combination, clash)]

    # Check list items
    if debug:
        print("\n\n--------------- Debug Index Permutation-------------")
        for permutations in permuted_index_lst :
            print(permutations)
        print("---------------- End Of Permutations ----------------\n")
        print(f"Permutation Count : {len(permuted_index_lst)}\n\n")

    return permutation_dict


if __name__ == '__main__':
    from NTU_Module import *

    sample_schedule1 = {
        '11008': [TimeSlot(1, 8, 20, 10, 20).getTime(), TimeSlot(3, 13, 30, 14, 30).getTime()],
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

    test_lst = permute_index(time_table.module_schedule, debug=1)

    no_clash = test_lst[0]
    clash_1 = test_lst[1]
    for combi in no_clash:
        print(combi)
