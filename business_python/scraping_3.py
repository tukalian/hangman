import urllib.request
import re

url = 'https://www.nikkei.com/markets/kabu/'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')

r = re.compile('<span class="mkc-stock_prices">(¥d+[,.])*¥d+</span>')
m = r.search(html)
s = m.group(0)
print(s)

s = re.sub('<.*?>', '', s)
print('日経平均株価:' + s)
