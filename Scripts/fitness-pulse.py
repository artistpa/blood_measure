import matplotlib.pyplot as plt
import csv
import numpy as np
with open('fitness.csv') as f1:
    r1 = csv.reader(f1)
    x1 = []
    for line in r1:
          x1.extend(map(float, line))
x = np.linspace(0, 30, num=447)
y = [(x1[i] * 0.096 - 4.516) for i in range (len(x1))]
y1 = [(y[i+1]-y[i]) for i in range (0, len(x1)-1, 998)]
print(len(y1))
k = 0
i = 0
while (i < len(y1)-2):
    if (y1[i] == 0):
        k += 1
    i += 1
print(k)
# Построим графики
plt.plot(x, y1, 'b',linewidth = 2, label='Пульс - 100 [уд/мин]')
# Подпишем оси
plt.xlabel('Время, c')
plt.ylabel('Изменение давления в артерии, мм рт. ст.')
# И график целиком
plt.title("Пульс после физической нагрузки")
plt.minorticks_on()
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.xlim([10,20])
plt.ylim([-1,1])
plt.legend()
plt.show()