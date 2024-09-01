class Student(object):
    def __init__(self):
        self.__name=None
        self.__age= None
    def __set_name(self,name):
        if len(name.split(" ")) <3:
            raise ValueError("Name must be 3 words")
        else:
            self.__name= name
    def __get_name(self):
        return self.__name
    def __del_name(self):
        del self.__name

    def __len__(self):
        return len(self.__name)

    name = property(__get_name,__set_name,__del_name)

s1 = Student()
s1.name = "Ahmad Mahmoud Ali"

print(len(s1))
