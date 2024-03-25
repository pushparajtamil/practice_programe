## basics
print("Hello word")

### identation (four space or one tab) if,while,for

if 6>2:
    print("yes")
else:
    print("no")

## if condition 
if 5>2:
    print("yes")
else:
    print("No")
 
## variables it is used to store  data or values or list or string or assign a value to it.
## in variables you doesn't use int, - , special character *,-,#,% 
""" it is also mentioned as comment -"""  """"""
a = 20
print(a)
b = 30
print(b)
name = "tamil"
print(name)
subject = "tamil"
print(subject)
a_b=23
print(a_b) # 
# 1 = "tamil"
# print(1)
# 3 = "raji"
# print(3)



###  assign same 

# a=5
# a=6
# print(a)
## global overall or outside of a function
## local inside the function or loop 


a=4
if a>2:
    print(a)
    a=5
    c=a+2
    print(c)
else:
    print("no")

print(a)


## casting


a = str("2")
b = float(5.5)
c = str("pushpu")
print(a)
print(type(a))
print(b)
print(c)
c= float(4)
print(c)


##Camel Case 
myVariableName = "John"

##Pascal Case
MyVariableName = "John"


##Snake Case
my_variable_name = "John"


##multiple values assign

a,b,c = 2,3,7
print(c)
print(b)
x = y = z = "Orange"
print(z)


## it is not possible to string and int

# a=3
# b="kjdap"
# print(a+b) # its shows error


## functions

def pushpu():
    print(5)
pushpu()