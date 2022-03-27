
# Distance Converter

def MilestoKilometers():
    Miles = float(input("How many miles would you like converted? "))

    Kilometers = float(Miles * 1.609)

    print("The distance is " + str(round(Kilometers, 2)) + " km")

    return

def KilometerstoMiles():
    KG = float(input("How many kilometers would you like converted? " ))

    mi = float(KG / 1.609)

    print("The distance is " + str(round(mi, 2)) + " mi")

    return

def chooser():
    tempvariable = str(input("What unit of measure will you use to calculate distance? Miles or kilometers? "))
    if tempvariable.lower() == "miles":
        KilometerstoMiles()
    elif tempvariable.lower() == "kilometers":
        MilestoKilometers()
    else:
        print("Error: Expecting 'miles' or 'kilometers'")

if __name__ == '__main__':
    chooser()