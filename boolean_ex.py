# # def pushpa():
# #     A="PUSHPA"
# #     B="TAMIL"
# #     C=A+B
# #     return C
# # obj=pushpa()

# # print(obj)

# age=16
# def Qualifaction(): 
#     if age >=18:
#         print("eligeble to vote")
#     else:
#         print("not eligeble to vote")
# Qualifaction()
    
# division /
a,b=(3,2)
print(a/b)

# modulus -% - its shows only remaining values
print(a%b)

#floor division (//) its shows without decimal value
print(a//b)

#Exponentiation same as 2*2*2*2*2
x=2
y=5
print(x**y)

# a=[4]
# print(type(a))

box=["apple","cherry","nuts","nuts"]
print(box)
print(type(box))
print(len(box))
# I want to print fourth value in the list?
print(box[3])
# print 2 values you should use negative index
print(box[-3])
#i want to print first three values in the list?
print(box[0:4])
print(box[:3])
print(box[0:])

if "apple" in box:
    print("yes")
else:
    print("no") 

#change Concept : 
a=[1,2,3,4,5]    
a[2]=6
print(a)
a[1:4]=[1,2,3]
print(a)

# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

#insert
a.insert(4,6)
print(a)

#append - add new item in the list -it will be added on last data in the list
a.append("pushpa")
b=[10,'tamil']
for p in range(0,10):
    print(p)
    a.append(p)
print(a)

x=["pushpa","tamil","valar","seetha"]
Z=["cricket","carom","hocky","ches"]
x.extend(Z)
print(x)

# #remove
# x.remove("carom")
# print(x)

# #pop - using index value
# x.pop(6)
# print(x)

# #delete - using only index value
# del x[5]
# print(x)

# #clear - to clear all the data
# x.clear()
# print(x)

#Loop throug a list by using "for"
for i in x:
    print(i)

#List Comprehension --  one line function
school=["student","principle","teacher"]
for i in school:
    print(i)

print(a)

z=[a for a in school if "s" in a]
print(z)

#sort  - it means assending the list values
school.sort()
print(school)

#sort decending - reverse true
school.sort(reverse=True)
print (school)

#copy list

a=[1,2,3]
b=a.copy()
print(b)

#join list
a=[5,6,7]
b=[7,8,9]
c=a+b
print(c)


