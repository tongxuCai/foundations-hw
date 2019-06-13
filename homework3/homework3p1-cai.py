#PART 1 LISTS
# numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]
# 1. Count how many numbers are in the list. 
count=0 
for number in numbers:
    count=count+1
print('There are ',count,'numbers in the list.')

# 2. Use a Python method to add a new number to the list. 
new=3
numbers.insert(1,new)
print(numbers)

# 3. Count how many even numbers are in the list. Use a for loop.
evencount=0
for number in numbers:
    if number%2==0:
        evencount=evencount+1
print('There are',evencount,'even numbers in the list.')

# 4. Count how many values are above the mean and how many are below the mean. 
import statistics 
mean=statistics.mean(numbers)
abovemean=0
for number in numbers:
    if number>mean:
        abovemean=abovemean+1
print('There are',abovemean,'values that are above the mean.')
belowmean=0
for number in numbers:
    if number<mean:
        belowmean=belowmean+1
print('There are',belowmean,'values that are below the mean.')

# 5. Total up the numbers. Use a for loop, do NOT use sum().
total=0
for number in numbers:
    total=total+number
print('The sum is',total)

# 6. Total up the numbers that are above the mean, and total up the numbers below the mean. 
totalabovemean=0
for number in numbers:
    if number>mean:
        totalabovemean=totalabovemean+number
print('The sum of numbers above the mean is',totalabovemean)

totalbelowmean=0
for number in numbers:
    if number < mean:
        totalbelowmean=totalbelowmean+number
print('The sum of numbers below the mean is',totalbelowmean)

# 7. Find the largest number. Use a for loop.
largest=numbers[0]
for number in numbers:
    if number > largest:
        largest=number
print('The largest number is',largest)

# 8. You have a list of dogs, add Maxwell. 
dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
newdog='Maxwell'
dogs.insert(1,newdog)
print(dogs)

# 9. Make a list of all dogs that have names of 5 characters or less. 
for dog in dogs:
    if len(dog)<5:
        print(dog,"has a name of 5 characters or less.")

# 10. I'm on a web page with some links about Zurich, and the URL looks like this:
#  http://important-swiss-things.ch/docs/download/ZH . 
# Bern is another canton - its abbreviation is BE, so its URL is 
# http://important-swiss-things.ch/docs/download/BE. I want to get this link for 
# every single canton in Switzerland, not just Zurich and Bern, 
# BUT I don't want to type each URL manually. 
# If I give you this list of the canton abbreviations, 
# can you print out all of the URLs?
cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", 
"BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", 
"JU"]
url="http://important-swiss-things.ch/docs/download/"
for canton in cantons:
    print(url+canton)

# 11. I'm trying to get some top-secret documents from top-secret-secrets.com
# Each secret document has a document ID and is made up of 12 pages, 
# pages "001.pdf" through "012.pdf". Each page is available at a different URL. 
# For example, for the document ID of QQ7LTHM, the pages are available at

# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf
# ...
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf
# I have the following document IDs: qq7lthm, jemsqhg, O6itcke, cp4Iua0, bkijcmo, 
# ctoyjrm,z8wc6xy, zk4Bmm0
# Can you print out all of the URLs? capitalize IDs in the URL
firsturl="www.top-secret-pdfs.com/content/secrets/"
IDs=['qq7lthm', 'jemsqhg', 'O6itcke', 'cp4Iua0', 'bkijcmo', 'ctoyjrm','z8wc6xy', 'zk4Bmm0']

newIDs=[]
for ID in IDs:
    newIDs.append(ID.upper())
secondurl='/page/'
pdfs=['001.pdf','002.pdf','003.pdf','004.pdf','005.pdf','006.pdf','007.pdf','008.pdf','009.pdf','010.pdf','011.pdf','012.pdf']
for pdf in pdfs:
    for newID in newIDs:
       print(firsturl+newID+pdf)


