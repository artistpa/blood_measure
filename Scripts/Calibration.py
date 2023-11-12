import matplotlib.pyplot as plt
import csv
import numpy as np
with open('40-mmHg.csv') as f1:
    r1 = csv.reader(f1)
    x1 = []
    for line in r1:
          x1.extend(map(float, line))
with open('80-mmHg.csv') as f2:
    r2 = csv.reader(f2)
    x2 = []
    for line in r2:
          x2.extend(map(float, line))
with open('100-mmHg.csv') as f3:
    r3 = csv.reader(f3)
    x3 = []
    for line in r3:
          x3.extend(map(float, line))
with open('120-mmHg.csv') as f4:
    r4 = csv.reader(f4)
    x4 = []
    for line in r4:
          x4.extend(map(float, line))
with open('160-mmHg.csv') as f5:
    r5 = csv.reader(f5)
    x5 = []
    for line in r5:
          x5.extend(map(float, line))


y=np.array([0, 40, 80, 100, 120, 160])
a1 = np.mean(x1, axis = None)
a2 = np.mean(x2, axis = None)
a3 = np.mean(x3, axis = None)
a4 = np.mean(x4, axis = None)
a5 = np.mean(x5, axis = None)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

x = np.array([0, a1, a2, a3, a4, a5])
a = np.polyfit(x, y, 1, rcond=None, full=False, w=None, cov=False)
x = [i for i in range (2000)]
y = [(a[0] * i) + a[1] for i in range (2000)]
print(a)

# Построим графики, указав названия
plt.plot(y, x, 'b', label='P = 0,096 * N - 4.516 [мм рт. ст.]')
plt.plot(40, a1,'ro', label='Измерения')
plt.plot(80, a2,'ro')
plt.plot(100, a3,'ro')
plt.plot(120, a4,'ro')
plt.plot(160, a5,'ro')
# Подпишем оси
plt.ylabel('Показания АЦП')
plt.xlabel('Давление, мм рт. ст.')
# И график целиком
plt.title("Калибровочный график показаний АЦП от давления")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([35,165])
plt.ylim([480,2000])
plt.legend()
plt.show()