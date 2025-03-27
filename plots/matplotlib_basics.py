import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.DataFrame({
    'year': [2012, 2013, 2014, 2015, 2016],
    'population': [100, 101, 103, 104, 101],
    'gdp': [81, 82, 87, 89, 88]
})

# make a 2x2 chart window
fig, ax = plt.subplots(nrows=2, ncols=2)

# make a lineplot in the top-left
ax[0, 0].plot(df['year'], df['population'])
ax[0, 0].plot(df['year'], df['gdp'], color='green', marker='o')
ax[0, 0].set_title('population and GDP by year')
ax[0, 0].legend(['pop.', 'gdp'])
ax[0, 0].set_xticks(df['year']) # force xticks to appear at whole years

# change the last tick on the lineplot to say "2016 ytd"
tick_labels = ax[0, 0].get_xticklabels()
tick_labels[-1] = '2016 ytd'
ax[0, 0].set_xticklabels(tick_labels)

# bar plot in the top-right
ax[0, 1].bar(df['year'], df['gdp'])
ax[0, 1].set_title('GDP by year')

# scatter plot in the bottom-left
ax[1, 0].scatter(df['population'], df['gdp'])
ax[1, 0].set_title('GDP vs Population')
ax[1, 0].set_xlabel('population')
ax[1, 0].set_ylabel('GDP')

# histogram in the bottom-right
random_data = np.random.normal(0, 1, 1000)
# add an outlier
random_data[-20:] = 99
# cap outliers to fit in some overflow bin
random_data[random_data > 3] = 3

bin_edges = np.linspace(-3, 3, 8)
bin_centers = bin_edges
ax[1, 1].hist(random_data, bins=bin_edges)
ax[1, 1].set_title('histogram of some random data')
# manipulate tick labels to show there's an overflow bin
ax[1, 1].set_xticks(bin_edges)
tick_labels = ax[1, 1].get_xticklabels()
tick_labels[-1] = '3 or more'
ax[1, 1].set_xticklabels(tick_labels)


plt.tight_layout() # reposition to avoid overlapping charts
plt.show()