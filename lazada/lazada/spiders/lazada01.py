import scrapy
import re
from ..items import LazadaItem


class Lazada01Spider(scrapy.Spider):
    name = 'lazada01'
    allowed_domains = ['lazada.vn']
    start_urls = ['https://www.lazada.co.id/products/gamispakaian-wanitabusana-wanita-termurah-ukuran-jumbo-rayon-twill-i5738234168-s11190718863.html?spm=a2o4j.searchlistcategory.list.1.4d016885OZD5oD&search=1&freeshipping=1',
                  'https://www.lazada.co.id/products/gamis-syari-syari-arabian-lengan-panjang-renda-dada-jumbo-l-fit-to-xxl-terlaris-2021-i5636218022-s11078880068.html?spm=a2o4j.searchlistcategory.list.12.4d0168859FPVGS&search=1']

    def parse(self, response):
        #<h1 class="pdp-mod-product-badge-title" data-spm-anchor-id="a2o4n.pdp_revamp.0.i0.7001594b3uSzoB">COOLMATE Áo thun nam Cotton Compact ngắn tay phiên bản Premium chống nhăn, thoáng mát nhiều màu</h1>
        name = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        #<span class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl" data-spm-anchor-id="a2o4j.pdp_revamp.0.i4.5374460fXeWzZg">Rp108.500</span>
        price = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        #<div class="location__address" data-spm-anchor-id="a2o4j.pdp_revamp.delivery_options.i1.28e7687aH3UP3w">DKI Jakarta, Kota Jakarta Barat, Cengkareng</div>
        address = response.xpath('//div[@class="location__address"]/text()').get()
        item = LazadaItem()
        item["name"] = name
        item['price'] = price
        item["address"] = address
        yield item
        pass
