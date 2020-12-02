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
		word = word.replace("\n","")
		if word in wordDict:
			pass
		else:
			wordDict[word] = i
			i = i +1
	f1 = open("asInt"+fileName,"w+")
	f2 = open("wordict.txt","w+")
	print(wordDict)
	for element in wordDict:
		f2.write(element + ":" + str(wordDict[element])+"\n")
	f2.close()
	f.close()
	f = open(fileName,"r")
	for line in f:
		line = line.split('&')[1]
		print(line)
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
for i in range(1,10):
	convert("avg"+str(i)+"points.txt")	
