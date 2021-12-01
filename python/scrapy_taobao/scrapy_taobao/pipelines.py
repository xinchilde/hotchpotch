# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

'''
pipeline（管道）能够实现数据的清洗和保存，能够定义多个管道实现不同的功能，常用的方法有：
    process_item(self,item,spider): 
        a.管道类中必须有的函数
        b.实现对item数据的处理
        c.必须有return item
    open_spider(spider):    在爬虫开启的时候执行一次
    close_spider(spider):   在爬虫关闭的时候执行一次

pipeline使用注意点：
 1.使用之前需要在settings中开启
 2.pipeline在setting中 键表示位置（即pipeline在项目中的位置可以自定义），值表示距离引擎的远近，越近数据会越先经过：权重值小的优先执行
 3.有多个pipeline的时候，process_item的方法必须return item，否则后一个pipeline取到的数据为None值
 4.pipeline中process_item的方法必须有，否则item没有办法接收和处理
 5.process_item方法接收item和spider，其中spider表示当前传递item过来的spider
 6.open_spider(spider):能够在爬虫开启的时候执行一次
 7.close_spider(spider):能够在爬虫关闭的时候执行一次
 8.上述两个方法经常用于爬虫和数据库的交互，在爬虫开启的时候建立和数据库的连接，在爬虫关闭的时候断开和数据库的连接

思考：在setting中能够开启多个管道，为什么需要开启多个？
 1.不同的pipeline可以处理不同爬虫的数据，通过spider.name属性来区分
 2.不同的pipeline能够对一个或者多个爬虫进行不同的数据处理的操作，比如一个进行数据清洗，一个进行数据的保存
 3.同一个管道类也可以处理不同爬虫的数据，通过spider.name属性来区分
'''
class ScrapyTaobaoPipeline:
    def process_item(self, item, spider):
        return item
