import os
curpath = os.path.abspath(os.curdir)
comDir = curpath+"/adana"
allFiles = [f for f in os.listdir(comDir) if os.path.isfile(os.path.join(comDir,f))]
commentList = []
for fil in allFiles:
	if "comment" in fil:
		commentList.append(fil)
allc = open("allcomments.txt","w+")
for fil in commentList:
	try:
		f = open(comDir+"/"+fil)
		for line in f:
			allc.write(line)
		
	except OSError as e:
		pass
	
