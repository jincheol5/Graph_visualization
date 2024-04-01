import sqlite3
import os
import networkx as nx
import matplotlib.pyplot as plt
from element import edgeEvent


current_directory_path=os.getcwd() # 현재 작업 경로
parent_directory_path=os.path.dirname(current_directory_path) # 현재 작업 경로의 부모 작업 경로 
db_path = os.path.join(parent_directory_path, "db") # db파일 상대 경로 db_path="C:\\repo\그래프시각화연구\TemPV\TemPV\db"


class Analyzer:
    
    def __init__(self,file_name):
        self.file_name=file_name
        
    def set_file(self,file_name):
        self.file_name=file_name
        
    def analyze(self,start_time,end_time):
        
        con=sqlite3.connect(db_path+"\\"+self.file_name+".db")
        cur=con.cursor()
        
        # load edge event
        rows=cur.execute("select * from edgeEvent").fetchall()
        edge_event_list=[]
        for row in rows:
            
            if row[3]<start_time:
                continue
            
            if row[3]>end_time:
                break
            
            
            edge_event_list.append(edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        # aggregate to static graph
        G = nx.Graph()
        for edge_event in edge_event_list:
            G.add_edge(edge_event.sourceID,edge_event.targetID)
            
        # 각 노드의 degree(연결된 엣지의 개수)를 계산
        degrees = dict(G.degree())

        # degree를 기준으로 내림차순 정렬
        sorted_nodes = sorted(degrees, key=lambda x: degrees[x], reverse=True)

        # degree를 기준으로 가장 많은 엣지를 가진 노드를 찾음
        node_1=sorted_nodes[0]
        node_2=sorted_nodes[1]
        node_3=sorted_nodes[2]
        node_4=sorted_nodes[3]
        node_5=sorted_nodes[4]



        print("node의 수: ", G.number_of_nodes())
        print("edge의 수: ",G.number_of_edges())
        
        print("가장 많은 엣지를 가진 노드:", node_1)
        print("연결된 엣지의 개수:", degrees[node_1])
        
        print("두번째로 많은 엣지를 가진 노드:", node_2)
        print("연결된 엣지의 개수:", degrees[node_2])
        
        print("세번째로 많은 엣지를 가진 노드:", node_3)
        print("연결된 엣지의 개수:", degrees[node_3])
        
        print("네번째로 많은 엣지를 가진 노드:", node_4)
        print("연결된 엣지의 개수:", degrees[node_4])
        
        print("다섯번째로 많은 엣지를 가진 노드:", node_5)
        print("연결된 엣지의 개수:", degrees[node_5])