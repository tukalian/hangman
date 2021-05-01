import numpy as np

r = np.random.randint(0, 10, 10)
print('ランダムな配列:{}'.format(r))
print('平均値:{}'.format(np.mean(r)))
print('標準偏差:{}'.format(np.std(r)))