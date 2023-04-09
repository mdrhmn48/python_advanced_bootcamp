name = input("what is your name? ")
sales = float(input("What is your sales for this month: "))

# first_name, last_name = name.split(" ")
commission = round(sales*13/100, 2)
print(f"Your name is {name}, amount of commission: {commission}")