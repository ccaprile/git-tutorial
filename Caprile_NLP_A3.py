"""

PROBLEM 1.

Write a function has_most_consonants() that takes a string as input and returns
the words that have the largest number of consonants in them. For this exercise,
consonants are just letters like t and k (in fact, all letters except a, e, i, o
and u). You may use split() to get the tokens and you do not need to worry about
splitting off punctuations. The

>>> has_most_consonants('The door is closed. And many dogs barked.')
['closed.', 'barked.']
>>> has_most_consonants('')
[]


PROBLEM 2.

Write a function called is_determiner() that takes a word as input and decides
if it is a determiner.

>>> is_determiner('the')
True
>>> is_determiner('thesis')
False

Then create another function remove_determiners() that uses is_determiner() and
that eliminates all determiners in a piece of a text.

>>> remove_determiners('the dog is asleep in a basket.')
'dog is asleep in basket.'

Contrary to what I said in class, do not worry about punctuation. But do worry
about removing things like 'The'.


PROBLEM 3.

Given an embedded list such as

   [['a', 'big', 'red', 'dog'], ['chased', ['a', 'small', 'red', 'cat']]]

where the embedding can be of any depth, but where the contents of the lists are
either other lists or strings. Write a function to replace all instances of an
arbitrary word with a new word.

>>> lst = [['a', 'big', 'red', 'dog'], ['chased', ['a', 'small', 'red', 'cat']]]
>>> replace_word(lst, 'a', 'the')
[['the', 'big', 'red', 'dog'], ['chased', ['the', 'small', 'red', 'cat']]]


PROBLEM 4.

Write a function that takes a string as input and returns a dictionary of
bigrams and their frequencies. As part of this, split off end-of-sentence
punctuation markers and commas and put all words in lower case. You can reuse
part of your solution to assignment 2 here.

>>> bigrams = get_bigrams('The dog is asleep in a basket? Yes, in a basket!')
>>> sorted(bigrams.items())[:4]
[((',', 'in'), 1), (('?', 'yes'), 1), (('a', 'basket'), 2), (('asleep', 'in'), 1)]

In addition, write a similar function for trigrams.

>>> trigrams = get_trigrams('The dog is asleep in a basket? Yes, in a basket!')
>>> sorted(trigrams.items())[:3]
[((',', 'in', 'a'), 1), (('?', 'yes', ','), 1), (('a', 'basket', '!'), 1)]


PROBLEM 5 (extra credit).

Write a function that takes as input a string and a number (the number being the
n in ngrams) and returns a dictionary of ngrams and their frequencies.

>>> ngrams = get_ngrams('The dog is asleep in a basket? Yes, in a basket!', 2)
>>> sorted(ngrams.items())[:4]
[((',', 'in'), 1), (('?', 'yes'), 1), (('a', 'basket'), 2), (('asleep', 'in'), 1)]
>>> ngrams = get_ngrams('The dog is asleep in a basket? Yes, in a basket!', 3)
>>> sorted(ngrams.items())[:3]
[((',', 'in', 'a'), 1), (('?', 'yes', ','), 1), (('a', 'basket', '!'), 1)]

Makes sure that this works for any integer higher than 1, not just bigrams and
trigrams. This means you need to give a meaningful message for those cases where
ngrams would be longer than the text itself.

"""
import nltk
from nltk.probability import FreqDist
from nltk.util import bigrams


# ### Problem 1
#function that counts the number of consonants in a word.
def cons(word):
    sub = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for ch in list(word):
        v = vowels.count(ch)
        sub = sub+v
        t = len(word)-sub
    return t


#function that within a string identifies words with most consonants.
def has_most_consonants(string):
    cons_len = []
    most_con = []
    split = string.split()
    for w in split:
        cons_len.append(cons(w))
    for w in split:    
        if cons(w) == max(cons_len):
            most_con.append(w)
    print(most_con)
    
# ### Problem 2

#Functions that defines if a certain string is a determiner
def is_determiner(word):
    det = ['a', 'an', 'the', 'A', 'An', 'The']
    if word in det:
        return True
    else:
        return False
        

#function that removes all determiners off a string.
def remove_determiners(string):
    split = string.split()
    for w in split:
        if is_determiner(w) == True:
            split.remove(w)
            s = " ".join(split)
        else:
            None
    return s

# ### Problem 3

#function that replaces a string in an embedded list
def replace_word(emb_list, old, new):
    for i, sub in enumerate(emb_list):
        if isinstance(sub, str):
            if sub == old:
                emb_list[i] = new
        elif isinstance(sub, list):
            replace_word(sub, old, new)
    return(emb_list)

# ### Problem 4

#function to get bigrams and its frequency
def get_bigrams(string):
    import re
    string = re.findall(r'\w+|[^\w\s]',string)
    string = [w.lower() for w in string]
    fd = FreqDist(bigrams(string))
    return fd



from nltk.util import ngrams

#function to get trigrams
def get_trigrams(string):
    import re
    string = re.findall(r'\w+|[^\w\s]',string)
    string = [w.lower() for w in string]
    tri = ngrams(string,3)
    fd = FreqDist(tri)
    return fd

if __name__ == '__main__':

    import doctest
    doctest.testmod()

