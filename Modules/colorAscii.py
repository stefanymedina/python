from pyfiglet import figlet_format 
from termcolor import colored

color_availables = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

message = input('What mesaage do you want to print?')
color = input('What color?')
if color not in color_availables:
    color = 'cyan'

result = colored(figlet_format(message), color)
print(result)