# Object Oriented Programming in Python

Python is a very interesting language and it has a lot of specifics. You can do a lot of hacky tings with it. We are not going to show all of the specifics and the hackness. If you are interested in it we recommend you the one and only python course at FMI - it rocks!.

This week introduces you to object-oriented programming, an important technique for writing complex programs. In an object-oriented program, you don't simply manipulate numbers and strings, but you work with objects that are meaningful for your application. Objects with the same behavior are grouped into classes. A programmer provides the desired behavior by specifying and implementing methods for these classes. At the end of this week you will learn how to discover, specify, and implement your own classes, and how to use them in your programs.

## Revision

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

If you can't explain one of these words. Go back to school!

## Build your first class in python

```python
class Panda:
    def __init__(self, weight, name, age):
        self.weight = weight
        self.name = name
        self.age = age

    
    def _get_fatter(self):
        if self.weight < 1000:
            self.weight += 1
    
    def eat_bamboo(self):
        self._get_fatter()
        print("Nomm nomm nomm!")

dimcho = Panda(1500, "Dimcho", 10)
print(dimcho.age)
print(dimcho.eat_bamboo())
```

- We use __init__ method as a constructor
- Every class method must take __self__ as a first argument
- You can access the attributes in class methods using __self__
- All methods that starts with _ are protected

## Magic methods that you can redefine for operators

```python
__eq__(self, other) # self == other
__add__(self, other) # self + other
__sub__(self, other) # self - other
__mul__(self, other) # self * other
__truediv__(self, other) # self / other
__floordiv__(self, other) # self // other
__mod__(self, other) # self % other
__lshift__(self, other) # self << other
__rshift__(self, other) # self >> other
__and__(self, other) # self & other
__xor__(self, other) # self ^ other
__or__(self, other) # self | other
```

## Static things 

A self-explaining example.

```python
class Panda:
    all_pandas = []
    pandas_count = 0

    def __init__(self, name):
        self.name = name
        Panda.pandas_count += 1
        Panda.all_pandas.append(name)

    @staticmethod
    def print_all_pandas():
        for panda in Panda.all_pandas:
            print panda.name

dimcho = Panda("Dimcho")
Panda.print_all_pandas() # Dimcho
```

## Inheritance

Another self-explaining example.

```python
class Panda:
    def __init__(self, weight, name, age):
        self.weight = weight
        self.name = name
        self.age = age

    
    def _get_fatter(self):
        if self.weight < 1000:
            self.weight += 1
    
    def eat_bamboo(self):
        self._get_fatter()
        print("Nomm nomm nomm!")


class KunkFuPanda(Panda):
    def __init__(self, weight, name, age, skill):
        Panda.__init__(self, weight, name, age)
        self.skill = skill

    def fight(self):
        self.weight -= 1    
        print("Bam bam!")
```

## Private and Protected

- You don't have an actual privacy in python
- Names that starts with _ are protected 
- Names that starts with __ are private

```python
class Panda:
    def __init__(self):
        self.__power = 42

jorko = Panda()
print(jorko.__power) # AttributeError: 'Panda' object has no attribute '__power'
```

