### Terminology
 - **Object-Oriented Programming** is used to manage bigger and complicated software
- **Classes** are the instructions to build different objects of the same **type**
- **Objects** or **values** or **instances (objects)** are built by classes
- When a new object is created we say that a new class instance has been created
- Classes and objects are referenced like nouns, while methods (also called **interfaces**) are referenced like verbs 
- **Instantiation** is the process of creating a new object from a class
- **Encapsulation** hides data and functionality behind method (or interfaces) mostly by convention. It serves as way to protect data and define clear boundaries, and let's you think of objects as nouns with actions (methods)
- **Polymorphism** is when different classes of objects are used through the same interface
- **Inheritance** is when a class (subclass) inherits the behaviors and properties of another class (superclass) so it can reuse and extend the code
-  **Properties** are getters that were created with the `@property` decorator
- A setter is a property value that could be reassigned
### Classes Define Objects
- A class is assigned to a variable. The variable references the object or instance of the class or that assigning to a variable means the class instance has been instantiated.
- **Class Constructor** is the same as calling a class as a function (Constructor)
- An object's **instance variables** or data can be initialized, accessed, replaced, or mutated through the class's instance methods and from outside the class
- **Instance methods** or **behaviors** are functions that are available and shared within the class instance
- **Attributes** are both instance variables and instance methods
- **Properties** are methods that are like instance variables that can be calculated
- **Magic method** or **dunder method** or **initializer** method, **instance constructor** or **constructor** initializes a new instance of an object (`__init__` method) (Initializer)
- `__new__` -> `__new__` method

### Inheritance
- **Inheritance** is where a superclass contains instance methods that subclasses can use

### States and Behaviors
- State are tracked via instance variables
- Behaviors are instance methods used by objects

### Object Scope
- Methods and instance variables inside of a class including via inheritance or mixins
- **Properties**


### Class Inheritance
- subclass or derived class of superclass
- superclass or base class of subclass
- a subclass of a subclass is also a subclass of a superclass
- a subclass is an instance of a superclass
- subclasses "inherit" (not really) superclass instances
- Don't Repeat Yourself
- "is-a" relationship

### The super Function
- Used to call functions in the superclass
- Common use case is to use it with the `__init__` method

### Multiple Inheritance
- Inherits and combines attributes from multiple superclasses
- Tricky rules for inherited methods with same names
- Very hard to implement without vast experience due to tradeoffs

### Mix-Ins
- Gives small specific behaviors to other classes as an interface
- Behavior-based helps avoid most of the MI tradeoff
- Naming convention using `Mixin` as a suffix

### "Is-a" vs "Has-a"

### Method Resolution Order (MRO)

### Curious
- Is polymorphism the same as inheritance

**Answering Framework**
1. Restate the question
2. Which code lines are being compared and contrasted?
3. What concept is being tested?
4. Compare the options
5. Add a "What If" Scenario
6. Answer in 2-4 clear sentences
