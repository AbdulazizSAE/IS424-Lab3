numbers = []

for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

largest_number = numbers[0]

for num in numbers:
    if num > largest_number:
        largest_number = num

print("The largest number is:", largest_number)
