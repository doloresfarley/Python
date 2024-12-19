''''
In programming, "operator overloading" is used instead of "operator overriding" because when you overload an operator, you are essentially defining a new behavior for that operator specifically for a user-defined type, while still keeping the same operator symbol, whereas overriding would imply changing the behavior of an existing operator for a derived class in an inheritance hierarchy, which is not the case with operator overloading; you are essentially creating a new, distinct implementation for the operator based on the type of operands involved.
Key points to remember:
Overloading:
Multiple definitions for the same operator, each with different parameter types, allowing the operator to work with different data types.
Overriding:
Changing the implementation of an inherited method in a derived class, where the method signature remains the same.
Example:
Imagine creating a class called "Complex" to represent complex numbers. You can overload the "+" operator to define how to add two complex numbers, essentially giving the "+" operator a new meaning for your "Complex" class, but you are not overriding the existing "+" operator for other data types.

'''