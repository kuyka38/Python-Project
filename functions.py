#built-functions/standard library functions

x = max( 67 , 55, 43, 33 ,99, 100 )
print("The maximum value is", x)

y = min(22, 45, 77, 20, 21, 12)
print("The minimum value is", y)

z = pow(2, 3)
print("The power of 2 is", z)

#user-defined functions
def greeting():
    print("Hello world!")
greeting()     #calling a function


def school ():
    print("MY Coding School is eMobilis")
school()

#parameters and arguments
def add (num1, num2):
    print(num1 + num2)

add(5, 10)
add(20, 10)

def student ( fullname,course,gender):
    print(fullname,course,gender)

student("Kuyuka Kunji","MIT","male")
student("James Kamau","MIT","male")
student("Tracy Ndege","MIT","female")
student("Julliet Some","Android","female")
student("Anitta Sanya","Cyber Security","female")
student("Caroline Nashipae","UI/UX","male")
student("Christine Bonareri","Data Science","female")


# create a python program that displays details of 5 employees at FinTech using Parameters and argument( display the fullname, email address, age , position, salary and marriage status )

def employee(fullname, emailaddress, age, position, salary, maritalstatus):
    print(f"{fullname} | {emailaddress} | Age: {age} | {position} | Salary: ${salary:.2f}| Married: {maritalstatus}")

employee("Evans woods", "woods@gmail.com", 22, "software developer", 100000, False)
employee("Brian hemisphere", "brian@gmail.com", 25, "Chief Manager", 120000, True)
employee("Cheryl putin", "chery@gmail.com", 26, "Data Analyst", 95000, False)
employee("David Ray", "davidray@com", 32, "Data Scientist", 110000, True)
employee("Eva Davids", "eva22@gmail.com", 21, "Finance Analyst", 105000, True)

