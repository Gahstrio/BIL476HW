from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.common.exceptions import NoSuchElementException
f = open("ill.txt")
curpath = os.path.abspath(os.curdir)
driver = webdriver.Firefox()
for city in f:
	ff = open(os.path.join(curpath,city[:-1])+"/"+city[:-1]+".txt","r")
	for url in ff:
		driver.get(url)
		name = driver.find_element_by_xpath("//div[@class='restaurantName']").text.replace(' ','-')
		fCuisine = driver.find_elements_by_xpath("//script[@type='application/ld+json']")
		cuisine = 'Default'
		for elements in fCuisine:
			tx = elements.get_attribute('innerHTML').split(",")
			for e in tx:
				if "servesCuisine" in e:
					cuisine = e.split(":")[1].replace('[','').replace('"','').replace(']','').replace(' ','')
		fff = open(os.path.join(curpath,city[:-1])+"/"+city[:-1]+name+"-menu.txt","w+")
		fff.write(cuisine.encode("utf8")+'\n')
		meals = driver.find_elements_by_xpath("//div[@class='restaurantDetailBox None ']")
		for meal in meals:
			mealType = meal.find_element_by_xpath(".//div[@class='head white']")
			mealNames = meal.find_elements_by_xpath(".//div[@class='product-info']/a")
			mealPrices = meal.find_elements_by_xpath(".//span[@class='price']")
			for [mealName,mealPrice] in zip(mealNames,mealPrices):
				towrite = mealName.text+"|"+mealPrice.text+"&"+mealType.text+"\n"
				fff.write(towrite.encode("utf8"))
		fff.close()
		#fcomment = open(os.path.join(curpath,city[:-1])+"/"+city[:-1]+name+"-comment.txt","w+")
		#commentAll = open(os.path.join(curpath,city[:-1])+"/"+city[:-1]+"-allComments.txt","w+")
		#pagesHold = driver.find_element_by_xpath("//ul[@class='ys-commentlist-page pagination']")
		#pages = pagesHold.find_elements_by_xpath(".//li")		
		#count = 0
		#for page in pages:
		#	count = count + 1		
		#while(count > 0 ):
		#	count = count - 1
		#	newUrl = url+"?section=comments&page="+str(count)
		#	driver.get(newUrl)
		#	commentHold = driver.find_element_by_xpath("//div[@class='comments allCommentsArea']")
		#	comments = commentHold.find_elements_by_xpath(".//div[@class='comments-body']")
		#	for commentBlock in comments:
		#		try:
		#			comment = commentBlock.find_element_by_xpath(".//div[@class='comment row']/p").text
		#			dateFromToday = commentBlock.find_element_by_xpath(".//div[@class='commentDate pull-right col-md-4']").text
		#			points = commentBlock.find_element_by_xpath(".//div[@class='restaurantPoints col-md-12']")
		#			pointList = points.find_elements_by_tag_name('div')
		#			pointAsText = str()
		#			for p in pointList:
		#				pointAsText = pointAsText +" "+ p.text
		#			twr = pointAsText+"|"+dateFromToday+"&"+comment+"\n"
		#			fcomment.write(twr.encode("utf8"))
		#			commentAll.write(twr.encode("utf8"))
		#		except NoSuchElementException:
		#			pass	
		#fcomment.close()
		#commentAll.close()

			
		
		
	
