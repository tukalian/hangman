import matplotlib.pyplot as plt
import math
import numpy as np

x = np.linspace(0, 5 * math.pi)
y = np.sin(x)

plt.title('正弦波')
plt.xlabel('時間[t]')
plt.ylabel('振幅[V]')
plt.plot(x, y, label='sin')
plt.legend()
plt.show()
