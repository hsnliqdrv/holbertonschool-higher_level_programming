import pickle

class CustomObject:
        def __init__(self, name, age, is_student):
            self.name = name
            self.age = age
            self.is_student = is_student
        def serialize(self, filename):
            with open(filename, "w") as file:
                pickle.dump(self, file)
        @classmethod
        def deserialize(cls, filename):
            with open(filename, "r") as file:
                return pickle.load(filename)
