class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def get_name(self):
        return self.name  + " " + self.major