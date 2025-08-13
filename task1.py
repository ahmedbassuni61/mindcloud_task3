print("###################")
class Parent:
    def talk(self):
        print("Parent is talking")

class Child(Parent):
    def talk(self):
        print("Child is talking")
child1=Child()
print("What will happen if the child and the parent have the same method?")
child1.talk()
print("###################")


print("What will happen if two parents have the same parent?")
class Grandparent:
    def say(self):
        print("Hello from Grandparent")

class Parent1(Grandparent):
    def say(self):
        print("Hello from Parent1")

class Parent2(Grandparent):
    def say(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    pass
child = Child()
child.say()
print("###################")