# Write a pattern which identifies if a string is a valid python variable

import re

txt = "asdas"
data = re.findall(r"^[0-9]|[ \-!@#$%^&*()]",txt)
if data:
    print("NO")
else:
    print("Yes")