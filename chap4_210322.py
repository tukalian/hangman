# 独学プログラマー

#関数
def func1(x) :  #引数あり
    return x * 2
print(func1(3))


def func2() :   #引数なし
    return 3 * 9 - 2
print(func2())


def func3(x, y, z) :   #引数なし
    return 3 * 9 - 2 + x + y + z 
print(func3(3, 2, 1))


#組み込み関数
print(len("tensaibakabon"))     #文字列の長さを出力

print(str(100))

age = input('年齢を入力：')
int_age = int(age)

if int_age == 33 :
    print('○')
else :
    print('×')