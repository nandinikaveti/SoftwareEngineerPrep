from dataclasses import dataclass
@dataclass
class Student:
    name : str
    grade : float
    email :str | None = None

    

s1 = Student("nandu", 74, "nand@gmail.com")
s2 = Student("Sanju", 85)