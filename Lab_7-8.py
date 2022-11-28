#Author Sean Salafia 11/28/22

def add_to_7 (num):
    '''Add a number to the value 7'''
    new_sum = num + 7
    return new_sum

def multiply_by_7 (number):
    '''Multiply 7 by an input value'''
    new_product = 7 * (number)
    return new_product

def product_of_all (new_sum,new_product):
    '''Find the product of the sum statement multiplied by the product statement'''
    final_product = new_sum * new_product
    return final_product

#Test Cases
if (product_of_all(add_to_7(5), multiply_by_7(3))) == 252:
    print ('Test Case 1 is True')
else:
    print ('Test Case 1 is False')


if (product_of_all(add_to_7(7), multiply_by_7(5))) == 490:
    print ('Test Case 2 is True')
else:
    print ('Test Case 2 is False')


if (product_of_all(add_to_7(1), multiply_by_7(30))) == 1680:
    print ('Test Case 3 is True')
else:
    print ('Test Case 3 is False')


if (product_of_all(add_to_7(40), multiply_by_7(90))) == 29610:
    print ('Test Case 4 is True')
else:
    print ('Test Case 4 is False')
