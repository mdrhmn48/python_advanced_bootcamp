
from calendar import*
year = int(input("enter Year: "))
print(calendar(year, 2,1,8,4))


my_text = "This text is a test"
result = my_text[-3]
print(result)

my_text = "In theory, theory and practice are the same. In practice, and they are not."
result = my_text.rindex("and")
print(result)

text = "ABCDEFGHIJKLM"
fragment = text[::-1]
print(fragment)

text = "We are going to learn six method today"
result = text.replace("e", "xxx")
print(result)

a = "learning"
b = "python"
c = "is"
d = "amazing"
e = " ".join([a, b, c, d])
print(e)

word = "If the implementation is hard to explain, it might be a bad idea."
word = word.replace("bad", "good")
word = word.replace("bad", "good")
print(word)


poem = """Thousand little white fish 
as if boiled 
    the color of the water"""
print("sun" not in poem)

###list####
#ordered indexed mutable allows duplicates []

example = ["apple","mango", "banana","orange"]
print(len(example))

result = example.reverse()
print(result)
print(example)

####dictionary####
my_dictionary = {"first_name" : "Md",
                  "last name" : "Rahman",
                  "age" : 28}
result = my_dictionary["first_name"]
print(result)

dic = {1: 55,
       2:  [12,"e",4],
       3: {"s1" : 100, "s2": 200}}
print(dic[2][1].upper())


#####Tuple#####
my_tuple = (1,4.4, "gh" , 2,3,4)
print(my_tuple[::-1])



####SET#####
print("my set")
my_set = set((1,2,3,(1,2),4,5))
print(my_set)

other_ser = {1,3,4,5}
print(type(other_ser))

s1 = {1,2,3}
s2 = {4,5,6}

s3 = s1.pop()
print(s3)


#####boolean ####
var1 = True
var2 = False

print(type(var1))
print(var1)


number = 5> 2+4

print(type(number))
print(number)



















