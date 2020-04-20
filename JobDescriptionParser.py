def char(string):
    #1 string formatting and manipulation
    string = string.lower()
    string = string.replace(". ", " ")
    string = string.replace(", ", " ")
    string = string.replace("? ", " ")
    string = string.replace("! ", " ")

    #2 dictionary creation
    wordoccurrence = {}
    for word in string.split():
        if word in wordoccurrence:
            wordoccurrence[word] +=1
        else:
            wordoccurrence[word] =1

    #3 dictionary to delete common words from created dictionary
    #delete pronouns
    #delete filler words
    wordstodelete = ["and", "to", "of", "the", "or", "is","passion","disability","."]
    for word in wordstodelete:
        if word in wordoccurrence:
            wordoccurrence.pop(word)
    #4 have to delete these words too
    CoordinatingConjunctions =["for", "and", "nor", "but", "or", "yet", "so", "of", "with", "a", "at"]
    for word in CoordinatingConjunctions:
        if word in wordoccurrence:
            wordoccurrence.pop(word)

    #5 get max key or word that appears the most
    max_key = max(wordoccurrence, key=wordoccurrence.get)
    return wordoccurrence

with open(r"C:\Users\JAndr\OneDrive\Projects\Project INeedaJob\lockheed.txt", 'r') as file:
    data = file.read().replace('\n', '')
print(char(data))

