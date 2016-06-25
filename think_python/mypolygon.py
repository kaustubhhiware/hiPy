from swampy.TurtleWorld import *
import math
#requirements : 
#sudo apt-get install python python-tk
# pip install swampy


#square function
def square(bob,length):
	for i in range(4):
		fd(bob,length)
		rt(bob)


#construct regular polygon
def polygon(bob,length,num_sides):
	angle = 360.0/num_sides #regular polygon angle

	for i in range(num_sides):
		fd(bob,length)
		rt(bob,angle)

def circle(bob,radius):
	arc = raw_input("Angle of arc ? 360 / 0 if circle : ")
	arc = int(arc)
	num_sides=63
	if arc==0 or arc==360:
		polygon(bob,0.1*radius,num_sides)
		# l * n = 6.28 *r
		# n= 63 => l ~ r/10
	else:
		num_sides=int(63*arc/360)
		angle=360.0/63
		for i in range(num_sides):
			fd(bob,0.1*radius)
			rt(bob,angle)


# move with fd , bk , lt , rt
#lt - 90^ - lt(bob,45) - lt 45^
#init	
world=TurtleWorld()
bob = Turtle()
print bob
bob.delay=0.01# move your arse boy!

option = raw_input("Enter anything for polygon , 0 for circle : ")
option=int(option)

if option==0:
	r=raw_input("Enter radius : ")
	rad = float(r)
	circle(bob,rad)

else:	
	len=raw_input("Enter side of polygon : ")
	length = int(len)
	#square(bob,length)

	n=raw_input("What number of sides? : ")
	num_sides = int(n)
	polygon(bob,length,num_sides)


wait_for_user()