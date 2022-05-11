from pathlib import Path

Year = '2020-06'
data_dirs = [Year,]

for data_dir in data_dirs:
    count = 0
    for path in Path(data_dir).iterdir():	
        if path.name.endswith('.txt'):
        	print (path.name)
        	file1=  open(path, "r")
        	file1_content = file1.readlines() 
#         	f = open("2020-01/2020-01-randomlychosen.txt", "a+")
#         	for i in file1_content:
#         		f.write(i)
        	
        	for line in file1_content:
        		count = count + 1
        		if count == 1000:
        			f = open("2020-2021/2020-06-randomlychosen.txt", "a+")
        			f.write(line)
        			print (line)
        			count = 0


# since 2005 count = 400

