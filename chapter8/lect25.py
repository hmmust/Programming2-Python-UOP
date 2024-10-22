import random
class Student:
    count =0 # class variable - static in java
    """def __init__(self):
        self.id = 0
        self.name=""
        self.spec="" """
    def __init__(self,id,name,spec): # constructor
        self.id = id
        self.name=name
        self.spec=spec
        self.__balance=0 # hidden variable
        Student.count+=1
    def __str__(self): # convert to string (toString in Java)
        return f"{self.id},{self.name},{self.spec}"

    def __eq__(self, other): # configure == operator
        if self.id == other.id and self.name== other.name:
            return True
        else:
            return False
    def __del__(self): # destructor (on delete of object)
        Student.count -= 1

class BSStudent(Student):
    def __init__(self,id,name,spec,gpa):
        super().__init__(id,name,spec)
        self.gpa = gpa
        self.email=""
        self.password = ""
    def __str__(self):
        return f'{super().__str__()},{self.email},{self.password},{self.gpa}'
    def generate_email(self):
        self.email= f'{self.name.lower()}@uop.edu.jo'
    def generate_password(self):
        self.password= f'{self.name.lower()[0]}@{random.randint(100,999)}'