"""
More on functions:
Functions with defaults
Functions with multiple arguments and keyword arguments
"""

# greeter function with default message and one name

def greeter(name, msg = "Welcome to the Python Course"):
    """
    Takes user input name and prints a welcome message
    with the name
    :param name: str
    :param msg: str
    :return: str
    """
    greeting = msg + ' ' + name
    return greeting

greetingmsg = greeter('Erik', 'Hello')
print(greetingmsg)

# greeter function to take as many arguments as you give it
def greeter_more(*names, msg='Hello'):
    """
    Takes user input name and prints a welcome message
    with the name
    :param name: str
    :param msg: str
    """
    for name in names:
        print(msg, name)

greeter_more('Ines')
greeter_more('Tilman', 'Kevin', 'Maryam', msg="Welcome")

# message function to store messages
# input type is msg1 = 'Hello', msg2 = 'How are you?'
def message_printer(*names, **messages):
    """
    Prints out messages and their names
    :param messages: str
    """
    print(type(messages))
    for name in names:
        for key, msg in messages.items():
            print(f'{key} {msg} {name}')

message_printer('Erik', 'Yin', msg1 = 'Hello', msg2 = 'How are you?')

