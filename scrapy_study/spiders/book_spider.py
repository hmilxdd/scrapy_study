
# -*- coding: utf-8 -*-

import scrapy

class BooksSpider(scrapy.Spider):
#每一个爬虫的唯一标识
    name="books"
    #定义爬虫爬取的起点，起始点可以是多个，这里只有一个
    start_urls=['http://books.toscrape.com/']

    def parse(self,response):
        #提取数据
        #每一本书的信息在<aritcle class="product_pod">中，我们使用
        #css()方法找到所有这样的article元素，并依次迭代
        for book in response.css('article.product_pod'):

            #书名信息在article > h3 > a元素的title属性里
            name=book.xpath('./h3/a/@title').extract_first()

            #书价信息在<p class="price_color">的text中.
            price=book.css('p.price_color::text').extract_first()

            yield {
                'name':name,
                'price':price,
            }
            
        #提取链接
        #下一页的url在ul.pager > li.next >a 里面
        #例如:<li class="next"><a href="catalogue/page-2.html">next</a></li>
        next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            #如果找到下一页的url,得到绝对路径,构造新的Request对象
            next_url=response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
