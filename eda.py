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




# We will zoom in on arrivals.
# First we create a figure and save the axis.
plt.figure(figsize=(10,6))
ax=plt.gca()
# Now we create the line plot (with markers, this time)
sns.lineplot(df[df['Measure']=='Arrivals'],x='Year',y='Value',marker='o')
ax.set_ylim(bottom=0)
# For each film in the Lord of the Rings series we will create a vertical line denoting its release.  
# We would like the lines to run from the base of the plot to the line defined above. We want each line to be striped, and
# not the same color as the linegraph.

# We set where (which x values) the three lines should be.  We label the entire collection.  We set the line style to dashed.
# We set the color to the second in the current palette. We set the ymin (the coordinate the lines start at) to 0.
# Finally, we set a different ymax for each line. We use .valuesto return numbers not a smaller dataframe.
plt.vlines(x=[2001,2002,2003],label="The Lord of the Rings", ls='--',color='C1',
           ymin=0,
           ymax=[df[(df['Measure']=='Arrivals') & (df['Year']==year)]['Value'].values for year in [2001,2002,2003]])

# We will annotate each of these lines with the title of the corresponding film.  
ax.text(2000.5, .05, 'The Fellowship of the Ring', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])
ax.text(2001.5, .05, 'The Two Towers', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])
ax.text(2002.5, .05, 'The Return of the King', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])

# We repeat for the films in The Hobbit trilogy (in a different color).
plt.vlines(x=[2012,2013,2014],label="The Hobbit", ls='--',color='C2',
           ymin=0,
           ymax=[df[(df['Measure']=='Arrivals') & (df['Year']==year)]['Value'].values for year in [2012,2013,2014]])


ax.text(2011.5, .05, 'An Unexpected Journey', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])
ax.text(2012.5, .05, 'The Desolation of Smaug', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])
ax.text(2013.5, .05, 'The Battle of the Five Armies', rotation=90, fontsize='small', transform=ax.get_xaxis_text1_transform(0)[0])
plt.legend()
plt.show()