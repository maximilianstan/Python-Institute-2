import math
print(help("modules"))
# You need to put this command,`import` keyword along with the name of the module you want to import
num = 4
print(math.sqrt(num))

# Use dot operator to access sqrt() inside module "math"

for name in dir(math):
    print(name, end="\t")
    print("\n")

# Ceil outputs an integer greater or equal to the imputed number

x = math.ceil(5.35)
print("x =", x)

# Floor outputs an integer smaller or equal to the imputed number

y = math.floor(12.8)
print("y =", y)

# Comb - returns the number of ways to choose k items from n items without repetition and WITHOUT order
# Combinatii de k luate cate n

num_people = 10
num_seats = 6
x = math.comb(num_people, num_seats)
print(x)

# Perm - Returns the number of ways to choose k item from n items without repetition and WITH order

num_people = 18
num_seats = 5
x = math.perm(num_people, num_seats)
print(x)

# Copysign - Returns a float with magnitute x, but the sign of y
speed = 10
distance_moved = -3
velocity = math.copysign(speed, distance_moved)
print(velocity)

# Fabs(x) - returns the absolute value of x
x = math.fabs(-8.3)
print(x)

# Factorial - functie factoriala

x = math.factorial(55)
print(x)

# F mod (x, y) - Returns the modulus (remainder of x/y) as a float

x = math.fmod(100, 9)
print(x)

x = 100 % 9
print(x)

