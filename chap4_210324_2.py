# 独学プログラマー

#例外処理

try:
    a = input('type a number:')
    b = input('type b number:')
    a = int(a)
    b = int(b) 
    print(a / b)
except(ZeroDivisionError, ValueError):
    print('Invalid input')    




