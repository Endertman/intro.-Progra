import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/josel/OneDrive/Documentos/intro. Progra/matplotlib/1.csv', sep= ',')

df['edad'].plot(kind='bar', color = 'red', marker  = 'o')
plt.title('Edades')
plt.xlabel('Personas')
plt.ylabel('Edad')

plt.show()