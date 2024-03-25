import sqlite3
import os
import networkx as nx
import matplotlib.pyplot as plt
from element import edgeEvent


db_path=os.getcwd()+"\\db"


class Visualizer:
    
    def __init__(self,file_name):
        self.file_name=file_name
    
    def set_file(self,file_name):
        self.file_name=file_name

    def visualize(self):
        
        con=sqlite3.connect(db_path+"\\"+self.file_name+".db")
        cur=con.cursor()
        
        # load edge event
        rows=cur.execute("select * from edgeEvent").fetchall()
        edge_event_list=[]
        for row in rows:
            edge_event_list.append(edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        # aggregate to static graph
        G = nx.Graph()
        for edge_event in edge_event_list:
            G.add_edge(edge_event.sourceID,edge_event.targetID)
            
        # 각 노드의 degree(연결된 엣지의 개수)를 계산
        degrees = dict(G.degree())

        # degree를 기준으로 가장 많은 엣지를 가진 노드를 찾음
        max_degree_node = max(degrees, key=degrees.get)

        print("가장 많은 엣지를 가진 노드:", max_degree_node)
        print("연결된 엣지의 개수:", degrees[max_degree_node])
        
        # kamada_kawai_layout으로 시각화
        pos = nx.kamada_kawai_layout(G)
        plt.figure(figsize=(8, 4))
        plt.subplot(121)
        nx.draw(G, pos, with_labels=False, node_color='black', edge_color='black',node_size=2,width=1)
        
        plt.show()
        
        
        
        