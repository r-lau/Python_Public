
# Weight Converter from Imperial to Metric

def PoundsToKilograms():
    Pound = float(input("How much does your item weigh in pounds? "))

    Kilograms = float(Pound / 2.205)

    print("The item weighs " + str(round(Kilograms, 2)) + " kg")

    return

def KilogramsToPounds():
    KG = float(input("How much does your item weigh in kilograms? "))

    LBs = float(KG * 2.205)

    print("The item weighs " + str(round(LBs, 2)) + " lbs")

    return

def OuncetoGrams():
    Ounce = float(input("How much does your item weigh in ounce? "))

    G = float( Ounce * 28.35)
    
    print("The item weighs " + str(round(G, 2) + " g"))

    return

def GramstoOunce():
    Grams = float(input("How much does your item weigh in grams? "))

    Ounce = float( Grams / 28.35)

    print("The item weights " + str(round(Ounce,2)) + " oz")

    return

def chooser():
    tempvariable = str(input("What unit of measure will you use to weigh items? Imperial or metric? "))
    if tempvariable.lower() == "imperial":
        tempvariable2 = str(input("Do you want to convert from ounces or pounds? "))
        if tempvariable2.lower() == "pounds":
            PoundsToKilograms()
        elif tempvariable2.lower() == "ounces":
            OuncetoGrams()
        else:
            print("Error: Expecting 'ounces' or 'pounds'")
    elif tempvariable.lower() == "metric":
        tempvariable3 = str(input("Do you want to convert from grams or kilograms? "))
        if tempvariable3.lower() == "grams":
            GramstoOunce()
        elif tempvariable3.lower() == "kilograms":
            KilogramsToPounds()
        else:
            print("Error: Expecting 'grams' or 'kilograms'")
    else:
        print("Error: Expecting 'imperial' or 'metric'")

if __name__ == '__main__':
    chooser()
