import os

def get_nmap(options,ip):
	command = "nmap "+options+" "+ip
	process = os.popen(command)
	results = str(process.read())
	marker = results.find('has address')
	return results[marker:].splitlines()[0]
	

#print(get_nmap('-F','54.186.250.79'))