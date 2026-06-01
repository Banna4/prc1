# # marks = [23,45,67,89,23,23]
# # marks.append(34)
# # marks.extend([1,2,3])
# # marks.insert(3,99)
# # marks.remove(99)
# # marks.pop()
# # marks.sort()
# # marks.reverse()
# # a = marks.copy()
# # print(a)
# # print(marks)
# # print(marks.index(67))
# # print(marks.count(23))

# # DICTIONARY

# marks = {"Mohan":23,"Yuvi":34,"Ajit":56,"Niku":89}
# print(marks)
# print(marks.get("Mohan"))
# print(marks.keys())
# print(marks.values())
# print(marks.items())
# marks.update({"Anu":99})
# print(marks)
# marks.pop("Yuvi")
# print(marks)
# marks.popitem()
# print(marks)
# # marks.clear()
# print(marks)
# mark = marks.copy()
# print(mark)
# keys = ["a","b"]
# d = dict.fromkeys(keys,0)
# print(d)

# FIND SUM OF LIST
# a = [1,2,3,4]
# sum = 0
# for i in a:
#     sum += i
# print(sum)

# # FIND MAXIMUM
# a = [10,5,20,8]
# max = 0
# #print(max(a)) #with inbult max function 
# for i in a:
#     if i > max:
#         max = i
# print("Maximum number is ", max)

# COUNT EVEN NUMBERS
# a = [1,2,3,4,6]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
# print(count)


# REVERS A LIST WITHOUT INBUIT FUNC
a = [1,2,3]
# a.reverse()#by func
# r = a[::-1] # by list slicing 
# print(r)
#BY WHILE LOOP 
# def reverse_in_place(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         #swap element
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#     return arr
# print(reverse_in_place(a))

# CREATE A DICT FROM TWO LIST 
# keys = ["a","b","c"]
# values = [1,2,3]
# result = dict(zip(keys,values))# zip pairs same elements and dict creates dictionary
# print(result)

