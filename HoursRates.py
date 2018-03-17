# Inputs
hri = input('Enter Hours: ')
rai = input('Enter Rate: ')
try:
    hours = float(hri)
    rate = float(rai)
except:
    print("Error, please enter numeric input")
    quit()
# print(hours, rate)
if hours > 40:
    # print("Overtime")
    regular = rate * hours
    overtime = (hours - 40.0) * (rate * 0.5)
    # print(regular, overtime)
    pay = regular + overtime
else:
    # print("regular")
    pay = hours * Rate

print("Pay:",pay)
