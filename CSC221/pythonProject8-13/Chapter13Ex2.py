
# https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nyc = pd.read_csv('data4.csv')
nyc. columns = ['Date', 'Temperature', 'Anomaly']
nyc. Date = nyc.Date.floordiv(100)

from scipy import stats

linear_regression = stats. linregress(x=nyc.Date, y=nyc. Temperature)
# x = year, y = temp
# y = mx +b
print(linear_regression.slope)
print(linear_regression.intercept)
# Temperature for future based on slope
print(linear_regression.slope * 2023 + linear_regression.intercept)
# Temperature for past based on slope
print(linear_regression.slope * 1890 + linear_regression.intercept)
print(linear_regression.slope * 2025 + linear_regression.intercept)

sns.set_style('whitegrid')
# Without regression
sns.relplot(x=nyc.Date, y=nyc. Temperature)
# With regression
axes = sns.regplot(x=nyc.Date, y=nyc. Temperature)
#axes. set Vim (10, 70)
plt.show()