                                  #MODULES

# modules are something code which was written the other developer but we use in our programming to make work easy


# two types of modules in python:

# 1.... build in modules
# 2.... external modules
# https://docs.python.org/3/py-modindex.html  list of all built in module




import math
import os

import mymodule
import requests
print(math.sqrt(16))     #give square root of number
mymodule.hello() 


r = requests.get("https://www.google.com")               #request is use to open any url
print(r.text)
