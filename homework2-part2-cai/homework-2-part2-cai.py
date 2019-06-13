# Tongxu Cai
# May 30 2019
# Homework 2, Part 2

# PART TWO: Lists
countries=["Brazil",'Peru','Italy','Morocco','Spain','Senegal','Thailand']
print(countries)
for country in countries:
    print(country)
countries.sort()
print('Sorted:',countries)
print(countries[0])
print(countries[-2])
countries.remove('Brazil')
print('Updated list:',countries)
for country in countries:
    print(country.upper())


# PART TWO: Dictionaries
tree={
    'name':'TreeofLife',
    'species':'Mesquite',
    'age':400,
    'location_name':'Bahrain',
    'latitude':25.994073,
    'longitude':50.583235
}
print(tree['name'], "is a ", tree['age'],"year old tree that is in", tree['location_name'])
if tree['latitude']<40.7128:
    print("The tree",tree['name'],"in",tree['location_name'],"is south of NYC.")
else: 
    print("The tree",tree['name'],"in",tree['location_name'],"is north of NYC.")
age=input("How old are you?")
variable=int(age)
print(age)

if variable > tree['age']:
    print("You are",(variable - tree['age']),"years older than", tree['name'])
else:
    print(tree['name'],"was",(tree['age']-variable),"years old when you were born.")


# PART TWO: Lists of dictionaries
cities =[{'name':'Moscow',
    'latitude': 55.7558},
    {'name':'Tehran',
    'latitude':35.6892},
    {'name':'FalklandIslands',
    'latitude':51.7963},
    {'name':'Seoul',
    'latitude':37.5665},
    {'name':'Santiago',
    'latitude':33.4489}]

for city in cities:
    if city['latitude']>0 :
        print(city['name'], "is above the equator.")
    elif city['latitude']<0:
        print(city['name'],"is below the equator.")
    else:
        print(city['name'],"is on the equator.")
    if city['latitude'] == 51.7963:
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

for city in cities:
    if city['latitude']>25.994073:
        print(city['name'],"is north of TreeOfLife.")
    else:
        print(city['name'],"is south of TreeOfLife.")

