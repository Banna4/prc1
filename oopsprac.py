#EENCAPSULATION

# class employee:

#     def __init__(self):
#         self.name = "Akash"
#         self.__selry = 5000

#     def show_selry(self):
#         return self.__selry()
    
# obj = employee()

# print(obj.name)
# print(obj.show_selry)

#INHERITANCE
# class parent:
#     def show(self):
#         print("PARENT")
# class Child(parent):
#     pass

# obj = Child()
# obj.show()

#POLYMORPHISM
# class Dog:
#     def sound(self):
#         print("Bhow bhow")
    
# class Cat:
#     def sound(self):
#         print("Meow meow")


# ani = [Dog(),Cat()]
# for i in ani:
#     i.sound()

#METHOD OVERRIDIING
class Parent:

    def show(self):
        print("Hellow from parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Hello from child")

obj = Child()
obj.show()