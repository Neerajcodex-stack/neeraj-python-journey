def sum(*args):
   # args will be a tuple of all the values passsed to sum
    total = 0
    for item in args:
        total += item
    return total    
                                 # sum() takes 2 positional arguments but 3 were given
print(sum(342, 2, 7,8 ,8 ,9, 6))             # if i try to make more than 2 digit bcz i entered two 
  
# for this error (sum() takes 2 positional arguments but 3 were given) we use args

# by using this coomand i can add all number of values i want 