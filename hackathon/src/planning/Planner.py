import matplotlib.pyplot as p
import math
import random
from shapely.geometry import Point, Polygon
from shapely.geometry import LineString
class Node(object):
    def __init__(self, node):
        self.node=node
        self.parent = None

def RRT(start,goal,x1,y1):
    low=0.0
    high=10.0                           
    rate=0.25
    n=400.0
    s=Node(start)
    stack=[s]
    p.scatter(start[0],start[1],color='r',s=5)
    p.scatter(goal[0],goal[1],color='r',s=5)
    
    while True:
        flag=0
        key=0
        x=random.uniform(low,high)      
        y=random.uniform(low,high)    
        rnd_node=(x,y)         
        dist= [(n.node[0]-rnd_node[0])**2 + (n.node[1]-rnd_node[1])**2 for n in stack] 
        min_pos=dist.index(min(dist))    
        nearest_node=stack[min_pos]
        angle=math.atan2(y-nearest_node.node[1], x-nearest_node.node[0]) 
        new_node_x=nearest_node.node[0]+rate*math.cos(angle) 
        new_node_y=nearest_node.node[1]+rate*math.sin(angle)
        new_node=(new_node_x,new_node_y)
        point=Point(new_node_x,new_node_y)
        coord=(new_node,nearest_node.node)
        coord2=(new_node,goal)
        line=LineString(coord)
        line2=LineString(coord2)
        for i in range(0,15):
            if(Point(x1[i],y1[i]).distance(point)<=0.25):
                flag=1
                break
        print("hello")
        if(flag==1):
            continue
        for i in range(0,15):
            if(Point(x1[i],y1[i]).distance(line)<=0.25):
                flag=1
                break
        print("world")
        if(flag==1):
            continue
        for i in range(0,15):
            if(Point(x1[i],y1[i]).distance(line2)<=0.25):
                key=0
                break
            else:
                key=1
        p.scatter(new_node_x,new_node_y,color='r',s=5)
        p.plot((nearest_node.node[0],new_node_x),(nearest_node.node[1],new_node_y),color='r')
        obj=Node(new_node)
        obj.parent=min_pos
        stack.append(obj)
        d_x= obj.node[0]-goal[0]
        d_y= obj.node[1]-goal[1]
        d= math.sqrt(d_x*d_x + d_y*d_y)
        if(d<=rate or key==1):
            print("goal reached")
            end=len(stack)-1
            path=[(goal)]
            while stack[end].parent is not None:
                path.append(stack[end].node)
                end=stack[end].parent
            path.append(start)
            return path

def visualize(path,start,goal,x1,y1):
    figure, axes = p.subplots()
    for i in range(0,15):
        circle= p.Circle((x1[i],y1[i]),0.25,fill=False)
        axes.add_artist(circle)
    i=len(path)-1
    p.scatter(start[0],start[1],color='r',s=5)
    p.scatter(goal[0],goal[1],color='r',s=5)
    while(i>0):
        p.plot((path[i][0],path[i-1][0]),(path[i][1],path[i-1][1]),color='g')
        i=i-1

def main():
    print("Start")
    start = (0.0,0.0)
    goal = (6,6)
    x1=(0.0,0.0,0.0,1.5,1.5,1.5,1.5,3.0,3.0,3.0,3.0,4.5,4.5,4.5,4.5)
    y1=(1.5,3.0,4.5,0.0,1.5,3.0,4.5,0.0,1.5,3.0,4.5,0.0,1.5,3.0,4.5)
    path = RRT(start,goal,x1,y1)
    visualize(path,start,goal,x1,y1)
    
if __name__ == '__main__':
    main()

p.show()
