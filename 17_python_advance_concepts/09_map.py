numbers = [1, 2, 3, 4, 5, 6]


def square(x):
    return x*x            # command can use for the square of all the digit in it     we can also use lambda function instead of this def square code we can just write list(filter(lambda x: x*x, numbers)) in the place of sqaure below


new = list(map(square, numbers))
print(new)