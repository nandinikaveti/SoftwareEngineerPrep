def create_profile(name, age = 18, **kwargs ):
    profile = {"name": name, "age": age}
    profile.update(kwargs)
    return profile

print(create_profile("Nandini", city="San Antonio"))

#here i am using functions to display name and age, since i am using **kwargs it does not throw an error for city but it does not display it either.
#In this case i can also use a class instead.

class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        return f"I am ", {self.name},"my age is ", {self.age} 


s1 = Profile("nandini", 26)
print(s1.intro())
