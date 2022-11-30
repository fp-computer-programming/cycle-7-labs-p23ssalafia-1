"""
# Author: Sean Salafia  11.9.22

#user inputs unique words
a = input("Input a unique word: ")
b = input("Input a unique word: ")
c = input("Input a unique word: ")
d = input("Input a unique word: ")
e = input("Input a unique word: ")

#convert those inputs into a list
x = [a, b, c, d, e]

len_a = len(a)
len_b = len(b)
len_c = len(c)
len_d = len(d)
len_e = len(e)

#create a new variable and list the indexes 
y = [len_a, len_b, len_c, len_d, len_e]
print (y)
"""
def word_length_lister (a, b, c, d, e):
    a = len(a)
    b = len(b)
    c = len(c)
    d = len(d)
    e = len(e)
    y = [a, b, c, d, e]
    return y

print (word_length_lister("one", "twoo", "three", "fourrr", "fiveeee"))
    


