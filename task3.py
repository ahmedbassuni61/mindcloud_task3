class Smartphone:
    def __init__(self):
        self.__contacts=[]
    def add_contact(self,name):
        if name not in self.__contacts:
            self.__contacts.append(name)
            print(f"{name} added")
        else:
            print("Already exists")
    def remove_contact(self,name):
        if name in self.__contacts:
            self.__contacts.remove(name)
            print(f"{name} removed")
        else:
            print(f"name {name} Doesn't exist")
    def make_call(self):
        print("####################")
        name=input("Enter name: ")
        if name in self.__contacts:
            print(f"Calling {name}")
        else:
            print(f"name {name} Doesn't exist")  
    def take_pic(self):
        print("The picture was taken successfully")
smartphone1=Smartphone()
smartphone1.add_contact("ahmed")
smartphone1.add_contact("ahmed")
smartphone1.remove_contact("mohammed")
smartphone1.make_call()
smartphone1.take_pic()