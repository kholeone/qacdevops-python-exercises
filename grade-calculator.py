print("Welcome to Grade Calculator")

maths = int(input("Please enter your maths mark:"))
chemistry = int(input("Please enter your chemistry mark:"))
physics = int(input("Please enter your physics mark:"))

grade = maths + chemistry + physics

print("Your percentage score is:" + str(grade / 3))

if grade >= 40.0:
    print("You scored a grade of: D")
elif grade >= 50.0:
    print("You scored a grade of: C")
elif grade >= 60.0:
    print("You scored a grade of: B")
elif grade >= 70.0:
    print("You scored a grade of: A")
else:
    print("You failed")





