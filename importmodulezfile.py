import math
print(help("modules"))
# You need to put this command,`import` keyword along with the name of the module you want to import
num = 4
print(math.sqrt(num))

# Use dot operator to access sqrt() inside module "math"

for name in dir(math):
    print(name, end="\t")

# Ceil outputs an integer greater or equal to the imputed number

x = math.ceil(7.45)
print("x =", x)

# Floor outputs an integer smaller or equal to the imputed number

y = math.floor(8.7)
print("y =", y)
