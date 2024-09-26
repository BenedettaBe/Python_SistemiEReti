import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import csv

anno = []
temp = []
annoMassa = []
massa = []

data_file = open("./GlobalAnomaly.csv")
data_reader = csv.reader(data_file, delimiter=",")

for row in data_reader:
    anno.append(int(row[0]))
    temp.append(float(row[1]))

data_file.close()

data_file = open("./MassaAntartide.csv")
data_reader = csv.reader(data_file, delimiter=",")

for row in data_reader:
    annoMassa.append(int(row[0]))
    massa.append(float(row[1]))

data_file.close()

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Correlazione e causalità del global warming')

ax1.plot(anno, temp, 'red', linewidth = 3)
ax1.set_xlabel('Anno')
ax1.set_ylabel('Temperatura terra-oceano (°C)')
ax1.grid()

ax2.plot(annoMassa, massa, 'red', linewidth = 3)
ax2.set_xlabel('Anno')
ax2.set_ylabel("Massa dell'Antartide (Gt)")
ax2.grid()
plt.show()