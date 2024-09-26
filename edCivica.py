import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import csv

mesi = []
temp = []
scuola = []
giacca = []
gioco = []

data_file = open("./datiXgrafico.csv")
data_reader = csv.reader(data_file, delimiter=",")

for row in data_reader:
    #mesi.append(float(row[0])) scrive 
    mesi.append(float(row[1]))
    temp.append(float(row[2]))
    giacca.append(float(row[3]))
    scuola.append(float(row[4]))
    gioco.append(float(row[5]))

data_file.close()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Correlazione e causualità')

ax1.plot(mesi, temp, 'red', linewidth = 3)
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura media °C')
ax1.grid()

ax2.plot(mesi, giacca, 'green', linewidth = 3)
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con la giacca')
ax2.grid()

ax3.plot(mesi, scuola, 'blue', linewidth = 3)
ax3.set_xlabel('Mese')
ax3.set_ylabel('giorni di scuola')
ax3.grid()

ax4.plot(mesi, gioco, 'yellow', linewidth = 3)
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di gioco')
ax4.grid()
ax4.set_ylim([0, 40])
plt.show()