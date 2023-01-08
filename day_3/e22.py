# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = float(input("Enter number of years you have lived: "))
remYears = 100 - years
print(f"Yout have {remYears*365.25*24*60*60} seconds to live")