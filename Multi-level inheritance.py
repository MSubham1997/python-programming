class GrandParents:
    def Propertyland(self):
        print("The Land given  for farming by Grand parents:")

class Parents(GrandParents):
    def PropertyHome(self):
        print("The home made by the Parents :")

class Child(Parents):
    def PropertyCar(self):
        print("The car bought by Son:")

c1= Child()
c1.Propertyland()
c1.PropertyHome()
c1.PropertyCar()