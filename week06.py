def word_count(text):
    #splits the text into a string list divided by its spaces
    words = text.split(' ')
    #counts length of list/words
    wordCount = len(words)
    return wordCount

def find_longest_word(text):
    words = text.split(' ')
    bigWord = ''
    #checks the list for a longer word/compares it with the longest
    for i in words:
        if len(bigWord) < len(i):
            bigWord = i
    return bigWord

def count_substring(text, substring):
    counter = 0
    words = text.split(' ')
    #any time the word is found, counter goes up by 1
    for i in words:
        if substring == i:
            counter += 1
    return counter

def extract_unique_words(text):
    words = text.split(' ')
    #this was meant to make a new list of words that-
    #-would not include repeated words
    unique = ['']
    for i in words:
        for u in unique:
            if i != u:
                unique.append(i)
    return unique
def main():
    print('Welcome to the Text Processing Program!\n')
    userText = input('Enter a text: ')
    print(f'\nOriginal Text:\n{userText}\n')
    userOption = 0
    while userOption != 5:
        print('''Text Analysis Options:
1. Word Count
2. Longest Word
3. Count of Substring
4. Unique Words
5. Exit''')
        userOption = int(input('Enter the number of the analysis option (1-5): '))
        if userOption == 1:
            print(f'\nWord count: {word_count(userText)}\n')
        elif userOption == 2:
            print(f'\nLongest word: {find_longest_word(userText)}\n')
        elif userOption == 3:
            theSub = input('\nEnter a substring to count: ')
            countin = count_substring(userText, theSub)
            print(f"Count of substring '{theSub}': {countin}\n")
        elif userOption == 4:
            print(f'\nUnique words: {extract_unique_words(userText)}\n')
        elif userOption == 5:
            continue
        else:
            print('\nInvalid number. Please try again.\n')
    print('\nThank you for using the Text Processing Program!')
        
if __name__ == "__main__":
    main()
