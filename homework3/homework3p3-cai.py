import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
print("The data looks like", data)
# 1. What are the columns in our dataset?
print(data[0].keys())

# 2. How many countries do we have in our dataset?
print("There are",len(data),"countries in our dataset.")

# 3. How many countries in Asia? How about North America?
asiacount=0
for country in data:
    if country['Continent']=='Asia':
        asiacount=asiacount+1
print('There are',asiacount,'countries in asia.')
nacount=0
for country in data:
    if country['Continent']=='N. America':
        nacount=nacount+1
print('There are',nacount,'countries in North America.')

# 4. What is the total population of the world?
pop=0
for country in data:
    pop=pop+int(country['Population'])
print(pop,"is the total population of the world.")

# 5. Which has a larger population, Africa or South America?
popafrica=0
for country in data:
    if country['Continent']=='Africa':
        popafrica=popafrica+int(country['Population'])
popsa=0
for country in data:
    if country['Continent']=='S. America':
        popsa=popsa+int(country['Population'])
if popafrica>popsa:
    print('Africa has more population than South America.')
if popafrica<popsa:
    print("South America has more population than Africa.")

# 6. Calculate the total GDP of each country and print it out (right now it's per capita).
for country in data:
    gdp=int(country['GDP_per_capita'])*int(country['Population'])
    print(gdp)

# 7. What is the median life expectancy of the world?
import statistics
life=[float(country['life_expectancy'])for country in data]
print(statistics.median(life),"is the median life expectancy.")

# 8. What is the median life expectancy of Europe?
lifeE=[float(country['life_expectancy'])for country in data if country['Continent']=='Europe']
print(statistics.median(lifeE),"is the median life expectancy of Europe.")

# 9. Print out each country that has a below-average life expectancy.
meanlife=statistics.mean(life)
for country in data:
    if float(country['life_expectancy'])< meanlife:
        print(country['Country'])

# 10. Print out each country that has a below-average GDP but an above-average life expectancy.

# 11. Calculate the 75th percentile of GDP.

# 12. What percent of the world population has a life expectancy of below 50 years? Above 80 years?