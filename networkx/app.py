from visualizer import Visualizer



file_name=input("file name: ")
start_time=int(input("start time: "))
end_time=int(input("end time: "))


analyzer=Visualizer(file_name)
analyzer.visualize(start_time,end_time)




