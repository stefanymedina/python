def copy(file1, file2):
    with open(file2, "w") as filec:    
        with open(file1) as file:
            filec.write(file.read())

def copy_and_reverse(file1, file2):
    with open(file1) as file:
        text = file.read()
    with open(file2, "w") as file1:
        file1.write(text[::-1])
    
copy_and_reverse('story.txt', 'story_copy.txt')   

def statistics(file):
    with open(file) as f:
        lines = f.readlines() 
    return {
        "lines" : len(lines),
        "words" : sum(len(line.split(" ")) for line in lines),
        "characters" : sum(len(line) for line in lines),

            }

print(statistics('story.txt'))