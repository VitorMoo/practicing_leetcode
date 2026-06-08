"""
Summary:
Class: The "blueprint" or "template" (the cookie cutter).
Object (Instance): The actual entity created from the class (the baked cookie).
Instance Attributes: Characteristics unique to each object (e.g., color).
Class Attributes: Characteristics shared by ALL instances of the class.
Methods: Actions or behaviors the object can perform.
Magic/Dunder Methods: Built-in methods with double underscores (like __init__ and __str__) that have special behaviors.
"""

class Cookie:
    # This attribute is shared across all instances of the Cookie class.
    # Every cookie created will belong to "Tech Bakery".
    bakery_name = "Tech Bakery"

    def __init__(self, color):
        """
        The __init__ method is the constructor.
        It runs automatically when a new object is instantiated.
        'self' refers to the specific object being created, ensuring
        that instance attributes belong ONLY to this specific object.
        """
        # Instance Attribute: Unique to each Cookie
        self.color = color

    def __str__(self):
        """
        The __str__ method defines the string representation of the object.
        It runs automatically when you use print(object).
        """
        return f"A delicious {self.color} cookie from {Cookie.bakery_name}!"


    def get_color(self):
        """Returns the value of the color attribute (Getter)."""
        return self.color
    
    def set_color(self, color):
        """Modifies the value of the color attribute (Setter)."""
        self.color = color


if __name__ == "__main__":

    # 1. Instantiating objects from the Class
    cookie_one = Cookie("Green")
    cookie_two = Cookie("Blue")

    # Accessing the methods to see each object's color
    print('Cookie one color is:', cookie_one.get_color())
    print('Cookie two color is:', cookie_two.get_color())
    
    # Printing the objects directly triggers the __str__ method
    print(cookie_one)
    print(cookie_two)

    # 2. Modifying the state of just ONE object
    # Notice that altering cookie_one does not affect cookie_two
    cookie_one.set_color("Yellow")

    print('Cookie one color is now:', cookie_one.get_color())
    print('Cookie two color is still:', cookie_two.get_color())