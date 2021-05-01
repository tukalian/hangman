# 独学プログラマー

#関数
def even_odd(x) :
    if x % 2 == 0:
        print('guusuu')
    else :
        print('kisuu')

even_odd(20)
even_odd(501)

def add_it(x=5, y=10):
    return x + y

result = add_it(100, 200)
print(result)

result = add_it()
print(result)

#スコープ：グローバル変数
x = 1
y = 2
def f():
    print(x)
    print(y)
f()

#スコープ：ローカル変数
def g():
    x = 5
    y = 6
    print(x)
    print(y)
g()






