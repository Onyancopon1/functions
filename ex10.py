#Function to print longest word in given list


def longest_word(word_list):
    longest=""
    for word in word_list:
        if len(word)>len(longest):
            longest=[word]
        elif len(word)==len(longest):
            longest.append(word)
    return longest


#Main routine
word=[]
word_=""
while word_!="1":
    word_=input("add word to list(or 1 to end):")
    word.append(word_)

print(f"the longest word in the list {word} is {longest_word(word)}")
