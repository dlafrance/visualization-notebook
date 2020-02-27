import os
import matplotlib.pyplot as plt
import pandas as pd

# Loading file
df = pd.read_csv('game_teams_stats.csv', header=0)
print(df.head())
print(df.columns)
print(df.shape)


# Plotting line chart for shots
plt.plot(df['shots'])
plt.title('Shots by game and team')
plt.xlabel('Game and team')
plt.ylabel('Shots')
plt.savefig(f'plots/shots_plot.png', format='png')
plt.clf()

# Plotting histogram for hits
plt.hist(df['hits'])
plt.title('Histogram of hits')
plt.xlabel('Bins')
plt.ylabel('Hits')
plt.savefig(f'plots/hits_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(df['shots'], df['hits'])
plt.title('Shots to hits')
plt.xlabel('Shots')
plt.ylabel('Hits')
plt.savefig(f'plots/shots_to_hits_scatter.png', format='png')

plt.close()