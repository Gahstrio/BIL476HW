import os
def convert(fileName):
	f = open(fileName,"r")
	wordset = set()
	for line in  f:
		words = line.split('&')[1].split(' ')
		for word in words:	
			if word in wordset:
				pass
			else:
				wordset.add(word)
	wordDict = {}
	i = 0
	for word in wordset:
		if word in wordDict:
			pass
		else:
			wordDict[word] = i
			i = i +1
	f1 = open("asInt"+fileName,"w+")
	f.close()
	f = open(fileName,"r")
	for line in f:
		line = line.split('&')[1]
		words = line.split(' ')
		createdWords = []	
		for word in words:
			try:
				createdWords.append(wordDict[word])
			except KeyError:
				pass
		f1.write(str(createdWords).replace('[','').replace(']','').replace(',','')+"\n")
	f.close()
	f1.close()
def getPointsFromComment(text):
	tokens = text.split("|")[0].split(" ")
	pointlist = []
	for token in tokens:
		print(token)
		if token.isnumeric():
			pointlist.append(token)
	return pointlist
def minXPoint(x, pointList):
	spP = pointList[0]
	srP = pointList[1]
	tsP = pointList[2]
	if spP < x or srP < x or tsP < x:
		return False
	else :
		return True
def maxXPoint(x,pointList):
	spP = pointList[0]
	srP = pointList[1]
	tsP = pointList[2]
	if spP >= x or srP >= x or tsP >= x:
		return True
	else :
		return False
def avgXMaxPoint(x,pointList):
	spP = pointList[0]
	srP = pointList[1]
	tsP = pointList[2]
	avgP = (spP+srP+tsP) / 3
	if avgP < x:
		return True
	else :
		return False
def avgXMinPoint(x,pointList):
	print(pointList)
	spP = pointList[0]
	srP = pointList[1]
	tsP = pointList[2]
	avgP = (int(spP)+int(srP)+int(tsP)) / 3
	if avgP > x:
		return True
	else:
		 return False
	
def segmentAccToPoint(x, checkFunction):
	curpath = os.path.abspath(os.curdir)
	outputComments = []
	allFiles = [f for f in os.listdir(curpath) if os.path.isfile(os.path.join(curpath,f))]
	for fil in allFiles:
		try:
			f = open(curpath+"/"+fil)
			if not "comment" in fil:
				continue
			for line in f:
				print(line)
				if "|" in line:
					if checkFunction(x,getPointsFromComment(line)):
						outputComments.append(line)
			
		except OSError as e:
			pass
	return outputComments
def segmentForAllPoints():
	for i in range(10):
		f = open("avg"+str(i)+"points.txt","w+")
		segmentation = segmentAccToPoint(i,avgXMinPoint)
		for line in segmentation:
			f.write(line)
segmentForAllPoints()
		
curpath = os.path.abspath(os.curdir)
allFiles = [f for f in os.listdir(curpath) if os.path.isfile(os.path.join(curpath,f))]
cuisines = {}
for fil in allFiles:
	if "menu" in fil:
		try:
			f = open(curpath+"/"+fil)
			fLine = f.readline().replace('\n','')
			if fLine in cuisines:
				cuisines[fLine].append(fil)
			else:
				cuisines[fLine] = list()
		except OSError as e:
			pass
for elements in cuisines:
	outFile = open(elements+".txt","w+")
	resList = cuisines[elements]
	for rest in resList:
		try:
			comF = open(curpath+"/"+rest.replace("menu","comment"))
			for line in comF:
				outFile.write(line)
		except OSError as e:
			pass
	convert(elements+".txt")

		
