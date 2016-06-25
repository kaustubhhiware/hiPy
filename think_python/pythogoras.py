import math

def dist(x1,y1,x2,y2):
	dx = x2-x1
	dy=y2-y1
	dsq = dx*dx + dy*dy
	result = math.sqrt(dsq)
	return result

print "dist :"
print dist(0,0,3,4)