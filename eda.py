import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# First load the dataset.
df=pd.read_csv('migration_nz.csv')
df.info()
print(df)
# We will check for duplicate rows.
print(df[df.duplicated(keep=False)])
# No duplicate rows.

# Let us see what kind of elements are in each qualitative column.
print(df['Measure'].unique())
print(df['Citizenship'].unique())
print(df['Country'].unique())

# Let us examine only the total arrivals and departures from all countries and all citizenships.
df=df[(df['Citizenship']=='Total All Citizenships') &(df['Country']=='All countries')]
df=df[df['Measure']!='Net']
df.drop(columns=['Citizenship','Country'],inplace=True)
df.reset_index(drop=True, inplace=True)
df.info()
print(df)

plt.figure(figsize=(8,4))
sns.lineplot(df,x='Year',y='Value',hue='Measure')
plt.show()

# Let us examine the year to year increase or decrease in arrivals.
print(df['Year'].unique())

years=[i for i in range(1980,2017)]
print(years)
arrivals=df[df['Measure']=='Arrivals']
print(arrivals)
print("What do I get?")
print(100*(arrivals[arrivals['Year']==1980]['Value'].values[0]
                     -arrivals[arrivals['Year']==(1979)]['Value'].values[0])
                     /arrivals[arrivals['Year']==(1979)]['Value'].values[0])

arrival_change=[100*(arrivals[arrivals['Year']==i]['Value'].values[0]
                     -arrivals[arrivals['Year']==(i-1)]['Value'].values[0])
                     /arrivals[arrivals['Year']==(i-1)]['Value'].values[0]
                     for i in range(1980,2017)]
print(arrival_change)
changes_df=pd.DataFrame({'Year':years,'Arrivals pct change from previous year':arrival_change})
print(changes_df)
# Now we do the same for departures.
departures=df[df['Measure']=='Departures']
changes_df['Departures pct change from previous year']=[100*(departures[departures['Year']==i]['Value'].values[0]
                                                             -departures[departures['Year']==(i-1)]['Value'].values[0])
                                                             /departures[departures['Year']==(i-1)]['Value'].values[0]
                                                             for i in range(1980,2017)]

print(changes_df)