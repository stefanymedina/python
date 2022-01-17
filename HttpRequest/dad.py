from pyfiglet import figlet_format 
from termcolor import colored
from random import choice
import requests

banner = colored(figlet_format('Dad Joke 3000'), 'magenta')
print(banner)


topic = input('Let me tell you a joke! Give me a topic:')
url = "https://icanhazdadjoke.com/search"

response = requests.get(
        url, 
        headers={"Accept" : "application/json"},
        params={"term" : topic}
    ).json()

values = response['total_jokes']
res = choice(response['results'])
if values > 1:
    print("there are many jokes:")
    print(res['joke'])
elif values == 1:
    print("there is one joke:")
    print(response['results'][0]['joke'])
else:      
    print(f"sorry couldn't find a joke with yout term: {topic }")







