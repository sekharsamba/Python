"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

1) if
2) if - else
3) if - elif - else
4) nested if

"""

# if statement
age = 18
if age == 18:
    print('eligible to vote')       # eligible to vote


# if - else
age > 20
if age>19:
    print("U can ride bike")        # U cant ride bike
else:
    print("U cant ride bike")


# if - elif - else
age = 17
if age > 18:
    print("you can vote")
elif age == 18:
    print("Correct age to vote")
else:
    print("Sorry You must be 18 years")  # Sorry You must be 18 years


# nested if
marks = 40
if marks > 35:
    print("You Pass the Exam")      # You Pass the Exam
    if marks > 40:
        print("Congrats !,You are Qualified")
    else:
        print("You are not Qualified ")     # You are not Qualified 
else:
    print("You are Fail")

