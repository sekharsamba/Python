"""
1.Lists are used to store multiple items in a single variable.
2.List items are ordered, changeable, and allow duplicate values.
3.If you add new items to a list, the new items will be placed at the end of the list.
4.The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
5. list is indicated with []

"""



# List
fruits = ["Apple","Banana","Cucumber","Dragon Fruit",1,2,3,"@"]
print(fruits, type(fruits))  # ['Apple', 'Banana', 'Cucumber', 'Dragon Fruit', 1, 2, 3, '@'] <class 'list'>

# allow duplicates
fruits = ["Apple","Banana","Cucumber","DragonFruit", "Banana","Apple"]
print(fruits, type(fruits)) # ['Apple', 'Banana', 'Cucumber', 'DragonFruit', 'Banana', 'Apple'] <class 'list'>

# changeable 
fruits = ["Apple","Banana","Cucumber","Dragon Fruit"]
fruits[0] = " Grapes"
print(fruits)   # [' Grapes', 'Banana', 'Cucumber', 'Dragon Fruit']


# add a new element
fruits = ["Apple","Banana","Cucumber","Dragon Fruit"]
fruits.append("Orange")
print(fruits)   # ['Apple', 'Banana', 'Cucumber', 'Dragon Fruit', 'Orange']


# Remove list item
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)   # ['apple', 'cherry']


# Loop through list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)      #apple
                #banana
                #cherry


