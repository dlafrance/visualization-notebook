import os
import matplotlib.pyplot as plt
import pandas as pd

# Loading file
df = pd.read_csv('insurance.csv', header=0)
print(df.head())

# Create plot directory
os.makedirs('plots', exist_ok=True)

# Plotting line chart for Charges
plt.plot(df['charges'])
plt.title('Charges by individual')
plt.xlabel('Individual')
plt.ylabel('Charges')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.clf()

# Plotting histogram for BMI
plt.hist(df['bmi'])
plt.title('Histogram of BMI')
plt.xlabel('Bins')
plt.ylabel('BMI')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(df['age'], df['charges'])
plt.title('Age to Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_charges_scatter.png', format='png')

plt.close()