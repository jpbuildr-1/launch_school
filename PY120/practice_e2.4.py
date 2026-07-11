class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()         # Instantiates a Hello object and assigns it to hello
hello.hi()              # Calls the hi method and it calls the self.greet method which outputs 'Hello'

hello = Hello()         # Instantiates a Hello object and assigns it to hello
hello.bye()             # Raises an AttributeError

hello = Hello()         # Instantiates a Hello object and assigns it to hello
hello.greet()           # Call the greet method that is inherited from the Greeting class and raises a TypeError because it is missing an argument

hello = Hello()         # Instantiates a Hello object and assigns it to hello
hello.greet('Goodbye')  # Calls the greet method and outputs 'Goodbye'

Hello.hi()              # Raises a TypeError because Hello is the class and hi is an instance method
