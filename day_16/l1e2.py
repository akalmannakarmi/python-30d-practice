# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime

current = datetime.now()
print(current.strftime("%m/%d/%Y, %H:%M:%S"))