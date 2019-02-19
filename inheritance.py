
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    defs show_info(self):
        print("Last Name: "+self.last_name)
        print("Eye Color: "+self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys
#method overriding
    def show_info(self):
        print("Last Name: "+self.last_name)
        print("Eye Color: "+self.eye_color)
        print("Number of toys : "+str(self.num_of_toys))


miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()

#print(miley_cyrus.last_name)
#print(miley_cyrus.num_of_toys)
