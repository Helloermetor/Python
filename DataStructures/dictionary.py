# in dic, {} used to store information and [] used to retrieve the information
person = {
    "name":"Soumo",
    "age": 21,
    "Gender":"Male" 
} #to store information

Age = person["age"] # retrieve the information
print(Age)
person["name"] = "Dave" #modifies the single key
print(person) #prints the whole dictionary
print(person.keys()) #prints the keys of dic
print(person.values()) #prints the values of each key in dic
print(person.items()) #prints keys with values of dic in list

if "name" in person: #checks whether the key exists in dic
    print("The key exists")
else:
    print("the key is not found")

person.update({"age":31,"Gender":"Female"}) #modifies multiple keys
print(person)