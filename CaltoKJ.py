while True:
    #Input Calories
    cal = input('Input amount of Calories:')
    try:
        cal = int(cal)
    except:
        print("Error, please enter whole number.")
        quit()

    #calculation
    kj = cal * 4.186
    print(kj, "Kilojoules")
