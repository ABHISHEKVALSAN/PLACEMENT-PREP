from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setDriverOptions():
	options 				= Options()
	options.binary_location = "/usr/bin/chromium-browser"
	#options.add_argument("--headless")
	options.add_argument("--start-maximized");
	options.add_argument("--window-position=1367,0")
	return	webdriver.Chrome(chrome_options=options)

url="http://placement.iitk.ac.in"
driver			= setDriverOptions()
driver.get(url)
driver.implicitly_wait(3)
username = driver.find_element_by_id("id_username")
password = driver.find_element_by_id("id_password")
username.send_keys("abhiavk")
password.send_keys("BUP3Y2Ja9X")
login_attempt = driver.find_element_by_xpath("//*[@type='Submit']")
login_attempt.submit()
url+="/jaf_view/"
for i in xrange(199,300):
    try:
        driver.implicitly_wait(3)
        driver.get(url+str(i))
        page_source=driver.page_source
        soup=BeautifulSoup(page_source,'html.parser')
        compName=soup.findAll("td")[3].text
        print(i,compNmae)
        f = open(compName+'.html'  , 'w')
        f.write(page_source.encode('utf-8'))
        f.close()
    except:
        print(i)
