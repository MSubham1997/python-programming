class Test:
     staticVariable =0
     instanceVariable =0
     def __init__(self):
         print("Constructing the object for the test class")
         self.instanceVariable +=1
         Test.staticVariable +=1




t1=Test()
print("After creating the first object :")
print("InstanceVariable :" , t1.instanceVariable)
print("staticVariable :", t1.staticVariable)


t2=Test()
print("After creating the second object :")
print("InstanceVariable :" , t2.instanceVariable)
print("staticVariable :", t2.staticVariable)
print("StaticVariable using the class ref:", Test.staticVariable)