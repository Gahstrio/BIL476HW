import scrapy
import os
class commentsSpider(scrapy.Spider):
	name = "commentsSpider"
	def getCities(self):
	
		cities = ["kastamonu","kayseri","kirklareli","kirsehir","kocaeli","konya","kutahya","malatya","manisa","kahramanmaras",
			"mardin","mersin","mugla","nevsehir","nigde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdag",
			"tokat","trabzon","sanliurfa","usak","van","yozgat","zonguldak","aksaray","karaman","kirikkale","batman","bartin",
			"igdir","yalova","karabuk","osmaniye","duzce"]
		return cities
	def start_requests(self):
		urls = []
		cities = self.getCities()
		rootDir = "/home/gahstrio/Desktop/476Odev"
		for line in cities:
			line = line.replace("\n","")
			restaurants = open(rootDir+"/"+line+"/"+line+".txt")
			for ur in restaurants:
				urls.append(ur.replace("\n",""))
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse, meta = {
					'splash':{
						'endpoint': 'render.html',
						'args': {'wait': 0.5}
					}
				}, dont_filter=True)			
						
	def commentParse(self,response):
		rootDir = "/home/gahstrio/Desktop/476Odev"
		name = response.xpath("//div[@class='restaurantName']/p").xpath('string(.)').get()
		if name is None:
			return
		name = name.replace(' ','-').replace('(','').replace(')','').replace('.','').replace(',','')
		fCuisine = response.xpath("//script[@type='application/ld+json']")
		cityName = "Default"
		for elements in fCuisine:
			tx = elements.xpath('string(.)').get().split(",")		
			for e in tx:
				if "areaServed" in e:
					cityName = e.split(":")[1].replace(' ','').replace('"','')
		fff = open(cityName+name+"-comments.txt","a")			
		commentHold = response.xpath("//div[@class='comments allCommentsArea']/div[@class='comments-body']")
		comments = commentHold.xpath(".//div[@class='comments-body']")
		for commentBlock in commentHold:
			comment = commentBlock.xpath(".//div[@class='comment row']/p").xpath('string(.)').get()
			if comment is None:
				continue
			dateFromToday = commentBlock.xpath(".//div[@class='commentDate pull-right col-md-4']").xpath('string(.)').get()
			points = commentBlock.xpath(".//div[@class='restaurantPoints col-md-12']/div").xpath('string(.)')
			pointAsText = str()
			for p in points:
				pointAsText = pointAsText +" "+ p.get()
			twr = pointAsText+"|"+dateFromToday+"&"+comment+"\n"
			fff.write(twr)
		fff.close()
	def parse(self,response):
		rootDir = "/home/gahstrio/Desktop/476Odev"
		name = response.xpath("//div[@class='restaurantName']/p").xpath('string(.)').get()
		if name is None:
			return
		name = name.replace(' ','-').replace('(','').replace(')','').replace('.','').replace(',','')
		fCuisine = response.xpath("//script[@type='application/ld+json']")
		cuisine = 'Default'
		cityName = "Default"
		for elements in fCuisine:
			tx = elements.xpath('string(.)').get().split(",")		
			for e in tx:
				if "areaServed" in e:
					cityName = e.split(":")[1].replace(' ','').replace('"','')
				if "servesCuisine" in e:
					cuisine = e.split(":")[1].replace('[','').replace('"','').replace(']','').replace(' ','')
		fff = open(cityName+name+"-menu.txt","w+")
		fff.write(cuisine+'\n')
		meals = response.xpath("//div[@class='restaurantDetailBox None ']")
		for meal in meals:
			mealType = meal.xpath(".//div[@class='head white']/h2").xpath('string(.)')
			mealNames = meal.xpath(".//div[@class='product-info']/a/text()")
			mealPrices = meal.xpath(".//span[@class='price']/text()")
			for [mealName,mealPrice] in zip(mealNames,mealPrices):
				towrite = mealName.get()+"|"+mealPrice.get()+"&"+mealType.get()+"\n"
				fff.write(towrite)
		fff.close()
		pageContainer = response.xpath("//ul[@class='ys-commentlist-page pagination']/li")
		maxPage = 0
		for page in pageContainer:
			if int(page.xpath('string(.)').get()) > maxPage:
				maxPage = int(page.xpath('string(.)').get())
		for i in range(1,maxPage+1):
			
			newUrl = response.meta['splash']['args']['url']+"?section=comments&page="+str(i)
			print("Visiting url:"+newUrl)
			yield scrapy.Request(url = newUrl, callback = self.commentParse, meta = {
					'splash':{
						'endpoint': 'render.html',
						'args': {'wait': 0.5}
					}
				},dont_filter = True)	
		














