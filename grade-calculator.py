print("Welcome to Grade Calculator")

maths = int(input("Please enter your maths mark: "))
chemistry = int(input("Please enter your chemistry mark: "))
physics = int(input("Please enter your physics mark: "))

marks = maths + chemistry + physics
overall_percentage = marks / 3

print("Your percentage score is:" + str(overall_percentage) + "%")

if overall_percentage >= 40.0:
    print("You scored a grade of: D")
elif overall_percentage >= 50.0:
    print("You scored a grade of: C")
elif overall_percentage >= 60.0:
    print("You scored a grade of: B")
elif overall_percentage >= 70.0:
    print("You scored a grade of: A")
else:
    print("You failed")





