import pandas as pd
import matplotlib.pyplot as plt
c = lambda f: 5/9 * (f - 32)
temps = [(f, c(f)) for f in range(0, 100, 10)]
temps_df = pd. DataFrame(temps, columns=[ 'Fahrenheit', 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_label = axes.set_ylabel( 'Celsius' )
plt.show()