


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]
#         [3, 3, 4, 5, 6, 7]
#         [6, 4, 5, 6, 7] 
#         [10, 5, 6, 7]        
#         [ 15, 6, 7]  
#         [21, 7]
#         [28]         this how it actually calculated 
           

def sum(a, b):
    return a + b


c = reduce(sum, numbers)
print(c)