numbers = [5, 20, 30, 30, 50]
inputNumber = int(input("Enter a number to remove"))
try:
    numbers.remove(inputNumber)
except:
    numbers.clear()
print(numbers)
