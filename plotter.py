import pandas as pd
import matplotlib.pyplot as plt
import sys

def plotter(n=3):

    # n is the number of column
    root = "../"
    plt.figure(figsize=(18,15))
    for act in range(1,6):
        path1 = root + "TrainData/subject1/activity"+str(act)+"/subject_1_activity_"+str(act)+"_repeat_1.csv"
        path2 = root + "TrainData/subject2/activity"+str(act)+"/subject_2_activity_"+str(act)+"_repeat_1.csv"
        path3 = root + "TrainData/subject3/activity"+str(act)+"/subject_3_activity_"+str(act)+"_repeat_1.csv"
        data1 = pd.read_csv(path1)
        data2 = pd.read_csv(path2)
        data3 = pd.read_csv(path3)
        
        a = plt.subplot(5,3,(3*(act-1))+1)
        a.plot(data1.iloc[:,n])
        a.set_xticks([])
        a.set_xlabel(f"User: 1, activity: {act}")
        b = plt.subplot(5,3,(3*(act-1))+2)
        b.plot(data2.iloc[:,n])
        b.set_xticks([])
        b.set_xlabel(f"User: 2, activity: {act}")
        c = plt.subplot(5,3,(3*(act-1))+3)
        c.plot(data3.iloc[:,n])
        c.set_xticks([])
        c.set_xlabel(f"User: 3, activity: {act}")
    plt.suptitle(f"Column: {n}")
    plt.show()

n = int(sys.argv[1])
plotter(n)