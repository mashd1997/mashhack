def sum_array(array):

    '''Return sum of all items in array'''

    if type(array) == int:
        return array

    sum = 0
    for i in array:
        if type(i) == list:
            sum = sum+sum_array(i)
        else:
            sum = sum+i
    return sum

#######next

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

######next

def factorial(n):

    '''Return n!'''

    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

#######next

def reverse(word):
    '''Return word in reverse'''
    '''input a string into function i.e input must be in '', e.g 'word' '''

    reversal = word[::-1]
    return reversal

#####done
