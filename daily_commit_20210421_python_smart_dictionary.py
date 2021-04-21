# Python Smart Dictionary
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# All the functions
# --------------------------------------------------------------------------------------------------------------


def read_dictionary():  # method that reads all the words from words.txt and separates english from chinese words
    with open('words.txt', 'r') as text_file:
        for line in text_file:  # reading each line
            line_split = line.split(' ')
            english_words.append(line_split[0])
            chinese_words.append(line_split[1])
            d['%s' % line_split[0]] = line_split[1]


def search_words():  # searches for english words which start with the console input value
    search_entry = raw_input("what are you searching for: ")
    print " "
    print " "
    match_count = 0

    print "Matching words: \n"
    for i in english_words:
        if i.startswith(search_entry):
            match_count += 1             # counting the matches
            print i                      # prints the matching english word
        else:
            pass

    print '\n%s matched %d words from the dictionary \n' % (search_entry, match_count)

    if match_count != 0:
        define_words()  # displays the definition
    else:
        print("thanks for using my smart dictionary!")


def search_chinese():  # searches for english words which match the input chinese words meaning
    chinese_word = raw_input("write the chinese characters you'd like to translate: ")
    for a in chinese_words:
        try:
            u = a.strip().decode('utf-8')
        except UnicodeDecodeError as e:
            print 'decode failed at', e.args[2], 'leaving', repr(a[e.args[2]:])
            u = a.strip().decode('utf-8', 'ignore')
        if chinese_word not in str(u):
            pass
        else:
            c = chinese_words.index(a)
            print str(english_words[c]) + " " + str(u)


def define_words():  # displays the definition of a selected word

    selected_word = raw_input("select a word you'd like to translate: ")
    while True:
        if selected_word not in d.keys():
            selected_word = raw_input("oops typo! select a word you'd like to translate: ")
        else:
            break

    definition = d[selected_word]
    w_type = definition.split('.')
    word_type = w_type[0]
    meaning = w_type[1:]

    print " "

    print '%s %s' % (selected_word, str(word_type)) + "."

    for i, line in enumerate(meaning):
        try:
            u = line.strip().decode('utf-8')
        except UnicodeDecodeError as e:
            print 'decode failed at', e.args[2], 'leaving', repr(line[e.args[2]:])
            u = line.strip().decode('utf-8', 'ignore')
        print u


def occurrence():
    print " "
    print "Occurrences of 26 letters of the alphabet in the dictionary: \n"

    one_big_word = ''
    for every_word in english_words:
        one_big_word += every_word.lower()

    word = one_big_word

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    hits = [
        (alphabet[i], word.count(alphabet[i]))
        for i in range(len(alphabet))

        if word.count(alphabet[i])
    ]

    for letter, frequency in hits:
        print letter.upper(), frequency

    # plotting the bar graph
    import matplotlib.pyplot as plt
    letters = []
    frequencies = []

    for letter, frequency in hits:
        letters.append(letter)
        frequencies.append(frequency)
    data = frequencies
    labels = letters
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Letters')
    plt.ylabel('Occurrences')
    plt.title('ALPHABET LETTERS OCCURRENCES')
    plt.bar(range(len(data)), data, color='black')
    plt.show()


# Searching sequence
# --------------------------------------------------------------------------------------------------------------

d = {}                    # dictionary with english words as the keys and chinese meanings as the values
english_words = []        # list of english words
chinese_words = []        # list of chinese translations
read_dictionary()         # reads all the words from words.txt
search_words()            # looks for matches

while True:               # for subsequent searches
    print " "
    asking = raw_input("would you like to continue?:  (yes/no) ")
    if asking == 'yes':
        search_words()
    else:
        print " "
        search_chinese()  # chinese to english search
        print " "
        print("thanks for using my smart dictionary!")
        break

# Bar Graph
# --------------------------------------------------------------------------------------------------------------

occurrence()              # bar graph for 26 letters in the dictionary against their occurrence
