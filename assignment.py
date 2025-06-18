# A python program that checks whether a number is even or odd

number = int(input("Enter your number :"))

if number % 2 == 0:
    print("The number is even.")

else :
    print("The number is odd.")

print()


# A python program that checks whether a letter is a vowel or consonant

letter = input("Enter a letter: ").lower()
if len(letter) == 1 and letter.isalpha():

  if letter not in ['a', 'e', 'i', 'o', 'u']:
     print("The letter is a consonant.")

  else:
   print("The letter is a vowel.")

else:
  print("Please enter a single alphabet letter.")

print()


#A python program that returns the perimeter of a rectangle
length = int(input("Enter the length of the rectangle : "))
width = int(input("Enter the width of the rectangle : "))

perimeter = 2 * (length + width)

print("The perimeter is", perimeter)
