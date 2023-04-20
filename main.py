from maxpar import *

def func1():
    print('xXx ')


def main():
    t1 = Task("T1", func1, ["M1"], ["M2"])
    t2 = Task("T2", func1, ["M1"], ["M4"])
    t3 = Task("T3", func1, ["M3", "M4"], ["M1"])
    t4 = Task("T4", func1, ["M3","M4"], ["M5"])
    t5 = Task("T5", func1, ["M4"], ["M2"])
    t6 = Task("T6", func1, ["M1", "M2","M4"], ["M4"])
    t7 = Task("T7",func1,["M1","M2","M4"],["M4"])
    t8 = Task("T8",func1,["M1","M3"],["M5"])
    ts = TaskSystem([t1, t2, t3, t4, t5, t6,t7,t8], {'T1': [], "T2": ["T1"], "T3": ["T2"], "T4": ["T2"], "T5": ["T4","T3"], "T6": ["T4"],"T7":["T6","T5"],"T8":["T7"]})

    t11 = Task("T11", func1, ["M1,M2"], ["M3"])

    # print("---------Task System valide--------------------")
    # print("---------Error doublon--------------------")
    ts1 = TaskSystem([t1, t1, t2,t3, t4, t5, t6,t7,t8], {"T1": [],"T1": [], "T2": ["T1"], "T3": ["T2"], "T4": ["T2"], "T5": ["T3","T4"], "T6": ["T4"],"T7":["T5","T6"],"T8":["T7"]})
    # print("---------Error tâche manquante dictionnaire--------------------")
    # ts2 = TaskSystem([t1,t11, t2, t3, t4, t5, t6,t7,t8], {"T2": [], "T3": ["T2"], "T4": ["T2"], "T5": ["T3","T4"], "T6": ["T4"],"T7":["T5","T6"],"T8":["T7"]})
    # print("---------Error tâche n'existe pas--------------------")
    # ts3 = TaskSystem([t1,  t3, t4, t5, t6,t7,t8], {"T1": [], "T2": ["T1"], "T3": ["T2"], "T4": ["T2"], "T5": ["T3","T4"], "T6": ["T4"],"T7":["T5","T6"],"T8":["T7"]})
    ts.runSeq()


main()