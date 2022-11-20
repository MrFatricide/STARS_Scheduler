import pandas as pd
import numpy as np
from NTU_Module import *


def excel_datetime(string, debug=0):
    week_day_dict = {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 0
    }
    if debug:
        print(string)

    try:
        string_list = string.split('_')
    except AttributeError:
        return None

    weekday = week_day_dict[string_list[0]]
    hour = int(string_list[1])
    minute = int(string_list[2])
    return weekday, hour, minute


def mod_class_creation(df, mod_code,debug=0):
    # df where module code column = mod_code
    # drop rows where 'Module_code' == Na
    new_df = df.where(df['Module_code'] == mod_code).dropna(subset=['Module_code'])

    index_list = list(new_df['Index'].astype(int))

    # Creating Dictionary
    mod_dict = {}
    for index in index_list :
        temp_df = new_df[new_df['Index'] == index].reset_index(drop=True)
        if debug:
            print(temp_df)
        mod_dict[str(index)] = [excel_datetime(temp_df[i][0], debug) for i in temp_df.iloc[:, 2:8]
                                if temp_df[i][0] != np.NAN]

        # { '11608' : [ lesson1start, lesson1end, ...]; lesson1start: (2,11,30)
        # Convert tuple to Timeslot Class
        timeslot_list = []
        for i in range(0, 6, 2):
            try:
                if debug:
                    print(mod_dict[str(index)][i])
                wday, hr, minute = mod_dict[str(index)][i]
                wday2, hr2, minute2 = mod_dict[str(index)][i+1]
                timeslot_list.append(TimeSlot(wday, hr, minute, hr2, minute2).getTime())

            except TypeError or IndexError:
                pass

        mod_dict[str(index)] = timeslot_list

    return mod_dict


if __name__ == "__main__":
    from BruteForceAlgo import *

    df = pd.read_csv('mod_info.csv')
    mod_code_list = [code for code in df['Module_code'].unique()]

    mod_list = []
    for code in mod_code_list:
        schedule = mod_class_creation(df, code, debug=0)
        mod = Module(str(code), schedule)
        mod_list.append(mod.getSchedule())

    time_table = TimeTable(mod_list)
    test_lst2 = permute_index(time_table.module_schedule)

    time_table.printHeaders()
    for idx_combination in test_lst2[0]:
        print(idx_combination)

    for idx_combination in test_lst2[1]:
        print(idx_combination)

