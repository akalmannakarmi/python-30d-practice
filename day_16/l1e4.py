# Calculate the time difference between now and new year.

from datetime import datetime

current = datetime.now()
newYear = datetime(current.year+1,1,1)
diff = newYear-current
print(diff)