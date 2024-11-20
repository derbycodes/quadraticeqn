import math
def quadratic_equation_roots(a, b, c):
  discriminant = b**2 - 4*a*c
  if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a) 
    print("The roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
  elif discriminant == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root =", root)
  else:
    print("The roots are imaginary.")

# Get coefficients from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
## Importing the Math Module:
# import math
#This line imports the math module, which provides various mathematical functions, including the square root function (sqrt).
#Defining the Function:
#def quadratic_equation_roots(a, b, c):
#This line defines a function named quadratic_equation_roots that takes three parameters: a, b, and c. 
# These represent the coefficients of a quadratic equation in the form ax^2 + bx + c = 0.
#Calculating the Discriminant:
#4. Checking the Discriminant:
#If the discriminant is positive:
#The equation has two distinct real roots.
#The roots are calculated using the quadratic formula and printed.
#If the discriminant is zero:
#The equation has two equal real roots.
#The root is calculated and printed.
#If the discriminant is negative:
#The equation has two complex roots, which are not real numbers.
#Getting User Input:
#a = float(input("Enter the coefficient a: "))
#b = float(input("Enter the coefficient b: "))
#c = float(input("Enter the coefficient c: "))
#These lines prompt the user to input the values of the coefficients a, b, and c.
#Calling the Function:
#quadratic_equation_roots(a, b, c)
#This line calls the quadratic_equation_roots function, passing the user-provided coefficients as arguments.