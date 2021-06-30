import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world-happiness-report.csv')

# print the info of csv file
print(df.info())

# print 1st 10 rows
print(df.head(10))


# extract all countries in data set
unique_country_names = df['Country name'].unique()
# print(unique_country_names)

# choose some countries to make reports
desired_countries = ['Afghanistan', 'Bahrain', 'Egypt', 'Iran', 'Iraq', 'Kuwait', 'Lebanon', 'Oman',
                     'Palestinian Territories', 'Saudi Arabia']

# desired_countries_data: dcd
dcd = df.loc[df['Country name'].isin(desired_countries)]

# detect the number of data for each country
dcd_group = dcd.groupby(['Country name']).size()

# remove 'Oman' due to lacking of data
dcd = dcd[dcd['Country name'] != 'Oman']

# detect the years that have complete data
dcd_group_year = dcd.groupby(['year']).size()

# region step 5
# # for each year compute the mean and max of Life Ladder values
# years = []
# means = []
# max_country = []
# max_array = []
# for x in range(2011, 2018):
#     years.append(x)
#     mean = dcd[dcd['year'] == x]['Life Ladder'].mean()
#     means.append(mean)
#     max_value = dcd[dcd['year'] == x]['Life Ladder'].max()
#     max_country_year = dcd[dcd['Life Ladder'] == max_value]['Country name'].values[0]
#     max_array.append(max_value)
#     max_country.append(max_country_year)
#
# # 5.1
# ser = pd.Series(means, index=years)
# ser.plot()
# plt.xlabel('Year')
# plt.ylabel('Life Ladder')
# plt.title('Mean Happiness Value')
# plt.ylim(4, 6)
# # plt.show()
# plt.savefig('Mean Happiness Value.png')
#
# # 5.2
# maxSeries = pd.Series(max_array, index=years)
# plt.cla()
# plt.scatter(x=years, y=max_array)
# counter = 0
# for x, y in zip(years, max_array):
#     plt.annotate(max_country[counter], (x, y), textcoords="offset points", xytext=(0, 10), ha='center')
#     counter += 1
# plt.xlabel('Year')
# plt.ylabel('Life Ladder')
# plt.title('Most Happiest Country')
# plt.ylim(6,7)
# # plt.show()
# plt.savefig('Most Happiest.png')
# endregion

# 6: Fill empty cells by mean value
mean_GDP = dcd['Log GDP per capita'].mean()
dcd['Log GDP per capita'].fillna(mean_GDP, inplace=True)

# correlation check
correlation = dcd.corr(method ='pearson')['Life Ladder']
