#Function for lab 6-5
# Author: Sean Salafia  11.9.22

def num_sort(a,b,c,d,e,f,g,h):
    '''sort nums into a list and return the maximum and minimum values.'''
    num_list = [a,b,c,d,e,f,g,h]
    num_list.sort()
    min = num_list[0]
    max = num_list[-1]
    return min, max

#Test Case
print (num_sort(1,6,3,7,3,7,1,8)) 

print (num_sort(3,77,5,6,2,1,8,6))

print (num_sort(-3,-77,-5,6,2,1,-8,6))

print (num_sort(999999,-9,-9,6,2,9,-8,-99999)) 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Function for lab 6-6


def word_lenghth_finder (w1,w2,w3,w4,w5):
    ''''''
    words = [w1,w2,w3,w4,w5]
    length_of_words = [len(w1),len(w2),len(w3),len(w4),len(w5)]
    return length_of_words
#Test Case
print(word_lenghth_finder("Bears","Beets","Battlestar","Galactica","Dwight"))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Function for lab 6-7

def number_doubler (num1,num2,num3):
    '''Take input numbers and double them'''
    double_number = [int(num1) * 2 ,int(num2) * 2 ,int(num3) * 2]
    return double_number
#Test Case
print(number_doubler(33,99,-30))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Function for lab

def even_odd_mixed_detector (num1,num2,num3):
    """Conditionals determine if all numbers are even, odd, or if there is a mix"""
    numbers = [int(num1),int(num2),int(num3)]
    if (numbers[0]%2 == 0 and numbers[1]%2 == 0 and numbers[2]%2 == 0):
       return ("Even")
    elif (numbers[0]%2 == 1 and numbers[1]%2 == 1 and numbers[2]%2 == 1):
        return ("Odd")
    else:
        return ("Mixed")
#Test Cases
print (even_odd_mixed_detector(5,7,9))
print (even_odd_mixed_detector(2,4,6))
print (even_odd_mixed_detector(3,4,5))
