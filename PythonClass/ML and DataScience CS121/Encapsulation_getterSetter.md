# Read-Write Properties

When you use a property, you're essentially treating a method as if it were an attribute. However, this method (called the getter or setter) allows you to control how the attribute is accessed or modified. This is an important feature for:

- **Validation**: With properties, you can enforce rules when setting an attribute's value. For example, an hour should be between 0 and 23, or a minute should be between 0 and 59.
- **Encapsulation**: You can "hide" the internal representation of the data (such as `_hour`, `_minute`, and `_second`) from the user of the class. The underscore prefix is a convention to indicate that these variables should not be directly accessed outside the class.

## Getter and Setter Methods

Properties allow you to define getter and setter methods that are accessed like normal attributes. This gives you the best of both worlds:

- **Getter** (`@property`) allows you to access the attribute value as if it were just a regular attribute (e.g., `time.hour`).
- **Setter** (`@hour.setter`) allows you to control what happens when someone tries to set the value (e.g., `time.hour = 6`), enabling you to validate the value before modifying the internal data.

### Example: Validation with Setter

<!-- 
@property defines a getter for the 'hour' attribute
-->
@property
def hour(self):
    """Get the hour."""
    return self._hour

<!--
@hour.setter defines a setter for the 'hour' attribute
-->
@hour.setter
def hour(self, hour):
    """Set the hour, ensuring it's between 0 and 23."""
    if not (0 <= hour < 24):
        raise ValueError(f"Hour ({hour}) must be between 0 and 23.")
    self._hour = hour

This design ensures that:

- If someone tries to set an invalid hour, like 25, the setter will catch the error and raise a `ValueError`.
- The getter simply returns the value of `_hour`, without any extra logic, making it easy for the user of the class to retrieve the hour.

## Why not just use attributes directly (`self._hour`)?

Using `self._hour` directly without properties would expose the internal implementation of the class. You'd lose the ability to validate the values when they are set. The code would look like this:

<!-- 
Directly using internal attributes without properties
-->
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour  # Internal attribute
        self._minute = minute
        self._second = second

With this design, you lose the ability to add validation or any other logic around the access and modification of the attributes. The client code (the code that uses the `Time` class) could set `self._hour` to any invalid value like 25, without triggering any error or validation, which might lead to bugs.

## The hour property is like a "smart" attribute

The `property` method makes the `hour`, `minute`, and `second` appear as normal attributes, even though they are backed by methods. To the user of the `Time` class, the access to `hour`, `minute`, and `second` looks the same as if these were regular attributes. For instance:

<!-- Example usage -->
wake_up = Time(hour=6, minute=30)
print(wake_up.hour)  # Calls the getter, prints 6

wake_up.hour = 10   # Calls the setter, updates _hour to 10

But under the hood:

- The getter method is called when you access `wake_up.hour`.
- The setter method is called when you assign a value to `wake_up.hour`.

## Why use the underscore (e.g., `_hour`) for internal attributes?

The underscore (`_hour`) is a convention in Python to indicate that an attribute is "private" or "internal" and should not be directly accessed outside the class. However, Python does not enforce this, and it’s just a guideline. The real enforcement comes from the getter and setter methods, which control access to `_hour`.

## Advantages of using properties

- **Cleaner Code**: Properties provide a clean, readable way to access and modify data, without having to call explicit getter/setter methods.
- **Validation**: As mentioned, you can ensure that invalid data isn’t set, which is important when working with values that have constraints (like hours, minutes, and seconds).
- **Future-Proofing**: If you decide to change how the internal attributes are stored (e.g., switching to a more complex structure), you don't need to change the external API. You can modify the getter and setter logic without affecting the user's code.

### Example: Using the `Time` class with Properties

<!-- Create a Time object with hour=6, minute=30 -->
wake_up = Time(hour=6, minute=30)

<!-- Accessing the hour using the getter (this looks like a normal attribute) -->
print(wake_up.hour)  # 6

<!-- Setting the hour using the setter (with validation) -->
wake_up.hour = 10  # Valid

<!-- This will raise a ValueError because the hour is out of range -->
try:
    wake_up.hour = 25  # Invalid hour
except ValueError as e:
    print(e)  # "Hour (25) must be 0-23"

Without properties, you'd have to manually validate each attribute, and there would be no encapsulation around the hour, minute, and second values.

## Summary

By using properties, you're essentially making your class more flexible, safe, and maintainable. The main benefits are:

- **Data Encapsulation**: Hiding the internal representation of the data (like `_hour`) from the user.
- **Validation**: Ensuring that invalid values can't be set (like an hour of 25).
- **Cleaner and More Readable Code**: The class user doesn't need to know or care about getter and setter methods; they just interact with the hour, minute, and second properties.

In short, properties are a way to provide controlled access to an attribute, allowing you to define behavior when getting or setting the value, while keeping the interface simple and intuitive for the user.
