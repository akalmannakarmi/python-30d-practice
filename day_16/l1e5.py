# Calculate the time difference between 1 January 1970 and now.

from datetime import datetime

current = datetime.now()
then = datetime.strptime("1 January 1970","%d %B %Y")
diff = current-then
print(diff)