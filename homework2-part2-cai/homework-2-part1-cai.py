# Tongxu Cai 
# May 30 2019
# Homework 2, Part 1

numbers=[22, 90, 0, -10, 3, 22, 48]
print(numbers)
print("There are", len(numbers), "numbers in the list")
print("The fourth element is", numbers[3])
print("the sum of the 2nd and 4th element is", numbers[1]+numbers[3])
numberss=[22, 90, 0, -10, 3, 22, 48]
# Sorting list of Integers in ascending 
numberss.sort() 
print(numberss)
print("the 2nd-largest value is", numberss[-2])
print("the last element of the original unsorted list is", numbers[-1])
print("the sum divided by two is", sum(numbers)/2)
import statistics 
print("The list's mean", statistics.mean(numbers),"is higher than its median", statistics.median(numbers))

#movie
movie={
    'title':'HarryPotter',
    'year':'2001',
    'director':'Chris Columbus'
    'budget':1000,
    'revenue':2000
}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
print("The difference between its budget and reveneu is", movie['revenue'] - movie['budget'])

if movie['revenue'] - movie['budget'] < 0:
    print("That was a bad investment.")
elif movie['revenue'] - 5*movie['budget'] >0:
    print("That was a great investment.")
else: print ("Okay investment.")

#population
pop={
    'Manhattan':1.6,
    'Brooklyn':2.6,
    'Queens':2.3,
    'Staten Island':0.47,
    'Bronx':1.4
}
print("The population of Brookyln is", pop['Brooklyn'],"million.")
print("The combined population of all five boroughs is", pop['Brooklyn'] + pop['Staten Island'] + pop['Manhattan'] + pop['Queens'] + pop['Bronx'],"millions.")
print(round(100*pop['Manhattan']/sum(pop.values()),2), "percentage of NYC's population lives in Manhattan.")
