#/usr/bin/env python
import sys
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
body='''
<html>
    <body>
        <h1>Hello World</h1>
        <h1>Hello Scrapy</h1>
        <b>Hello python</b>
        <ul>
            <li>C++</li>
            <li>Java</li>
            <li>Python</li>
        </ul>
    </body>
</html>
'''
response=HtmlResponse(url='http://www.example.com',body=body,encoding='utf8')
selector=Selector(response=response)
selector_list=selector.xpath('//h1')
print(sys._getframe().f_lineno,'行:')
print(selector_list)
print('\n')


print(sys._getframe().f_lineno,'行:')
for sel in selector_list:
    print(sel.xpath('./text()'))
print('\n')


print(sys._getframe().f_lineno,'行:')
print(selector_list.xpath('./text()'))
print('\n')

print(sys._getframe().f_lineno,'行:')
print(selector.xpath('.//ul').css('li').xpath('./text()'))
print('\n')



print(sys._getframe().f_lineno,'行:')
sl=selector.xpath('.//li')
print(sl)
print(sl[0].extract())
print('\n')

print(sys._getframe().f_lineno,'行:')
sl=selector.xpath('//li/text()')
print(sl)
print(sl[1].extract())
print('\n')

print(sys._getframe().f_lineno,'行:')
print(sl.extract())
print('\n')
