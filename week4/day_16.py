'''
https://github.com/darkprinx/break-the-ice-with-python/tree/master/Status
'''
'''
60
Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5
Then, the output of the program should be:

500
'''

def my_func(n):
    if n == 0:
        return 0
    else:
        return my_func(n-1)+100






'''
61 + 62

generate next in the fibonacci seq
'''

# Recursive function much better!


def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
    
    



def next_fib(p):  # Much slower!!
    n = 1
    while fib(n) <= p:
        n += 1
    else:
        print(f'This one is next!: {fib(n)}') 

'''
63

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

10
Then, the output of the program should be:

0, 2,4,6,8,10
'''



def evens(max):
    upper = int((max+2)/2)
    yield from [str(i*2) for i in range(upper)]





def div5and7(n):
    '''
    64
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n /
    in comma separated form while n is input by console.

    Example: If the following n is given as input to the program:

    100
    Then, the output of the program should be:

    0,35,70
    In case of input data being supplied to the question, it should be assumed to be a console input.
    '''
    li = []
    for i in range(0, n+1):
        if i % 35 == 0:  # i % 7 == 0 and i % 5 == 0:
            li.append(i)
    yield from li


if __name__ == "__main__":
    print(f'{my_func(0)},  {my_func(1)}, {my_func(5)}')
    print(fib(7))
    next_fib(125)
    print(",".join(evens(10)))
    print(list(div5and7(100)))