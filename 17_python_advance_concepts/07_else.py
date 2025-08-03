try:
     a = 342/10                        #agr isko 342/0 krdu toh ye bolega division by 0 nhi toh hey i am good

except Exception as e :
    print(e)



# gets executed when there was no error in the try block        


else:
    print("Hey i am good")