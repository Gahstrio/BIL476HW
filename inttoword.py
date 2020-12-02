def itw(filename):
	worddict = {}
	wordF = open("wordict.txt","r")
	for line in wordF:
		word,val = line.split(":")[0],line.split(":")[1]
		val = val.replace("\n","")
		print(word+"@@"+val+"@@")
		worddict[val] = word
	convertFile = open(filename,"r")
	converted = open("asword"+filename,"w+")
	for line in convertFile:
		freq = line.split("#")[0].split(" ")
		for el in freq:
			if el:
				converted.write(worddict[el]+"\n")
itw("allcommentsfrequent.txt")
				
