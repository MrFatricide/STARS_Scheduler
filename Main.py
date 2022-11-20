# Finalized version 1
from ReadExcel import *

if __name__ == '__main__':
    from NTU_Module import TimeTable, TimeSlot, Module
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
