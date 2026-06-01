# def is_pelendrom(s):
#     return s == s[::-1]
# print(is_pelendrom("ramar"))
# def revers_str(s):
#     rs = s[::-1]
#     rs = rs.upper()
#     return rs
# print(revers_str("helan"))

# def fibonacci(n):
#     a, b = 0, 1
#     result = []
#     for i in range(n):
#         result.append(a)
#         a, b = b, a+b
#     return result 

# print(fibonacci(6))

# def remove_dup(arr):
#     return list(set(arr))
# print(remove_dup([1,1,2,2,2,3,3,3,4,4,4]))
# n = int(input())
# for i in range(n):
#         print("*" * i)
# n = [i for i in range (1,5)]
# print(n)

# s = lambda x: x*x
# print(s(9)) 
# s = lambda x,y: x+y
# print(s(5,7))


# text = "Zenqua"

# rev = ""
# for i in text:
#     rev = i + rev
# print(rev)


# text = "NARAYARAN"

# rev = ""
# for i in text:
#     rev = i + rev
# if rev == text:
#     print("Palindrom")
# else:
#     print("Not")

# n = [1,24,3,45,6]
# a = 0
# for i in n:
#     if i > a:
#         a = i
# print(a)
# num = [8,99,44,35,67,87,9,1]

# n = num[0]
# for i in num:
#     if i < n:
#         n = i
# print(n) 


# text = "Akash"
# c = 0
# for i in text:
#     c += 1
# print(c)

# text = "AKashCouhan"

# c = 0

# for i in text:
#     if i in "aeiouAEIOU":
#         c += 1
# print(c)


#febo
# a = 0
# b = 1

# for i in range(10):
#     print(a)

#     c = a + b
#     a = b
#     b = c

# n = 5

# f = 1
# for i in range(1,n+1):
#     f = f * i
# print(f)

# num  = [1,2,3,3,4,5,5,6,6,7]

# unique = []

# for i in num:
#     if i not in unique:
#         unique.append(i)
# print(unique)

# num  = [1,2,2,2,3,4,5,5,6,7,7,8,89]
# print(list(set(num)))


# n = (1,2,3,5)

# for i in n:
#     if i == 2:
#         n.count(1)
# print(n)


# n = 170000001

# r = 0

# while n > 0:
#     digit = n % 10
#     r = r * 10 + digit
#     n = n // 10
# print(r)

# n = "StreangerThings"
# r = ""

# for i in n:
#     r = i + r
# print(r)

# def revers_arr(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1

#     return arr

# print(revers_arr([1,2,4,6,7,8]))

# n = [1,2,2,2,2,1,1,2,4,4,5,6,6,7,8,9,1,2,3,4,5]


# seen = set()
# dup = set()

# for i in n:
#     if i in seen:
#         dup.add(i)
#     else:
#         seen.add(i)
# print(list(dup))

# n = (7,8,9,0)
# print(n)

# n = int(input("Enter you no."))
# orignal = n
# r = 0

# while n > 0:
#     digit = n % 10
#     r = r * 10 + digit
#     n = n // 10
# if r == orignal:
#     print("Is palindrom")
# else:
#     print("Is not")


# s = "sts"

# r = ""
# for i in s:
#     r = i + r
# print(r)
# if r == s:
#     print("t")

# n = [1,1,6,6,1,2,2,3,3,34,4,7,8,8]

# seen = set()
# rev = set()

# for i in n:
#     if i in seen:
#         rev.add(i)
#     else:
#         seen.add(i)
# print(list(rev))

def my_decore(func):
    def wapper():
        print("Before decoratore")
        func()
        print("After decore")
    return wapper
@my_decore
def hello():
    print("Decorator")

hello()