import os.path
import random as rn

filename = "data.json"
    	
    
def write():
	limit = 1000000
	with open(filename,"a") as f:
		f.write("[{'data':[")
		for i in range(limit+1):
			f.write(str(rn.randint(0,limit))+',')
		f.write("}]")
	
		
			
			
			

def fileEmpty():
	# Print out 'File is empty!' if nodata.txt is empty
	if os.path.exists(filename):
		if os.path.getsize(filename) == 0:
			return True
		else:
			return False
	write();return fileEmpty()
	
	
		
def get():
	with open(filename,'r') as f:
		return f.read()[10:-3].split(',')
	
		
