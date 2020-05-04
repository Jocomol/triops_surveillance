#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import sqlite3


#Get the data from the database
conn = sqlite3.connect('triops.db')
c = conn.cursor()
c.execute('''SELECT temperature_C from measurement;''')

y = c.fetchall()
print(y)
x = range(len(y))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.minorticks_on()

# Zeichnen
plt.plot(x, y, label='Aufgabe A')

# Styling
plt.title('Triops Temperatur')
plt.grid(alpha=.7, linestyle='--',which="both")
plt.legend()



# Anzeigen
plt.show()
