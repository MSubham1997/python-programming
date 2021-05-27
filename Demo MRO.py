class X:pass
class Y:pass
class Z:pass

class A(X,Y):pass
class B(Y,Z):pass



class C(A,B,Z):pass
for obj in C.mro():
    print(obj)