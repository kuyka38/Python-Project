courses = ["Python", "Android", "Cyber security", "Full-stack", "Data-science"]
print(courses)
#accessing an element in an array just use the index position to access it
print(courses[2])

print()

#looping through an array
for course in courses:
    print(course)

# adding a new element
courses.append("UI/UX")
print(courses)

# removing an element
courses.remove("Python")
print(courses)