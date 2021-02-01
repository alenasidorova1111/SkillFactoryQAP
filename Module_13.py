amount = int(input('Please enter amount of tickets:\n'))
money = 0

for elem in range(amount):
    age = int(input("Please enter ticket owner's age:\n"))
    if 18 <= age < 25:
        money += 990
    elif age >= 25:
        money += 1390

if amount > 3:
    print(f'Total price of tickets: {money * 0.9} rubles')
else:
    print(f'Total price of tickets: {money} rubles')
