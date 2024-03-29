from visualizer import Visualizer
from graph_analysis import Analyzer


# file_name=input("file name: ")
# start_time=int(input("start time: "))
# end_time=int(input("end time: "))


# analyzer=Visualizer("simple_a_0_10_TP")
# analyzer.visualize(start_time,end_time)
# analyzer.tree_visualize(0,10)

analyzer=Analyzer("bitcoin")
analyzer.analyze(0,1294771313000)


