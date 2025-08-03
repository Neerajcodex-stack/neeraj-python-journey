def marks(**kwargs):
    for item in  kwargs.keys():
      # kwargs is a dictionary with all the key value pairs which were passed to marks

        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, neeraj=99, jack=34, marie=90)        




# result 
'''The marks of shubham is 34
The marks of neeraj is 99
The marks of jack is 34
The marks of marie is 90'''