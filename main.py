
print("Hello")
class Mobile:
    fp='Yes'
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("Fingerprint:",cls.fp)
        print("Ram:",r)
realme=Mobile()
Mobile.show_model('16GB')