# -*- coding: utf-8 -*-
import os

#Each website is a folder
#refrain from using dir as var since it is a standard

def create_project_directory(directory):
	if not os.path.exists(directory):
		print('Creating project : '+directory)
		os.makedirs(directory)


#Create queue and crawled files(if not done already)
def create_data_files(project_name,base_url):
	queue = project_name+"/queue.txt"
	crawled = project_name+"/crawled.txt"

	if not os.path.isfile(queue):
		write(queue,base_url)
		#write to what file, what is written

	if not os.path.isfile(crawled):
		write(crawled,"")


#Create a new file
def write_file(path,data):
	f = open(path,'w')
	f.write(data)
	f.close()



#Add data onto an existing file
def append_to_file(path,data):
	with open(path,'a') as file:		#a - append
	file.write(data+'\n')


#Delete file contents
def delete_file_contents(path):
	with open(path,'w'):
		pass				#do nothing,snow



name=raw_input("What dir? ")
create_project_directory(name)

