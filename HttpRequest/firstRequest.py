import requests
url = "http://www.goole.com"
response = requests.get(url)
#print(f"your request to {url} cambe back w/ status code {response.status_code}")

#print(response.text) # this is how the page response all the information present in the page but this is not human format.
# and we need to find a way that this will be more frendly format for python too

#Another example

url1 = "https://icanhazdadjoke.com/"
response = requests.get(url1, headers={"Accept" : "application/json"})


print(type(response.text)) # this a jason but the type is an string an I Can't ask for, you know, give me the joke in that string, beacuse it's is a string
# instead I can do that with :
print(response.json())
data = response.json()
print(data['joke']) # you can acceses to an specific value into the json

