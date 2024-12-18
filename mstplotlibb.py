import matplotlib.pyplot as plt
import numpy as np
x =np.array([1, 2, 3, 4, 5])
y =np.array([1, 4, 9, 16, 25])

plt.plot(x, y)

plt.xlabel("X o'qi", fontsize=12, color='purple')
plt.ylabel("Y o'qi", fontsize=12, color='blue')

plt.title("X va Y o'qlar grafigi", fontsize=14)
plt.plot(y,'r--3')
plt.show()
