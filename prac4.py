# a = [i for i in range (1, 11) ]
# print(a)
# print([ i*i for i in range(1,9)])
# square = lambda x: x*x
# print(square(2))


# def my_func(func):
#     def wrapper():
#         print("Hey")
#         func()
#         print("Sir")
#     return wrapper

# @my_func
# def Yfunc():
#     print("Akash")

# Yfunc()

# def count(a):
#     frequ = {}
#     for i in a:
#         if i in frequ:
#             frequ[i] += 1
#         else:
#             frequ[i] = 1

#     return frequ
# a = "mohhan"
# print(count(a))

# a = [1,2,3,99,4,5,55,888]

# larg = a[0]
# for i in a:
#     if i > larg:
#         larg = i

# print(larg)
# n = 10
# a = 0
# b = 1
# pln = []
# for i in range(n):
#     pln.append(a)
#     a,b = b , a+b

# print(pln)

# n = 128
# r = 0
# while n > 0:
#     digit = n%10
#     r = r*10 + digit
#     n = n//10

# print(r)

# n = "AKash"

# r = ""
# for i in n:
#     r = i + r

# print(r)
# a = 10
# b = 23

# a = a + b
# b = a - b
# a = a - b

# print(a)
# print(b)



def revers(a):
    left = 0
    right = len(a) - 1

    while left < right:
        a[left],a[right] = a[right],a[left]
        left += 1
        right -= 1
    return a
print(revers([1,2,3,4,5,5]))