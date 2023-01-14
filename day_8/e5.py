# Get the value of skills and check the data type, it should be a list
student = {
    "first_name":"Alish",
    "last_name":"sth",
    "gender":"male",
    "age":18,
    "marital status":False,
    "skills":["writing","reading","c programming","office package"],
    "country":"America",
    "city":"New York",
    "address":"21 street",
}
print(type(student["skills"]))