def func1(*args, **kwargs):
    print(args)       # always first use args before kwargs
    print(kwargs)


func1(1, 2, 3, 4, 5, jack=34, chill=23, nanu=89)    

# in result we got firstly args and then i got kwargs 


