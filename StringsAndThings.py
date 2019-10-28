# strings
#anything that falls withing""

#concatenation
# put 2 or  more strings together

firstName= "Fred"
lastName="Flintstone"

print(firstName+ " "+ lastName)

fullName = firstName + " " +lastName

print(fullName)

# repititon
#repitition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

#Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

#Slicing and Dicing
#slicing operator:
#slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])

#searching inside of strings

print("biv" in name)
print("v" not in name)

if "y" in name:
    print("the letter y is in name")
else:
    print("the letter y is no9t in the name")

    #Strings methods to investigate:
    #method         use Example     explination
    #center         aStr.center(w)
    #ljust          aStr.ljust(w)
    #rjust          aStr.rjust(w)
    #upper          aStr.upper()
    #lower          aStr.index(item)
    #rindex         aStr.rindex(item)
    #find           aStr.find(item)
    #rfind          aStr.rfind(item)
    #replace        aStr.replace(old, new)

    #be sure to include multiple examples of all of them in use

    # Charecter functions

    print(ord('5'))

    print(chr(97+13))

    print(str(12548))