
# Temperature calculator

def celicustempcalc():
    try:
        Current_F = float(input("What is the current temp in farenheit? "))

        Current_C = 5.0 * (float(Current_F) - 32.0) / 9.0

        print("The current temperature in celcius is: " + str(Current_C))
    except Exception as e:
        print("Error: " + e)
    return

def farenheittempcalc(): 
    try:
        Current_C_Temp = float(input("What is the current temp in celcius? "))

        Current_F_Temp = (float(Current_C_Temp) * 9.0/5.0) + 32

        print("The current temperature in farenheit is: " + str(Current_F_Temp))
    except Exception as e2:
        print("Error: " + e2)
    return   

def chooser():
    tempvariable = str(input("What tempature do you need converted from? Farenheit or celcius? "))
    if tempvariable.lower() == "farenheit":
        farenheittempcalc()
    elif tempvariable.lower() == "celcius":
        celicustempcalc()
    else:
        print("Error: Expecting 'farenheit' or 'celcius'")
        
if __name__ == '__main__':
    chooser()