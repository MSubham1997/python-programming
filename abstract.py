from abc import ABC, abstractmethod
class Institute(ABC):
    def __init__(self):
        print(type(self). __name__, "Detials :")

    def courseOffered(self):
        print("Course offered :C, C++, java, .NET")
    @abstractmethod
    def address(self):pass

class TechnoAccedemy(Institute):
    def courseOffered(self):
        print("Course offered : Python, Data science , Dev-ops, AWS ")
    def address(self):
        print("The accedemy is at hyderabad")

class OnlineAccedemy(Institute):
    def address(self):
        print("Address @ Bangalore")
inst=Institute
ta=TechnoAccedemy()
ta.courseOffered()
ta.address()

olt=OnlineAccedemy()
olt.courseOffered()
olt.address()
