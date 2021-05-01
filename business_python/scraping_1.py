import urllib.request

url = 'https://www.nikkei.com/markets/kabu/'

res = urllib.request.urlopen(url)

html = res.read().decode('utf-8')

print(html)