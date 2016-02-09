import math
#from cmath import sqrt
#def distance(a,b) 
#a="1234"
#b="5678"

def distance(a,b)
	sum=0
	count=0
	for i in range(len(a)) :
		count=(( ord(b[i])-ord(a[i]))^2) 
		sum=count+sum
		
	dist=math.sqrt(sum)
	return dist	
