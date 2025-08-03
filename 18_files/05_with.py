# f = open("neeraj.txt", "r")

# content = f.read()
# print(content)
# f.close()


# if i doent want to use command f.close i can also use------->>>


with open("neeraj.txt","r") as f:     # contex manager 
    content = f.read()
    print(content)



    # no need to f.close() because file is already closed by default when using with syntax
    # i can use with command in large python code its very important 