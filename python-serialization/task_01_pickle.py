import pickle

class CustomObject:
        def __init__(self, name, age, is_student):
            self.name = name
            self.age = age
            self.is_student = is_student
        def serialize(self, filename):
            try:
                with open(filename, "wb") as file:
                    pickle.dump(self, file)
            except Exception as e:
                pass
        @classmethod
        def deserialize(cls, filename):
            try:
                with open(filename, "rb") as file:
                    return pickle.load(file)
            except Exception as e:
                return None
