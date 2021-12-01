import scrapy
from scrapy_taobao.items import ScrapyTaobaoItem

'''
1.回顾之前模拟登录的三种方法：
 1.1 requesr模块是如何实现模拟登录？
    a.直接携带cookies请求页面
    b.找url地址，发送post请求储存cookie
 1.2 selenium是如何模拟登录的？
 1.3 scarapy模拟登录
    a.直接携带cookies
    b.找url地址，发送post请求存储cookie
 
2.scrapy携带cookie直接获取需要登录后的页面
 应用场景：
    a.cookie过期时间很长，常用于一些不和规范的网站
    b.能在cookie过期之前把所有的数据拿到
    c.配合其他程序使用，比如使用selenium把登录之后的cookie获取保存到本地，scrapy发送请求之前先读取本地cookie

3.字符串与字节数组互转：
 1. bytes --> str :
 bytes_data = b'message'
    # 方法一：
    str_data = str(bytes_data, encoding = 'utf-8')
    # 方法二：
    str_data = bytes_data.decode('utf-8')
    
 2. str --> bytes :
 str_data = 'message'
    # 方法一：
    bytes_data = bytes(str_data, encoding = 'utf-8')
    # 方法二：
    bytes_data = str_data.encode('utf-8')
    
    
4. scrapy.Request的更多参数：
    scrapy.Request(url,[,rallback,method="GET",headers,body,cookies,meta,dont_filter=Flase])
    参数解释：
     a.中括号里面的参数为可选参数
     b.callback: 表示当前的url的响应交给哪个函数去处理
     c.meta:实现数据在不同的解析函数中传递，meta默认带有部分数据，比如下载延迟，请求深度等
     d.dont_filter:默认为Flase，会过滤请求的url地址，即请求过的url地址不会继续被请求，对需要重复请求的url地址可以把它设置为Ture,比如贴吧的翻页请求，
        页面的数据总是在变化；start_urls中的地址会被反复请求，否则程序不会启动
     e.method:指定POST或GET请求
     f.headers：接收一个字典，齐总不包括cookies
     g.cookies:接收一个字典，专门放置cookies
     h.body:接收json字符串，为POST的数据，发送payload_post请求时使用
     

5.关于scrapy.Request url与callback是一个组合，代表这个url对应的解析方法，而不是每次所有的新请求都会走self.parse，实质为callback指定的
'''

'''
登录地址：https://login.taobao.com/member/login.jhtml
https://s.taobao.com/search?q=oneplus&tab=old

代理网站： https://www.kuaidaili.com/free/
'''


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    # start_urls = ['http://taobao.com/']
    # start_urls = ['https://s.taobao.com/search?q=oneplus&tab=old']
    start_urls = [
        'https://item.taobao.com/item.htm?spm=a230r.1.14.1.582b6bef0Lip4J&id=657693859684&ns=1&abbucket=20#detail']

    # 通过设置cookie_cookie
    def start_requests(self):
        url = self.start_urls[0]
        temp = 'miid=52814753156143063; thw=cn; cna=T/gnGYzRpmgCAdzIBXQUUbXl; t=7ebc0f6fb8b1aadbb4aab2531bb779df; _samesite_flag_=true; ' \
               'cookie2=1b8d2998de66506d9095301dc8caceae; _tb_token_=7e33df6e8b575; xlly_s=1; ' \
               'sgcookie=E100qIEBspeQXKCSxF7qcUKPx3NQO34zu0wOlM8ZszRHHhVaXr5GC0IEsA+XLpj86+fhgogqJcF9eF+eOQunX3rBdblAyh9pVrThxCCAkkyY9lE=; ' \
               'unb=2665676119; uc3=id2=UU6nRCPwz76sDw==&vt3=F8dCvUj1q9fFSk3TqKM=&nk2=VvzzwGzkLBnGAVRFX2eV&lg2=W5iHLLyFOGW7aA==; ' \
               'csg=81a44e90; lgc=520\u4EF0\u671B\u661F\u8FB01314; cancelledSubSites=empty; cookie17=UU6nRCPwz76sDw==; dnk=520\u4EF0\u671B\u661F\u8FB01314; ' \
               'skt=405cfc9f7c760991; existShop=MTYzODM2MDk0NA==; uc4=id4=0@U2xqIFXJBM5azRA8p6wvSrL6yhvM&nk4=0@VHrFiqtYDz7AkKLbKNMVsS00ozHSG/a8Ao4=; ' \
               'tracknick=520\u4EF0\u671B\u661F\u8FB01314; _cc_=URm48syIZQ==; _l_g_=Ug==; sg=493; _nk_=520\u4EF0\u671B\u661F\u8FB01314; ' \
               'cookie1=BxJIue//2vquIrzMPnvCQBCTIaQfJP+qYanMk7cIbZU=; mt=ci=11_1; _m_h5_tk=7c281bd1dbb26cc5094c0d634d2a4cef_1638371414259; ' \
               '_m_h5_tk_enc=40baac8d9d27aca6e70c83b2b1a1d5c0; uc1=pas=0&cookie21=URm48syIYB3rzvI4Dim4&existShop=false&cookie15=UIHiLt3xD8xYTw==&cookie14=Uoe3f4OlUH/1/w==&cookie16=UtASsssmPlP/f1IHDsDaPRu+Pw==; ' \
               'enc=d8C3xTgp316OHK/IQFWSt6XnF2pSEB/oYNojtQLCsU4zFZJBs1P8xGQNs37vg4BYw3u/n0yyRv39HqzleCtJKg==; hng=CN|zh-CN|CNY|156; ' \
               'UM_distinctid=17d75ec9a8fb2c-0d767a43cb40a8-5919135e-1fa400-17d75ec9a90d7c; l=eBN2JW2PjMTnm3fYBO5Cnurza779PQAb4sPzaNbMiInca1-5OUYhZNCdqBcp5dtjgtCFheKzyZKXvRLHR3fRwxDDB3h2q_oqExvO.; ' \
               'isg=BNXVMXbQGLOrtz1QF2qfD-p75NGP0onkWkKj81d4tcz4rvWgHiDUtBwveLIYrqGc; tfstk=czQOBFT2XJ2gSUddaGEhlqMCw02labwvdf9mkWOsq9imP8uqos2lrahstlOXUdFd.'
        cookies = {data.split('=')[0]: data.split('=')[1] for data in temp.split("; ")}
        yield scrapy.Request(url=url, callback=self.parse, cookies=cookies)

    # 通过发送post请求设置cookie
    def start_requests_post(self):
        # 从登录页面响应中提取post数据
        token = ''
        post_data = {
            "name": "",
            "password": "exile_morqanna"
        }
        # 针对登录url发送post请求
        yield scrapy.FormRequest(url="post请求地址", callback=self.parse, formdata=post_data)

    def parse(self, response):
        # print(response.body.decode(encoding='utf-8'))
        # 下载列表页面
        # download_page('taoboa_detail.html',response)

        # 获取所有商品信息
        commodity_list = response.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div')
        # 遍历商品
        for commodity in commodity_list:
            scrapyTaobaoItem = ScrapyTaobaoItem()
            # 1.图片部分
            pic_box = commodity.xpath('./div[contains(@class,"pic-box")]')
            # 商品图片
            scrapyTaobaoItem['img'] = pic_box.xpath('//div[@class="pic"]//img/@src').extract_first()
            # 详情地址
            detail_href = pic_box.xpath('//div[@class="pic"]//a/@href').extract_first()
            # response.urljoin()用户拼接相对路径的url,可以理解成自动补全

            # 2.文字部分
            ctx_box = commodity.xpath('./div[contains(@class,"ctx-box")]')
            # 价格
            scrapyTaobaoItem['price'] = ctx_box.xpath('//div[contains(@class,"price")]/strong/text()')
            # 付款人数
            scrapyTaobaoItem['sales_volume'] = ctx_box.xpath('//div[@class="deal-cnt"]/text()')
            # 标题
            scrapyTaobaoItem['title'] = ctx_box.xpath('./div[@class="row row-2 title"]/text()')
            # 卖家
            scrapyTaobaoItem['seller'] = ctx_box.xpath('//div[@class="row row-3 g-clearfix"]/a/span/text()')
            # 地址
            scrapyTaobaoItem['location'] = ctx_box.xpath('//div[@class="row row-3 g-clearfix"]/div[@class="location"]/text()')

            # 返回信息
            print(scrapyTaobaoItem)
            # yield scrapyTaobaoItem
            # 构建详情页页面的请求
            yield scrapy.Request(url='', callback=self.parse_detail, meta={'item': scrapyTaobaoItem})

        # 获取下一页地址
        part_url = response.xpath('//*[@id="mainsrp-pager"]/div/div/div/ul/li[last()]')
        # 判断最后的li class是否包含next-disabled
        # 判断终止条件
        if part_url !='javasc(0)':
            next_url = response.urljoin(part_url)
            # 构建请求对象，并且返回给引擎
            yield scrapy.Request(url=next_url,callback=self.parse)

    # 详情解析方法
    def parse_detail(self, response):
        # 下载详情页面
        # download_page('taoboa_detail.html', response)
        scrapyTaobaoItem = response.meta['item']
        '''
          ...........省略操作步骤
        '''
        # 添加上详情的内容的之后 返回给引擎
        yield scrapyTaobaoItem


# 下载页面
def download_page(fileName, response):
    print('获取结果')
    with open(fileName, 'wb')as f:
        f.write(response.body)
