def count_letters(text) : #defining a function to determine the no of letters encountered in a given text
    count = {}
    for letter in text.lower() :
        if (letter not in count) : 
            count[letter] = 0
        count[letter] += 1
    return count

def print_dict(dictio):
    for key,value in dictio.items():
        print(key , '--' , value)
text = 'Pranav Phanindra Sai'
print_dict(count_letters(text))
print(count_letters(text))
