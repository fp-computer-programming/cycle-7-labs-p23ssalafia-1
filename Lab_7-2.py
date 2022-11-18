#Author: SJS 11/18/22

#Create function and define parameters
def find_sum(num1,num2):
    '''Finds the sum of the two numbers that were input'''
    sum_of_numbers = num1 + num2
    return(sum_of_numbers)

#separate statment that finds the sum of input numbers by running the find_sum function and substituting 20 and 40
input_numbers = find_sum (20, 40)
#prints the sum
print (input_numbers)
