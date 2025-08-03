
                                    # FIBONACCI SEQUANCE

# a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. So, the sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, and so on. 


# 0 1  1  2  3  5  8  13
# 0 1  2  3  4  5  6 . . . . . . .

# fib(0) = 0
# fib(1) = 1
# fib(2) = fib(0) + fib(1)
# fib(3) = fib(1) + fib(2)
# fib(4) = fib(2) + fib(3) 



def fib(n):

# Base case of recursion 

    if(n==0 or n==1):
        return(n)
    
    return fib(n-2) + fib(n-1)

print(fib(6))      #hence prove we knoe fib 6 = 8


# long manually method of it

print(fib(6))

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 +  0 + 1  + fib(0) + fib(1) + fib(2) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 +  0 + 1 + 0 + 1 + fib(0) + fib(1) + 1
0 + 1 + 1 + 0 + 1 + 1 +  0 + 1  +0 + 1 + 0 + 1 + 1        #too much long to calculate (ans = 8)


