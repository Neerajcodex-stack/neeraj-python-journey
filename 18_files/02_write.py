# write to a file callled john doe.txt
# it should contain data about john doe


f = open("john Doe.txt", "w")
string = '''
John Doe is a nice guy. He lives in Nyc and he works with Python His favourite pakage is pandas i also live with him ..'''


f.write(string)

f.close 




# automatically new file was creted in list of folder and the content was automatically written there.....

# if i want to add more than  i have to use append 

# if file not found error than use ((except Filenotfound error))