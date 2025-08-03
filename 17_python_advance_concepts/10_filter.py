# def is_greater_than_9(x):
#     if x<9:
#         return True                                # TWO METHODS 
#     else:
#         return False
    
# a = [1, 3, 5, 234, 34, 34, 32, 10, 8.5, 7.12]              


# new = list(filter(is_greater_than_9, a))
# print(new)







# def is_greater_than_9(x):
#     if x<9:                             # ISTEAD OF USINGB THIS CODE IN IT WE CAN ALSO USED LAMBDA CODE FOR SIMPLE
#         return True
#     else:
#         return False
    
a = [1, 3, 5, 234, 34, 34, 32, 10, 8.5, 7.12]    


new = list(filter(lambda x: x>9 , a))               #   <----------
print(new)