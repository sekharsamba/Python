"""
Loops are Two Types
For
While

1. A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
2. loop or iterative  Statements
3. With the for loop we can execute a set of statements

"""

# forloop
for i in range(0,10):
     print(i)        # 0 1 2 3 4 5 6 7 8 9


# for loop range
for x in range(0,20,2):
    print(x)        # 0 2 4 6 8 10 12 14 16 18 

# using list
names = ["Sekhar","Samba","Siva","Raja"]
for x in names:
    print(x)     # Sekhar Samba Siva Raja
                   

# # using string
fruit = "Apple"
for i in fruit:
    print(i)    # A p p l e

# nested for loop
for i in range(1,5):
    for j in range(10,15):
        print(i*j)          #10 11 12 13 14 20 22 24 26 28 30 33 36 39 42 40 44 48 52
