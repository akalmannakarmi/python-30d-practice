# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter score: "))
if score>=90:
    print("A")
elif score>=70:
    print("B")
elif score>=60:
    print("C")
elif score>=50:
    print("D")
elif score>=0:
    print("F")
else:
    print("invalid")