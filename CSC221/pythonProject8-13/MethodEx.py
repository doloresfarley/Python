def introduce(*args, **kwargs):
    for name in args:
        print(f"Hi, {name}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

# Example usage:
introduce("Alice", "Bob", age=30, city="New York")
# Output:
# Hi, Alice!
# Hi, Bob!
# age: 30
# city: New York
