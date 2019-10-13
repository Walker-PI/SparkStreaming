import csv
import os
import time
import pandas as pd

# remove origin files

def del_origin_files(path):
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)

def sort_csvfile(csvfile):
    csv_reader = pd.read_csv(csvfile)
    csv_reader = csv_reader.sort_values(by=['Id_tag'],ascending=False)
    return csv_reader


if __name__ == '__main__':
    del_origin_files("outputDir")
    
    csv_reader = sort_csvfile("problemset.csv")

    with open("problemset.csv","r") as csvfile:
        rows = len(csvfile.readlines())    
    rows_one_time=100
    
    
    for x in range(rows-2, -1, -rows_one_time):
        times = str(time.time())
        y = x - rows_one_time + 1
        if y < 0:
            y = 0
        csv_reader.loc[x:y,['Algorithms']].to_csv("outputDir/"+times+".txt",header=None,index=None,quoting=0,encoding='utf-8')
        time.sleep(1)

    




        



