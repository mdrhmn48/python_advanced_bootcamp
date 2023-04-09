text = "the sentence is short"
my_bool = not "a" == "b"
print(my_bool)

text = "When something is important enough, you do it even if the odds are against you"

word1 = "success"
word2 = "technology"

my_bool = not((word1 in text) and (word2 in text))
print(my_bool)

#Control Flow####

age = 20
has_license = False

if age<18:
    print("You can't drive yet. You must be 18 years old and have a license")
elif (age >= 18) and has_license:
    print("You can drive. You have a license")
elif (age >= 18) or has_license:
    print("You can't drive. You need to have a license")
else:
    print("----")


speak_french = False
knows_python = False

if (speak_french == True) and (knows_python == True):
    print("You meet the requirements to apply")
elif (speak_french == False) and (knows_python == False):
    print("To apply, you need to know how to program in Python and speak French")
elif (speak_french == False) or (knows_python == True):
    print("To apply, you need to speak French")
elif (speak_french == True) or (knows_python == False):
    print("To apply, you need to know how to program in Python")

################LOOOOOOOOOOPSS################
#for loops
names = ["Md", "Rahim", "Amir", "Tawsif"]

for number, name in enumerate(names):
    name_number = names.index(name) + 1
    print(f"Hello {name, number} index: {name_number}")

for name in names:
    if name.startswith("R"):
        print(name)
    else:
        print(name)

numbers = [1,3,4,5,6]
my_value = 0

for number in numbers:
    print(f"my value: {my_value}")
    my_value = my_value + number
    print(f"after addition: {my_value}")

print(my_value)


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_numbers = 0
for number in list_numbers:
    sum_numbers += number
    print(sum_numbers)


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0
for num in list_numbers:
    if (num % 2 == 0):
        sum_even += num

    elif (num % 2 == 1):
        sum_odd += num

    print(sum_odd)

#######################                            WHILE LOOPS ###################################

coins = 5
while coins >0:
    print(f"I have {coins} coins")
    coins -=1
else:
    print("No Money")

answer = "y"
while answer == "y":
    answer = input(">")
else:
    print("Thank you")

number = 10
while number > -1:
    print(number)
    number -= 1

number = 33
while number >-1:
    print(f"this is  5: {number}")
    number -= 1
    if number % 5 == 0:
        print(f"this is divided by 5: {number}")
    elif number % 5 != 0:
        print(f"this is not divided by 5: {number}")
        continue

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
    if number > 0:
        pass
        print(number)
    else:
        print(number)
        break

my_list = list(range(1, 101))
print(my_list)
for number in range(1, 21, 5):
    print(number)



sum_squares = 0
for number in range(1,16):
    print(f"number: {number}")
    sum_squares += number ** 2



list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')





indices_list = "Python"

for index, names in enumerate(indices_list):
    print(index, names)
string = "Python"
indices_list = list(enumerate(string))
print(indices_list)




list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, names in enumerate(list_names):
        if names[0] == "M":
            print(index)






name = ["Adibah", "Ayub", "MD", "Rahman"]
age = [21,21,22,28, 55]
cities = ["new york", "Dhaka"]

combo = list(zip(name, age, cities))
print(combo)
brands =["my lingerie", "booty", "shorts"]
products = ["zara", "H&M", "Forever21"]

my_zip = zip(products,brands)

print(my_zip)

my_list = [45, 54, 55, 24]

print(f"min number: {max(my_list)}")

dic = {"key" : 5,
       "key1": 3}
print(min(dic.values()))

dictionary_ages = {"Tony":55, "Paulie":42, "Meadow":78, "Vito":44, "Ralph":24, "Sarah":35, "Evan":19, "Jean":2 ,"Ned":49}


minimum_age = min(dictionary_ages.values())

last_name = max(dictionary_ages.keys())

print(last_name)


from random import *


color = ["blue", "green", "yellow", "black"]
my_random = choice(color)
print(my_random)


numbers = list(range(5, 50,5))
shuffle(numbers)
print(numbers)
random_number = random(0,1)

print(random_number)


####   list comprehension ####

word = "python"
my_list = [md if md *2>10 else "heloo" for md in range(0,21,2) ]

print(my_list)

feet  = [10,20,30,40,50]
meters = [f*0.3048 for f in feet]
print(meters)

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [ (temp-32)*(5/9) for temp in temperature_fahrenheit]

print(degrees_celsius)


#####Match

series = "Nf-02"

match series:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Apple")
    case "N-04":
        print("Motorola")
    case _:
        print("No Match")


client = {
    "name" : "Md",
    "age" : 28,
    "occupation": "Data Science Engineer"
}

job = {
    "title" : "Data Science Engineer",
    "location" : { "city": "Richmond",
                   "state" : "Virginia"
                   }}
items = [client, job, "looking"]

for i in items:
    match i:
        case {
            "name": name,
            "age": age,
            "occupation" : occupation
        }:
            print("clinet is found")
            print(name, age, occupation)
        case {
            "title": title,
            "location": {
                "city": city,
                "state": state
            }
        }:
            print("Job is found")
        case _:
            print("Still searching")



















































