#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.

count = 0
total = 0
avg = 0
largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    try:
        num = float(num)
        count+= 1
        total+= num
        avg = total / count
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
    except:
        if num == 'Done' or num == 'done':
            break
        else:
            print('Invalid Input.')
            continue

print('Count:', count, 'Largest:', largest, 'Smallest:', smallest)
