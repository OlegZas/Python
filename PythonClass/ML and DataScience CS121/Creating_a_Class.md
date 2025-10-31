# Python Classes: Account Example

## 1. Defining a Class

In Python, a class is defined using the `class` keyword followed by the class name and a colon (`:`).  
This first line is called the **class header**.

**Class naming convention:**  
- Use `CapitalizedWords` for class names (e.g., `Account`) as recommended by PEP 8 (Python style guide).

**Indentation:**  
- All statements inside the class (the class body or suite) must be indented.

**Example:**

<!--
# account.py
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    pass
-->

- The **docstring** immediately after the class header describes what the class does.  
- You can view a class docstring in IPython:  
<!-- Account?  # shows the class and its docstring -->

---

## 2. Class Constructor (`__init__` method)

- When you create an object from a class (`account = Account(name, balance)`), Python calls the class’s **constructor**, which is the `__init__` method.  
- `__init__` is used to **initialize the object’s attributes**.  
- The first parameter of every method in a class must be `self`, which is a reference to the object being created.

**Example `__init__` method:**

<!--
def __init__(self, name, balance):
    """Initialize an Account object."""
    
    # Ensure the balance is valid
    if balance < Decimal('0.00'):
        raise ValueError('Initial balance must be >= 0.00.')
    
    # Assign attributes dynamically
    self.name = name
    self.balance = balance
-->

- `self.name` and `self.balance` are **object attributes** that are created when the object is instantiated.  
- Attributes are **added dynamically**, so an object does not have them until you assign them using `self.attribute_name = value`.  
- **Important:** Returning anything other than `None` from `__init__` will cause an error.

---

## 3. Special Methods

- Python classes can define **special methods** (like `__init__`) that have double underscores at the beginning and end.  
- These methods give objects standard behaviors (initialization, string representation, arithmetic, etc.).

---

## 4. Defining Other Methods

- Methods are functions defined inside a class.  
- They must have `self` as the first parameter to access the object’s attributes.

**Example: Deposit method**

<!--
def deposit(self, amount):
    """Deposit money to the account."""
    
    # Ensure the amount is valid
    if amount < Decimal('0.00'):
        raise ValueError('Amount must be positive.')
    
    # Update the balance
    self.balance += amount
-->

- This method adds a positive amount to the account balance.  
- If a negative amount is passed, it raises an exception.

---

## 5. Putting It All Together

**Full `Account` class example:**

<!--
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= 0.00.')
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money to the account."""
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be positive.')
        self.balance += amount
-->

**Key points to remember:**

1. `class` defines a new type of object.  
2. `__init__` initializes the object’s attributes.  
3. `self` is always required to access object data.  
4. Methods define the behavior of objects (like `deposit`).  
5. Attributes are dynamically added via `self.attribute = value`.  
6. Use docstrings to explain classes and methods.
