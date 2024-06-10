from datetime import datetime, timezone


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = (datetime.now(timezone.utc))
        return utc_time
    # 'Static method' is shared by all instances of the class in the same way that the 'power_source' class attribute
    # of our Kettle class was shared by all instances.
    # Notice that it's defined above '__init__', it has no 'self' parameter and also having 'staticmethod' annotation
    # above the def.

    # The convention is that names starting with an underscore are non-public even though if you remember there's
    # nothing in Python that enforces this, so the 'Account' class is concerned with managing bank accounts not with
    # dates and times, so although clients can call the 'current_time' method, the underscore makes it clear that this
    # method isn't intended to be used outside the class.

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self.transaction_list.append((datetime.now(timezone.utc), amount))
            # Refactoring above:
            self._transaction_list.append((Account._current_time(), amount))  # We are explicitly creating a tuple
            # with the current timestamp and the amount so that we can add them as a tuple.

            # On tuples we said that you can assign a value to several variables in a single assignment statement by
            # using a tuple (line 17), and that's all it's really happening in the for loop in 'show_transactions'
            # method instead of just assigning a value to a single variable for each value in the list.

            # Python then unpacks the tuple and assigns the value to both data and amount at the same time (line 43).

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
            # Notice that we do not use 'self' when calling static methods on class but the class name then underscore
            # and the static method's name.
            # We also could 'self' while calling our static method, but there's no advantage to doing so, and in actual
            # fact performance slightly suffers because Python will first attempt to find the method in the instances
            # namespace and when it fails it then checks the class name space; so if you know you got a static method,
            # best to leave it there just save that little bit of time and to make it clear also in the code that it is
            # a static method.
        else:
            print("The amount must be greater then zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print(f"{amount} {tran_type} on {date} (local time was {date.astimezone()})")


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()
    tim.withdraw(2000)
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()

"""
:::Non-Public and Mangling:::

In Python, non-public members and name mangling are mechanisms used to indicate the intended scope and access 
level of attributes and methods within a class. These features are not about strict enforcement but about guiding 
the use of attributes and providing some level of name protection, especially in the context of inheritance and 
subclassing.

Non-Public Members Non-public members are attributes or methods intended for internal use within a class or module. 
By convention, their names start with a single underscore (_).

Single Underscore (_): This indicates to the programmer that the member is intended to be private and should not be 
accessed directly. However, it is only a convention and does not prevent access.

class MyClass: 
    def __init__(self): 
        self._private_attribute = "I am private"

    def _private_method(self):
        return "This is a private method"

obj = MyClass() 
print(obj._private_attribute)  # Accessible but not recommended 
print(obj._private_method())   # Accessible but not recommended 


Name Mangling: 
Name mangling is a mechanism where Python internally changes the name of a member to include the class name, making it
harder to accidentally access it from outside the class. This is done by prefixing the member name with two underscores
 (__).

Double Underscore (__): This triggers name mangling, making the attribute or method name unique to the class. This is 
especially useful to avoid name clashes in inheritance hierarchies.
 
class BaseClass: 
    def __init__(self): 
        self.__mangled_attribute = "I am mangled"

    def __mangled_method(self):
        return "This is a mangled method"

    def access_mangled(self):
        return self.__mangled_method()

obj = BaseClass()

# Direct access will fail
# print(obj.__mangled_attribute)  # AttributeError
# print(obj.__mangled_method())   # AttributeError

# Access through the correct mangled name 
print(obj._BaseClass__mangled_attribute)  # Accessible with mangled name 
print(obj._BaseClass__mangled_method())   # Accessible with mangled name
 
In the example above, __mangled_attribute and __mangled_method are internally renamed to _BaseClass__mangled_attribute 
and _BaseClass__mangled_method respectively. This renaming prevents accidental access or overriding in subclasses.

Summary
Single Underscore (_): Used to indicate that a member is intended for internal use. It is a convention and not enforced by Python.
Double Underscore (__): Triggers name mangling to make the member name unique to the class, preventing accidental access or overriding in subclasses.
These mechanisms help manage access and maintain the integrity of data within classes, making code more readable and less error-prone.
"""
