
# Liquid Converter

def MillilitertoCups():
    Milliliter = float(input("How many milliters are needed to be converted? "))

    Cups = float(Milliliter / 237)

    print("The conversion from milliliter to cups is " + str(round(Cups,2)))

    return

def CupsToMilliters():
    Cups = float(input("How many cups are needed to be converted? "))

    Millliters = float(Cups * 237)

    print("The conversion from cups to milliliters is " + str(round(Millliters,2)))

    return

def chooser():
    tempvariable = str(input("What unit of measure do you want to convert from? Imperial or metric?"))
    if tempvariable.lower() == "imperial":
        CupsToMilliters()
    elif tempvariable.lower() == "metric":
            MillilitertoCups()
    else:
        print("Error: Expecting 'imperial' or 'metric'")


if __name__ == '__main__':
    chooser()