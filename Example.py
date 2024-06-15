
# variable
a=10
b=20
print(a if a > b else b)

a1,b1 = 30,20
print(a1 if a1 > b1 else b1)

# Arithmetic Operators
# 1. Addition
a,b=4,5
print( a + b) # 9

# 2. Subtraction
a2,b2 = 4,6
print(a2 - b2) # -2

# 3. multiplication
a,b=4,3
print(a*b) #12

# 4. division
a,b=4,3
print(a/b) # 1.33333333333

# 5. floor division
a,b = 4,3
print(a//b) # 1

# 6. modulus
a,b=6,5
print(a%b) # 1

# 7. exponentiation
a,b=3,4
print(a**4) # 81

# Assignment Operators 

# +=
a,b=3,4
a +=b
print(a) # 7

# -=
a,b =3,4
a -=b
print(a) # -1

# *=
a,b=4,3
a *=b
print(a) # 12

# /=
a,b=4,3
a /=b
print(a) # 1.333

# %=

a,b=3,4
a %=b
print(a) # 3

# //=
a,b = 4,3
a //=b
print(a) # 1

# **=

a,b=5,4
a *=b
print(a) #20

# &
a,b=10,5

a &=b
print(a) #0

# Comparison Operators

# ==
a,b=4,5
print(a==b) # False

# !=
a,b = 5,4
print(a !=b) # true

# <
a,b=6,7
print(a <b) # true

# <=
a,b=4,4
print(a <= b) # true

# >
a,b=5,4
print(a >b) # true

# >=
a,b=5,6
print(a >= b) # false

# Logical Operators
# and
a,b=10,5
print(a and b) # 5
print((a > b) and( a!=b)) # true

# or
a,b=10,5
print(a or b) # 10
print((a >b) or (a <= b)) # true

# not
a,b=10,5
print(not a) # false

# input function

print('enter e integer')
a = int(input())
b = int(input())
print(a + b)

























