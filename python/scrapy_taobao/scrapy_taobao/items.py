# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品图片
    img = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 付款人数
    sales_volume = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 卖家
    seller = scrapy.Field()
    # 地址
    location = scrapy.Field()
