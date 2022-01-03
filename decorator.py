'''pass a func as a parameter'''
def first_decorator(function):  
    def sub_message():
        print("Welcome to my country UK")
        function()
        print("Beautiful weather I love it")
    return sub_message()
def second_decorator():
    print("welcome to my country India") 
    
first_decorator(second_decorator)



''' Define a Decorator'''


def first_decorator(function):
    def sub_message():
        print("Welcome to my country UK")
        function()
        print("Beautiful weather I love it")
    return sub_message()
@first_decorator 
def second_decorator():
    print("welcome to my country India") 