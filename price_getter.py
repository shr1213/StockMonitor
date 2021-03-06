# coding=utf-8
'''
IsqQVc NprOob i49XU7Qb6iyI - zJFzKq8ukm8
IsqQVc NprOob iGWdbQsLV5hw - zJFzKq8ukm8
'''
import requests
import time
from bs4 import BeautifulSoup
import re


class PriceGetter():

    def __init__(self, stockcode):
        self.stockcode = stockcode

    def get_price(self):
        baseurl = ('http://finance.sina.com.cn/realstock/company/sz000977/nc.shtml')
        r = requests.get(baseurl)
        time.sleep(5)  # 避免网速低而加载过慢
        content = r.text
        soup = BeautifulSoup(content, 'lxml')
        divs = soup.find_all(class_='up')
        print(divs)

pg = PriceGetter("000977")
pg.get_price()
'''
            if divs == []:
                divs = soup.find_all(class_='green')
                if divs == []:
                    print('获取失败，记录错误...')
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logging error...')
                    with open('C:\\Users\\sunhaoran\\Documents\\fund_log.txt', 'a', encoding='UTF-8')as f:
                        f.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                        f.write(str(soup))
                        f.write('============================================================')
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + 'logged...')
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '数据获取失败，五分钟后将重试')
                    time.sleep(300)
                else:
                    status = 0  # 0代表DOWN
                    break
            else:
                status = 1  # 1代表UP
                break
        worth = divs[0].get_text()
        extent = divs[1].get_text()
        extent = float(extent.strip('%'))
        extent = extent / 100
        return status, worth, extent
'''
