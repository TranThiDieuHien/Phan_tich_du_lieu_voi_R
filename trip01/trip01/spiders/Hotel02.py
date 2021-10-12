import scrapy
import re
from ..items import Trip01Item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
import time




class Hotel02Spider(scrapy.Spider):
    name = 'Hotel02'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotel_Review-g293926-d2350513-Reviews-Jade_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d625203-Reviews-Alba_Spa_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d19690646-Reviews-Diep_s_Homestay_Hue-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d15353391-Reviews-Baly_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d302838-Reviews-Hotel_Saigon_Morin-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d613690-Reviews-Thai_Binh_Hotel_2-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d583457-Reviews-Asia_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d19000530-Reviews-Hue_Mate_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d1482849-Reviews-Romance_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d1959306-Reviews-Hong_Thien_Hotel_1-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d17563213-Reviews-Anh_s_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d10433427-Reviews-Hue_Ecolodge-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d17657058-Reviews-Hue_Melody_Hostel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d12997740-Reviews-Sala_Homestay_Hue-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d19706715-Reviews-Tam_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d13976982-Reviews-Stop_and_Go_Boutique_Homestay_Hue-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d18849313-Reviews-Hue_Lotus_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d15662131-Reviews-Hung_Long_Hostel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d20031555-Reviews-Lam_Garden_Boutique_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d1230773-Reviews-Sunny_B_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d18980023-Reviews-Amy_Hostel_Hue-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d1650568-Reviews-Why_Not_Hostel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d7388707-Reviews-Thanh_Lich_Hue_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d623907-Reviews-ORCHID_HOTEL-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d14009712-Reviews-Tam_Family_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d13163700-Reviews-Timothy_Homestay-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d17750042-Reviews-La_Habana_House-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d3794254-Reviews-Hue_Royal_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d582872-Reviews-Pilgrimage_Village-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d1790391-Reviews-Canary_Hotel-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com/Hotel_Review-g293926-d15113220-Reviews-Vinpearl_Hotel_Hue-Hue_Thua_Thien_Hue_Province.html']
     

    
    
    def parse(self, response):
        hotel_name = response.xpath('//h1[@id="HEADING"]/text()').get()
        #<div class="ui_column is-12-tablet is-9-mobile bgVDn P"><div class="eIsCM f"><h1 class="fkWsC b d Pn" id="HEADING">Jade Hotel</h1></div><div class="eCOqA f Mc"><a class="fbhUA q eRJGA _T Gi" href="#REVIEWS"><span class="ui_bubble_rating bubble_50"></span><span class="HFUqL">2,509 reviews</span></a><div class=""><span class="daVAz f e _Y"></span></div><div class="KeVaw"><span><b class="rank">#16</b> of 208 <a href="/Hotels-g293926-Hue_Thua_Thien_Hue_Province-Hotels.html">Hotels in Hue</a></span></div></div></div>
        rank = response.xpath('//b[@class="rank"]/text()').get()
        #<div class="cNJsa">Excellent</div>
        review = response.xpath('//div[@class="cNJsa"]/text()').get()
        #<span class="ceIOZ yYjkv">43 Hung Vuong, Hue 0543 Vietnam</span>
        address = response.xpath('//span[@class="ceIOZ yYjkv"]/text()').get()
        #<span class="bpwqy VyMdE">105</span>
        restaurant_nearby = response.xpath('//span[@class="bpwqy VyMdE"]/text()').get()
        item = Trip01Item()
        item["Hotel_name"] = hotel_name
        item["Rank"] = rank
        item["Review"] = review
        item["Address"] = address
        item["Restaurant_nearby"] = restaurant_nearby

        yield item
        pass
