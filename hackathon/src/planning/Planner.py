#!/usr/bin/env python3
import matplotlib.pyplot as p
import math
import random
import rospy
from planning.msg import array
from shapely.geometry import Point, Polygon
from shapely.geometry import LineString
from obstacles.msg import coords


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
        if(flag==1):
            continue
        for i in range(0,15):
            if(Point(x1[i],y1[i]).distance(line)<=0.25):
                flag=1
                break
        if(flag==1):
            continue
        for i in range(0,15):
            if(Point(x1[i],y1[i]).distance(line2)<=0.25):
                key=0
                break
            else:
                key=1
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
            path.reverse()
            return path

def main():
    print("Start")
    
def callback(msg):
    start = (0.0,0.0)
    goal = (6,6)
    main()
    x1=msg.x
    y1=msg.y
    path = RRT(start,goal,x1,y1)
    
    
if __name__ == '__main__':
    rospy.init_node('Planner')
    while not rospy.is_shutdown():
        sub=rospy.Subscriber('obstacles',coords,callback)
        pub=rospy.Publisher('path',array)
        rate=rospy.Rate(2)
        pub.publish(path)
        rate.sleep()
