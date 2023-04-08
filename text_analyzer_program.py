text = input("Enter your text: ").lower()
letters = input("Enter your three letter: ").lower().split(" ")

print(text)
print(letters)

for letter in letters:
    letter_repetition = text.count(letter)
    print(f"{letter} appeared {letter_repetition} times in '{text}'")

#1
letter = list(letters)
print(letter)




#2
text = list(text)
print(len(text))

#3
print(text[0])
print(text[-1])

#4
text = "".join(text)
print(text)
# print(text.reverse())

#5
result = "python" in text
print(result)
my_dict = {
    True: "was",
    False: "was not"
}
print(f"The word 'python' {my_dict[result]} in text")

# print(result)
