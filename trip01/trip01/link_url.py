# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:47:16 2021

@author: Admin
"""

import scrapy

class urlItem(scrapy.Item):
    url_name = scrapy.Field()
    pass

class n(scrapy.Spider):
    
    t = 'https://www.tripadvisor.com/Hotels-g293926-Hue_Thua_Thien_Hue_Province-Hotels.html'
    def nn(self, response):
    #<div class="listing_title"><a target="_blank" href="/Hotel_Review-g293926-d2350513-Reviews-Jade_Hotel-Hue_Thua_Thien_Hue_Province.html" id="property_2350513" class="property_title prominent " data-clicksource="HotelName" onclick="return false;" dir="ltr">      Jade Hotel</a></div>
        link = response.xpath('//div[@class="listing_title"]/text()').get()
        links = urlItem()
        links['url_name'] = link
        yield links
        pass
        
