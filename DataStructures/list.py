age = 19
has_license = True
my_list = ["Alice",25,age,True,has_license] #can contain different data types
name = my_list[0] #accessing the first element of the list
age = my_list[2] #accessing the third element of the list
has_license = my_list[-1] #accessing the last element of the list
print(name) #Output: Alice
print(age) #Output: 19
print(has_license) #Output: True
my_list.append("Bob") #add to end of the list
print(my_list)
my_list.insert(1,31) #add the value at the specified index
print(my_list)
my_list.remove("Alice") #removes by value  
print(my_list)
my_list.pop(2) #removes by index
print(my_list)