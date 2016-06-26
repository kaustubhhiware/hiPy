inp_str = raw_input("enter string to encode : ")

rot_id = raw_input("enter id of rotation : ")
rot_id = int(rot_id)
rot_id = rot_id % 26

out_str=inp_str
for i in range(len(inp_str)):
	#ord converts a to 97 , b to 98 so on
	wt = ord(inp_str[i])+rot_id

	#chr inverts ord
	print chr(wt)


print 'encoded string : ',out_str