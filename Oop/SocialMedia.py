class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

c1 = Comment("davey123","lol you're so silly",3)
print(c1.likes)
