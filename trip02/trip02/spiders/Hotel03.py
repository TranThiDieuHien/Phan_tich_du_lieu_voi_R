import scrapy
from..items import Trip02Item
from selenium import webdriver
from scrapy.utils.project import get_project_settings


class Hotel03Spider(scrapy.Spider):
    name = 'Hotel03'
   #allowed_domains = ['tripadvisor.com']
    #start_urls = ['https://www.tripadvisor.com/Hotel_Review-g293926-d2350513-Reviews-Jade_Hotel-Hue_Thua_Thien_Hue_Province.html']

        
    def start_requests(self):
        url = ['https://www.tripadvisor.com/Hotels-g293926-Hue_Thua_Thien_Hue_Province-Hotels.html/',
            'https://www.tripadvisor.com/Hotels-g293926-oa30-Hue_Thua_Thien_Hue_Province-Hotels.html',
            'https://www.tripadvisor.com/Hotels-g293926-oa60-Hue_Thua_Thien_Hue_Province-Hotels.html'
            ]
        for item in url:
            settings= get_project_settings()
            driver_path = settings['CHROME_DRIVER_PATH']
            options= webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(driver_path, options=options)
            driver.get(item)
            link_elements = driver.find_elements_by_xpath(
                 '//*[@data-prwidget-name="meta_hsx_responsive_listing"]//a[text()]'
            )
            for link in link_elements:
                yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
            driver.quit()

    

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
        #<span class="bpwqy dfNPK">93</span>
        GFW = response.xpath('//span[@class="bpwqy dfNPK"]/text()').get()
        #<span class="bpwqy eKwbS">14</span>
        Attractions = response.xpath('//span[@class="bpwqy eKwbS"]/text()').get()
        #<span class="btQSs q Wi z Wc">2,509 reviews</span>
        review_number = response.xpath('//span[@class="btQSs q Wi z Wc"]/text()').get()
        #<div class="ui_column  is-3-tablet is-shown-at-tablet "><div class="cMImN b S4 H4">Language</div><ul class="mPill w S4"><li class="ui_radio dQNlC"><input id="LanguageFilter_0" type="radio" value=""><label for="LanguageFilter_0" class="bahwx Vm _S"><span class="fwSIg q">All languages</span><span class="cvxmR">(2,509)</span></label></li><li class="ui_radio dQNlC"><input id="LanguageFilter_1" type="radio" value="en" checked=""><label for="LanguageFilter_1" class="bahwx Vm _S"><span class="fwSIg q">English</span><span class="cvxmR">(1,905)</span></label></li><li class="ui_radio dQNlC"><input id="LanguageFilter_2" type="radio" value="fr"><label for="LanguageFilter_2" class="bahwx Vm _S"><span class="fwSIg q">French</span><span class="cvxmR">(224)</span></label></li><li class="ui_radio dQNlC"><input id="LanguageFilter_3" type="radio" value="de"><label for="LanguageFilter_3" class="bahwx Vm _S"><span class="fwSIg q">German</span><span class="cvxmR">(111)</span></label></li><div class="dbKhu b _S"><span class="text">More</span></div></ul></div>
        languages = response.xpath('//span[@class="fwSIg q"]/text()').getall()
        #<label for="TravelTypeFilter_0" class="Oixff Vm _S">Families</label>
        traveltype = response.xpath('//label[contains(@for, "TravelTypeFilter")]/text()').getall()
        #<div class="cJdpk Ci">₫340,909<!-- --> - <!-- -->₫590,909<!-- --> <!-- -->(Based on Average Rates for a Standard Room) </div>
        min_price =  response.xpath('//div[@class="cJdpk Ci"]/text()')[0:1].getall()
        max_price = response.xpath('//div[@class="cJdpk Ci"]/text()')[2:3].getall()
        price_range = response.xpath('//div[@class="cJdpk Ci"]/text()')[0:3].getall()
        room = response.xpath('//div[@class="cJdpk Ci"]/text()')[-1].getall()
        ##<span class="cXdRV"> (48) </span>
        traveler_pic = response.xpath('//span[@class="cXdRV"]/text()')[0:3].getall()
        number_room_dining = response.xpath('//span[@class="cXdRV"]/text()')[-2].getall()
        number_room_suite = response.xpath('//span[@class="cXdRV"]/text()')[-5].getall()
        item = Trip02Item()
        item["Hotel_name"] = hotel_name
        item["Rank"] = rank
        item["Review"] = review
        item["Address"] = address
        item["Restaurant_nearby"] = restaurant_nearby
        item["number_images_Traveler"] = traveler_pic
        item["Review_number"] = review_number
        item["Great_for_walker"] = GFW
        item["Attractions"] = Attractions
        item["languages"] = languages
        item["Travel_types"] = traveltype
        item["Price_min"] = min_price
        item["Price_max"] = max_price
        item["Price_range"] = price_range
        item["Room_number"] = room
        item["number_room_suite"] = number_room_suite
        item["number_room_dining"] = number_room_dining
        yield item
        pass
        pass

