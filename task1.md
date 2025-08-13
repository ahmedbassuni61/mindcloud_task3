# Task_1.1
## Shallow Copy
### Definition
A shallow copy creates a new object but does not recursively copy the objects inside it. Instead, it stores references to the nested objects of the original.
### Characteristics
-Top-level object is duplicated.
-Nested objects are shared between the original and the copy.
-Modifying a nested object in the copy will also modify it in the original.
## Deep Copy
### Definition
A deep copy creates a new object and recursively copies all nested objects inside it. The copy and original do not share any mutable sub-objects.
### Characteristics
-Both the top-level object and all nested objects are duplicated.
-No shared references between the copy and the original.
-Changes in one do not affect the other.
# Task_1.1
# Multiple inheritance
## 1-If a child class and a parent class have a method with the same name in Python, the child class’s method will override (replace) the parent’s method when called from an instance of the child.
## 2-If two parents share the same parent (i.e., multiple inheritance with a common ancestor), Python will use the Method Resolution Order (MRO) to decide which method to run.