"""Count words in file."""

def count_words(txt_file):

    poem = open(txt_file)

    dictionary_of_poem = {}

    for line in poem:
        words = line.split()
        #print(words)
        
        for word in words:
            dictionary_of_poem[word] = dictionary_of_poem.get(word, 0) + 1
            
    for key, value in dictionary_of_poem.items():
        print(key, value)

count_words("test.txt")
