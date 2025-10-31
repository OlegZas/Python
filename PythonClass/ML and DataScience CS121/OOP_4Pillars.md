# Object-Oriented Programming 4 PIllars 

## 1. Encapsulation

**Definition:**  
Encapsulation means bundling data (variables) and methods (functions) that operate on that data into a single unit — a class.  
It also restricts direct access to some of an object’s components to prevent accidental interference and misuse.

**Goal:**  
Protect the internal state of an object and control how it’s accessed or modified.

**Example (in Python):**

```
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

Here, `__balance` is hidden from direct access — you can only modify it via methods.

---

## 2. Abstraction

**Definition:**  
Abstraction means hiding complex details and showing only the essential features of an object.  
It helps simplify the interface and focus on *what* an object does instead of *how* it does it.

**Goal:**  
Reduce complexity by exposing only necessary operations.

**Example:**

```
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
```

You don’t need to know how `start_engine()` works — only that every `Vehicle` must have one.

---

## 3. Inheritance

**Definition:**  
Inheritance allows a child class to inherit properties and methods from a parent class.  
It promotes code reuse and a logical hierarchy between classes.

**Goal:**  
Reuse code and establish relationships between classes.

**Example:**

```
class Animal:
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("The dog is barking")

# Usage
dog = Dog()
dog.eat()   # inherited from Animal
dog.bark()
```

---

## 4. Polymorphism

**Definition:**  
Polymorphism means “many forms.”  
It allows objects of different classes to be treated as objects of a common superclass, even though they behave differently.

**Goal:**  
Enable one interface to be used for different data types or classes.

**Example:**

```
class Bird:
    def make_sound(self):
        print("Chirp")

class Dog:
    def make_sound(self):
        print("Bark")

for animal in [Bird(), Dog()]:
    animal.make_sound()
```
