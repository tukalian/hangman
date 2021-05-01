import urllib.request

url = 'https://www.nikkei.com/markets/kabu/'
res = urllib.request.urlopen(url)
html = res.read().decode('utf-8')

f = open('kabu.html', 'w', encoding='utf-8')
f.write(html)
f.close()

print('kabu.htmlに書き込みました')