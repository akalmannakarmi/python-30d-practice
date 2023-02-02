# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

current = datetime.now()
print(f"Day: {current.day}")
print(f"Month: {current.month}")
print(f"Year: {current.year}")
print(f"Hour: {current.hour}")
print(f"Minute: {current.minute}")
print(f"itemstamp: {current.timestamp()}")