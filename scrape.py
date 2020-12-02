from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
def scroll_to_bottom(driver):
	item_nb = [0,1]
	while (item_nb[-1] > item_nb[-2]):
		items = driver.find_elements_by_xpath("//div[@class='restaurant-display-name']/a")
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
		time.sleep(5)
		item_nb.append(len(items))

f = open('ill.txt')
cities = []
for x in f:
	x = x[:-1]
	cities.append(x)
urlBody = 'https://www.yemeksepeti.com'
urls = []
curpath = os.path.abspath(os.curdir)
for city in cities:
	urls.append(urlBody+'/'+city+'/restoran-arama')
driver = webdriver.Firefox()
restURl = []
for url,city in zip(urls,cities):
	f = open(os.path.join(curpath,city+"1.txt"),"w+")
	driver.get(url)
	time.sleep(10)
	dialog = driver.find_element_by_xpath("//div[@class='restaurant-display-name']/a")
	last_scroll_height = 0
	scroll_to_bottom(driver)
	elem = driver.find_elements_by_xpath("//div[@class='restaurant-display-name']/a")
	for element in elem:
		f.write(element.get_attribute('href')+"\n")
	f.close()
driver.close()













