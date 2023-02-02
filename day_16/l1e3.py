# Today is 5 December, 2019. Change this time string to time.

from datetime import datetime

d = datetime.strptime("5 December, 2019",'%d %B, %Y')
print(d)