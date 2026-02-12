numbers = [3,1,5,7,9,2,1]
print(len(numbers))
print(numbers.count(1)) #returns the number of occurence of the particular number
print(numbers.index(5)) #returns the index position of the value
numbers.sort() #sort the list in aescing order by default
print(numbers)
numbers.reverse() #reverse the list
print(numbers)
new_list = numbers.copy() #copies the whole list
print(new_list)