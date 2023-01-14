# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter month: ")
Autumn = ["September","October","November"]
Winter = ["December","January","February"]
Spring = ["March","April","May"]
Summer = ["June","July","August"]
if month in Autumn:
    print("Autumn")
elif month in Winter:
    print("Winter")
elif month in Spring:
    print("Spring")
elif month in Summer:
    print("Summer")
else:
    print("invalid")