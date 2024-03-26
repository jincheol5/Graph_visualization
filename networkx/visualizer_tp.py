import sqlite3
import os
import networkx as nx
import matplotlib.pyplot as plt
from element import TP_edgeEvent


current_directory_path=os.getcwd() # 현재 작업 경로
parent_directory_path=os.path.dirname(current_directory_path) # 현재 작업 경로의 부모 작업 경로 
db_path = os.path.join(parent_directory_path, "db") # db파일 상대 경로 db_path="C:\\repo\그래프시각화연구\TemPV\TemPV\db"


class TPVisualizer:
    
    def __init__(self,file_name):
        self.file_name=file_name
    
    def set_file(self,file_name):
        self.file_name=file_name

    def visualize(self,start_time,end_time):
        
        con=sqlite3.connect(db_path+"\\"+self.file_name+".db")
        cur=con.cursor()
        
        
        # load edge event
        rows=cur.execute("select * from tpEdgeEvent").fetchall()
        edge_event_list=[]
        for row in rows:
            
            if row[3]<start_time:
                continue
            
            if row[3]>end_time:
                break
            
            
            if row[1]!=row[2]:
                edge_event_list.append(TP_edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        # aggregate to static graph
        G = nx.Graph()
        for edge_event in edge_event_list:
            G.add_edge(edge_event.sourceEID,edge_event.targetEID)
            
        # 각 노드의 degree(연결된 엣지의 개수)를 계산
        degrees = dict(G.degree())

        # degree를 기준으로 가장 많은 엣지를 가진 노드를 찾음
        max_degree_node = max(degrees, key=degrees.get)


        print("node의 수: ", G.number_of_nodes())
        print("edge의 수: ",G.number_of_edges())
        print("가장 많은 엣지를 가진 노드:", max_degree_node)
        print("연결된 엣지의 개수:", degrees[max_degree_node])
        
        # kamada_kawai_layout으로 시각화
        #pos=nx.spring_layout(G)
        pos = nx.kamada_kawai_layout(G)
        plt.figure(figsize=(10, 8))
        # nx.draw_networkx_nodes(G, pos,node_color='black',node_size=1,alpha=0.3)
        nx.draw_networkx_edges(G, pos,edge_color='black',width=1,alpha=0.1)
        
        plt.show()
        
        
        
        