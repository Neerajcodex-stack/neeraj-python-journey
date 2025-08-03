# append to a file callled john doe.txt
# it should contain data about john doe

f = open("John Doe.txt", "a")

string = '''
John Doe initially lived in Phoenix, Arizona. He is a very nice guy '''

f.write(string)
f.close