# Delete one of the items in the dictionary
student = {
    "first_name":"Alish",
    "last_name":"sth",
    "gender":"male",
    "age":18,
    "marital status":False,
    "skills":["writing","reading","c programming","office package"],
    "country":"America",
    "city":"New York",
    "address":"21 street"
}
student.pop("last_name")
student.popitem()
del student["country"]
print(student)