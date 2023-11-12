import matplotlib.pyplot as plt
import csv
import numpy as np
with open('rest.csv') as f1:
    r1 = csv.reader(f1)
    x1 = []
    for line in r1:
          x1.extend(map(float, line))
x=np.linspace(0, 30, num=(len(x1)))
y=[(x1[i] * 0.096 - 4.516) for i in range (len(x1))]
print(y[59500])
print(y[386900])
# Построим графики
plt.plot(x, y, 'g', label='P - 131/74 [мм рт. ст.]')
plt.plot(x[59500],y[59500],'ro', label='Систола')
plt.plot(x[386900],y[386900],'bo', label='Диастола')
# Подпишем оси
plt.xlabel('Время, c')
plt.ylabel('Давление, мм рт. ст.')
# И график целиком
plt.title("Артериальное давление до физической нагрузки")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([0,30])
plt.legend()
plt.show()