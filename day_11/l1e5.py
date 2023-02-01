# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(m):
    m=int((m%12)/3)
    print(m)
    if m == 0:
        return "Winter"
    elif m == 1:
        return "Spring"
    elif m == 2:
        return "Summer"
    else:
        return "Autumn"
    
print(check_season(12))
        