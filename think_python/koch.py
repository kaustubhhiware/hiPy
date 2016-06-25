from swampy.TurtleWorld import *


def koch_curve(t,length):
	"""
	draw a koch curve
	"""
	if length < 3:
		fd(t,length)
	else:
		koch_curve(t,length/3)
		lt(t,60)

		koch_curve(t,length/3)
		rt(t,120)

		koch_curve(t,length/3)
		lt(t,60)

		koch_curve(t,length/3)

#init	
world=TurtleWorld()
bob = Turtle()
print bob
bob.delay=0.01# move your arse boy!

l = raw_input("Enter length of koch: ")
l = float(l)
koch_curve(bob,l)

wait_for_user()