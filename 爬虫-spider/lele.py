from numpy import *
from itertools import *
e=array([[1,0],[0,1]])
pauli1=array([[1,0],[0,-1]])
pauli2=array([0,1],[1,0])
list=[e]*10
H=zeros((2**10,2**10))
for i in range(9):
	list[i]=pauli1
	list[i+1]=pauli1
	c=list[0]
	for j in list[1:-1]:
		c=product(c,j)
	for x in c:
		list=[]
		list.append(x)
	H1=list.reshape((1024,1024))
	H+=H1