
# 入力
pa_in = 1
pa_zero = 10.1
pa_gain = 2

# 演算
zpa_zero = pa_in + pa_zero
zpa_gain = zpa_zero * pa_gain
sin_data = zpa_gain / (2 ** 15)


# 出力
print(sin_data)
print(int(sin_data))
print(type(zpa_zero))   # pythonはデータ型を自動で変えてくれる
