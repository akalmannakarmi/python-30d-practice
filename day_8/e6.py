# Modify the skills values by adding one or two skills
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
student["skills"].append("eating")
student["skills"].append("bike")
print(student)