# func ki return value ko ak objn ki property
# ki tarah istemal kar sakte ha or isko set
# bhi kar sakte ha

class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")

    # work for getter
    @property     #this is a property decorator
    def ten_value(self):
        return 10 * self._value

    #  for setter
    @ten_value.setter 
    def ten_value(self, new_value):
        self._value = new_value
        # return 10 * self._value 

obj = MyClass(10)       
obj.show()
# print(obj._value)
print(obj.ten_value)   #getter

obj.ten_value = 67  #this direct change will throw an error need propr syntx for setter

