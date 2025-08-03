s = {34, 23, 1, 3, 22}

s.add(32)
s.add(90)
s.add(9090)

s.remove(34)
s.remove(1)    # if i remove a number from the set which was not actually not present in it i may cause an error but if i want to avoid error i can use (discard) option discard option help ijn the remove the word which was present if it was not present it runs without an error ## koi error nhi aayega ager nahi hua toh wo number ya word agr hua to hta  dega ye.....

s.discard(123432)    # no error 
s.discard(21334)
print(s)

