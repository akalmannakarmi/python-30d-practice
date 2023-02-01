# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(list):
    result = 0
    for item in list:
        result+=item
    result/=len(list)
    return result
def calculate_median(list):
    n = len(list)
    if n%2 == 0:
        return (n+1)/2
    return (n/2)+(n/2+1)/2
def calculate_mode(list=[]):
    mode = list[0]
    for item in list:
        if list.count(mode) >list.count(item):
            mode = item
    return mode
def calculate_range(list):
    list.sort()
    return list[-1] - list[0]
def calculate_variance(list):
    result = 0
    mean=calculate_mean(list)
    for item in list:
        result+= item - mean
    result/=len(list)
    return result
def calculate_std(list):
    return calculate_variance(list)**.5