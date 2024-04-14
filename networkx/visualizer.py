import sqlite3
import os
import networkx as nx
import igraph as ig
import matplotlib.pyplot as plt
from element import edgeEvent,TP_edgeEvent, Edge
import math


current_directory_path=os.getcwd() # 현재 작업 경로
parent_directory_path=os.path.dirname(current_directory_path) # 현재 작업 경로의 부모 작업 경로 
db_path = os.path.join(parent_directory_path, "db") # db파일 상대 경로 db_path="C:\\repo\그래프시각화연구\TemPV\TemPV\db"


class Visualizer:
    
    def __init__(self,file_name):
        self.file_name=file_name
    
    def set_file(self,file_name):
        self.file_name=file_name

    def visualize(self,sourceID,start_time,end_time):
        
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
            
            
            if row[1]!=row[2]:
                edge_event_list.append(edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        con=sqlite3.connect(db_path+"\\"+self.file_name+"_"+sourceID+"_"+str(start_time)+"_"+str(end_time)+"_TP.db")
        cur=con.cursor()
        
        
        # aggregate to static graph
        G = nx.Graph()
        for edge_event in edge_event_list:
            G.add_edge(edge_event.sourceID,edge_event.targetID)
        
        # Fruchterman-Reingold 
        pos=nx.spring_layout(G)
        
        
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(G, pos,node_color='black',node_size=2,alpha=0.5)
        nx.draw_networkx_edges(G, pos,edge_color='black',width=1,alpha=0.3)
        
        
        ### temporal paths 강조 
        # load tp edge event
        tp_edge_rows=cur.execute("select * from edge").fetchall()
        tp_edge_list=[]
        for row in tp_edge_rows:
            tp_edge_list.append(Edge(row[0],row[1],row[2]))
        
        cur.close()
        con.close()
        
        hilights=[]
        for tp_edge in tp_edge_list:
            hilight=(tp_edge.sourceID,tp_edge.targetID)
            hilights.append(hilight)
        
        nx.draw_networkx_edges(G, pos, edgelist=hilights, edge_color='red', width=1, alpha=0.3)
        
        plt.show()
    
    def tree_visualize(self,start_time,end_time):
        
        con=sqlite3.connect(db_path+"\\"+self.file_name+".db")
        cur=con.cursor()
        
        # load edge event
        rows=cur.execute("select * from tpEdgeEvent").fetchall()
        tp_edge_event_list=[]
        for row in rows:
            
            if row[3]<start_time:
                continue
            
            if row[3]>end_time:
                break
            
            
            if row[1]!=row[2]:
                tp_edge_event_list.append(TP_edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        # create 
        G=ig.Graph()
        
        vertex_set=set()
        vertex_index_dic={}
        
        
        for event in tp_edge_event_list:
            vertex_set.add(event.sourceEID)
            vertex_set.add(event.targetEID)
        
        for vertex_id in vertex_set:
            G.add_vertex(name=vertex_id)
            vertex_index_dic[vertex_id]=-1
        
        for event in tp_edge_event_list:
            G.add_edge(event.sourceEID,event.targetEID)
        
        
        for key in vertex_index_dic.keys():
            for v in G.vs:
                if v["name"]==key:
                    vertex_index_dic[key]=v.index
        
        
        root_name="a|0"
        root_index=-1
        for v in G.vs:
            if v["name"] == root_name:
                root_index=v.index
        
        my_layout=G.layout_reingold_tilford(root=[root_index])
        my_layout.rotate(270)
        
        
        
        print(my_layout.coords)
        print()
        print(vertex_index_dic)
        
        
        
    
        
        fig, ax = plt.subplots(figsize=(10,6))
        ig.plot(
            G, 
            target=ax,
            layout=my_layout,
            vertex_size=2,
            edge_width="1"
            )
        
        plt.show()
        
        
    def igraph_vis(self,start_time,end_time):
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
            
            
            if row[1]!=row[2]:
                edge_event_list.append(edgeEvent(row[0],row[1],row[2],row[3]))

        cur.close()
        con.close()
        
        # create 
        G=ig.Graph()
        
        vertex_set=set()
        
        for event in edge_event_list:
            vertex_set.add(event.sourceID)
            vertex_set.add(event.targetID)
        
        for vertex_id in vertex_set:
            G.add_vertex(name=vertex_id)
            
        for event in edge_event_list:
            G.add_edge(event.sourceID,event.targetID)
            
        my_layout = G.layout_kamada_kawai()
        
        fig, ax = plt.subplots(figsize=(10,6))
        ig.plot(
            G, 
            target=ax,
            layout=my_layout,
            vertex_size=2,
            edge_width="1",
            alpha=0.1
            )
        
        plt.show()