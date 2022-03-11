#function to print longest word in given list


def longest_word(word_list):
    longest=""
    for word in word_list:
        if len(word)>len(longest):
            longest=word
    return longest


#main routine
word=[]
word_=""
while word_!="1":
    word_=input("add word to list(or 1 to end):")
    words.append(word_)

print(f"the longest word in the list {words} is {longest_word(words)}")
