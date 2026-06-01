# #reverse string 
# a = "AKASH"
# b = ""
# for i in a:
#     b = i + b
# print(b)
# n = [1,2,4,5,6,3,2,6,1,1]
# b = set()
# dup = []
# dup1 = []
# for i in n:
#     if i in b:
#         dup.append(i)
#     else:
#         b.add(i)
# print(set(dup))
# def is_palendrom(a):
#     s = ""
#     for i in a:
#         s = i + s
#     if s == a:
#         return True
#     else:
#         return False
    
# a = "salos"
# print(is_palendrom(a))

# def greet(*args, **kwargs):
#     for name in args:
#         print("Hellow",name)
#     for k, v in kwargs.items():
#         print(k,"=",v)
# greet("raj","priya",city = "indore")

a = "Production"

# count = 0
# for i in a:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count += 1
# print(count)


# a = "akash"
# b = []
# for i in a:
#     b.append(i)
# print(b)
a = "akashA"

count = 0

# for i in a:
#     if i in "aeioAEIOU":
#         count += 1
# print(count)

a = [1,2,3,4,5,6]

# revers = []

# for i in a:
#     revers = [i] + revers
# print(revers)
# lg = a[0]

# for i in a:
#     if i >  lg:
#         lg = i
# print(lg)


student = {"akash":67,"mohit":56,"ram":67}

student.update({"rani":89})
student.pop('rani')
print(student.items())