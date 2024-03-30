import os
import time

current_directory_path=os.getcwd() # 현재 작업 경로
parent_directory_path=os.path.dirname(current_directory_path) # 현재 작업 경로의 부모 작업 경로 
db_path = os.path.join(parent_directory_path, "db") # db파일 상대 경로 db_path="C:\\repo\그래프시각화연구\TemPV\TemPV\db"


file_path="D:\mydata\\bitcoin.txt"
new_file_path="D:\mydata\\new-bitcoin.txt"


file=open(file_path,'r')
new_file=open(new_file_path,'w')

while True:
    line=file.readline()

    if not line: break
    
    data=line.split()
    
    sourceID=data[0]
    targetID=data[1]
    milli_time=data[2]
    
    seconds_time=int(milli_time)/1000
    
    
    
    new_value=sourceID+" "+targetID+" "+str(int(seconds_time))+"\n"
    
    new_file.write(new_value)