import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Load the data from the CSV file
file_path = 'SalaryPrediction.csv'
data = pd.read_csv(file_path)

# Converting the 'Wage' column to numeric data type
data['Wage'] = data['Wage'].replace('[\$,]', '', regex=True).astype(float)
data['Wage'] = data['Wage'] / 1e6

# # Histogram of wages in millions
# plt.figure(figsize=(10, 6))
# sns.histplot(data['Wage'], bins=30, kde=True)
# plt.title('Distribution of Wages in Millions')
# plt.xlabel('Wage (in millions)')
# plt.ylabel('Number of People')
# plt.show()

# # Bar chart of average wage per league
# average_wage_per_league = data.groupby('League')['Wage'].mean().sort_values(ascending=False)
# plt.figure(figsize=(10, 6))
# sns.barplot(x=average_wage_per_league.values, y=average_wage_per_league.index)
# plt.title('Average Wage per League')
# plt.xlabel('Average Wage (in millions)')
# plt.ylabel('League')
# plt.show()

# # Scatter plot of age vs wage
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=data['Age'], y=data['Wage'])
# plt.title('Relationship between Age and Wage')
# plt.xlabel('Age')
# plt.ylabel('Wage (in millions)')
# plt.show()

# # Scatter plot of Apps vs age
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=data['Age'], y=data['Apps'])
# plt.title('Relationship between Age and Number of Appearances (Apps)')
# plt.xlabel('Age')
# plt.ylabel('Number of Appearances (Apps)')
# plt.show()

# # Box plot of age distribution across different positions
# plt.figure(figsize=(10, 6))
# sns.boxplot(x=data['Position'], y=data['Age'])
# plt.title('Age Distribution across Different Positions')
# plt.xlabel('Position')
# plt.ylabel('Age')
# plt.show()

# Descriptive statistics of data
wage_descriptive = data['Wage'].describe()
print(f"{wage_descriptive}\n")
age_descriptive = data['Age'].describe()
print(f"{age_descriptive}\n")
apps_descriptive = data['Apps'].describe()
print(f"{apps_descriptive}\n")
caps_descriptive = data['Caps'].describe()
print(f"{caps_descriptive}\n")

# Hypothesis testing for average wage
avg_wage = 1.500
mean = wage_descriptive['mean']
z_score = (avg_wage - mean) / wage_descriptive['std']
p_value = stats.norm.sf(abs(z_score))

print(f"p_val = {p_value} > 0.05, therefore we fail to reject the null hypothesis.\n")

# Correlation Analysis between Age and Wage whether they are correlated
r = stats.pearsonr(data['Age'], data['Wage'])
print(f"r = {r[0]} \np_val = {r[1]} < 0.05, therefore we reject the null hypothesis.")


