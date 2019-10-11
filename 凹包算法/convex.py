# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:04:30 2019

@author: yllzxzyq
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 01:08:12 2019

@author: yllzxzyq
"""
import numpy as np
import matplotlib.pyplot as plt
import copy
import math
#获取基准点的下标,基准点是p[k]
def get_leftbottompoint(p):
    k = 0
    for i in range(1, len(p)):
        if p[i][1] <= p[k][1]:
            k = i
    return k
#叉乘计算方法
def multiply(p1, p2, p0):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])
#获取极角，通过求反正切得出，考虑pi/2的情况
def get_arc(p1, p0, the):
    # 兼容sort_points_tan的考虑
    if (p1[0] - p0[0]) == 0:
        if ((p1[1] - p0[1])) == 0:
            return -1;
        else:
            return math.pi / 2
    tan = float(p1[1] - p0[1]) / float(p1[0] - p0[0])
    arc = math.atan(tan)-the
    if arc >= 0:
        return arc
    else:
        return math.pi + arc
#对极角进行排序,排序结果list不包含基准点
def sort_points_tan(p, pk, the):
    p2 = []
    for i in range(0, len(p)):
        p2.append({"index": i, "arc": get_arc(p[i], pk, the)})
    #print('排序前:',p2)
    p2.sort(key=lambda k: (k.get('arc')))
    #print('排序后:',p2)
    p_out = []
    for i in range(0, len(p2)):
        p_out.append(p[p2[i]["index"]])
    return p_out

def distance(p1, p2):
    """
    Calculates the distance between two points.

    :param p1, p2: points
    :return: distance between points
    """
    p1x, p1y = p1
    p2x, p2y = p2

    return math.sqrt((p1x - p2x) ** 2 + (p1y - p2y) ** 2)

#r为滚圆法的半径
def concavehull(p,r):
    k=get_leftbottompoint(p)
    #print('排序前去除基准点的所有点:',p,'基准点:',pk)
    pk=copy.deepcopy(p[k])
    p_result=[0,p[k]]
    the=0
    #按与基准点连线和x轴正向的夹角排序后的点坐标
    #print('其余点与基准点夹角排序:',p_sort)
    while(True):
        thelist = []
        p_sort = sort_points_tan(p, pk,the)
        for i in range(len(p_sort)):
            thelist.append(math.atan2(p_sort[i][1]-pk[1],p_sort[i][0]-pk[0]))
            leng=distance(p_sort[i],pk)
            if(leng<2*r and leng!=0 and (p_sort[i]!=p_result[-2]) or len(p_result)<2):
                mid=[0.5*(pk[0]+p_sort[i][0]),0.5*(pk[1]+p_sort[i][1])]
                arc2=thelist[i]+math.pi*0.5
                dist=math.sqrt(r**2-0.25*(leng**2))
                C1=[mid[0]+math.cos(arc2)*dist,mid[1]+math.sin(arc2)*dist]
                C2=[mid[0]-math.cos(arc2)*dist,mid[1]-math.sin(arc2)*dist]
                t1 = True
                t2 = True
                for j in range(len(p_sort)):
                    if(distance(p_sort[j],C1)<=r and (p_sort[j]!=pk and p_sort[j]!= p_sort[i])):
                        t1=False
                    if(distance(p_sort[j],C2)<=r and (p_sort[j]!=pk and p_sort[j]!= p_sort[i])):
                        t2=False
                if(t1 or t2):
                    the = thelist[i]
                    pk=copy.deepcopy(p_sort[i])
                    p_result.append(p_sort[i])
                    break
        if(pk==p_result[1]):
            break
    p_result.remove(0)
    return p_result#测试

# Plotting the output
def plotre(p,p_result):
    plt.figure()
    plt.axis('equal')
    plt.plot(np.array(p)[:, 0], np.array(p)[:, 1], '.')
    x,y=zip(*p_result)
    plt.plot(x,y,'r')
    
points =[
    (207, 184), (393, 60), (197, 158), (197, 114), (128, 261), (442, 40),
    (237, 159), (338, 75), (194, 93), (33, 159), (393, 152), (433, 267),
    (324, 141), (384, 183), (273, 165), (250, 257), (423, 198), (227, 68),
    (120, 184), (214, 49), (256, 75), (379, 93), (312, 49), (471, 187),
    (366, 122)
]
p=points
p_r=concavehull(p,10000)
plotre(p,p_r)