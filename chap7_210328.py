# 独学プログラマー

# for
name = 'Ted'
for a in name:
    print(a)

tv = ['got', 'nacros', 'vice']
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    print(show)
    i += 1
print(tv)

tv = ['got', 'nacros', 'vice']
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

print('\n')


asamesi = ['gohan', 'misosiru', 'nattou']
dessert = ['MIKAN', 'RINGO', 'Banana']
kondate = []

for show in asamesi:
    show = show.upper()
    kondate.append(show)

for show in dessert:
    show = show.lower()
    kondate.append(show)

print(kondate)