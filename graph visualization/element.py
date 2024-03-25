class Edge:
    def __init__(self,id,sourceID,targetID):
        self.id=id
        self.sourceID=sourceID
        self.targetID=targetID

class vertexEvent:
    def __init__(self,id,vertexID,time,x_pos,y_pos):
        self.id=id
        self.vertexID=vertexID
        self.time=time
        self.x_pos=x_pos
        self.y_pos=y_pos
    
class edgeEvent:
    def __init__(self,id,sourceID,targetID,time):
        self.id=id
        self.sourceID=sourceID
        self.targetID=targetID
        self.time=time    
        
class TP_edgeEvent:
    def __init__(self,id,sourceEID,targetEID,time):
        self.id=id
        self.sourceEID=sourceEID
        self.targetEID=targetEID
        self.time=time 