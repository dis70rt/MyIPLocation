#  URL
#  Search Box
#  Search Button

from selenium import webdriver
import geocoder

class MyIPLocation:
    
    def __init__(self):
        self.browser = webdriver.Chrome("Chromedriver.exe")
        self.browser.get('https://www.google.co.in/maps')
        
    def toLocate(self,latitide,longitude):
        element = self.browser.find_elements_by_xpath('//*[@id="searchboxinput"]')[0]
        element.send_keys(str(latitide),",",str(longitude))
        
        click_element = self.browser.find_elements_by_xpath('//*[@id="searchbox-searchbutton"]')[0]
        click_element.click()
        

add = MyIPLocation()

g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]

add.toLocate(lat, lng)
