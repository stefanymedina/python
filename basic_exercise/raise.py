# throw errors using the raise keyword. This is helpful when creating your own kinds of exception and error messages.


def colorize(text, color):
    colors = ('blue', 'white', 'red', 'purple')
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError(f"{color} is invalid color")
    print(f"Printed {text} in {color}")

#colorize("hello", "red") # this is fine
#colorize("hello", "cyan") # this i not good becuse the color is not in the tuple colors
#colorize(123, "red") # this is not good because the first argument is an int and the function is waiting for an string


# try
# except:
# else:
# finally:


def divide(num1, num2):
    try:
        print(int(num1/num2))
    except ZeroDivisionError:
        print("Please do not divide by zer")
    except TypeError:
        print("Please provide two integers or floats")


divide(1,0)