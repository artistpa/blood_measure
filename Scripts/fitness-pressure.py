import matplotlib.pyplot as plt
import csv
import numpy as np
with open('fitness.csv') as f1:
    r1 = csv.reader(f1)
    x1 = []
    for line in r1:
          x1.extend(map(float, line))
x=np.linspace(0, 30, num=(len(x1)))
y=[(x1[i] * 0.096 - 4.516) for i in range (len(x1))]
print(y[34500])
# Построим графики
plt.plot(x, y, 'g', label='P - 133/73 [мм рт. ст.]')
plt.plot(x[34500],y[34500],'ro', label='Систола')
plt.plot(x[245000],y[245000],'bo', label='Диастола')
# Подпишем оси
plt.xlabel('Время, c')
plt.ylabel('Давление, мм рт. ст.')
# И график целиком
plt.title("Артериальное давление после физической нагрузки")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([0,30])
plt.legend()
plt.show()