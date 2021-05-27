class Father:
    def FatherProperty(self):
        print("Father's property")

class Mother:
    def MotherProperty(self):
        print("Mother's proerty")

class Child(Father,Mother):
    def Property(self):
        print("Child will inherit property from:")
        super().FatherProperty()
        super().MotherProperty()
c1=Child()
c1.Property()