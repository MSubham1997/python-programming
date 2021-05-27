class English:
    def greet(self, name):
        print("Good moring", name)
class French:
    def greet(self, name):
        print("Adriqnaa",name)

    def greetings(language,name):
        language.greet(name)



english = English()
french = French()
greetings(english, "Subham")
greetings(french, "Subham")
