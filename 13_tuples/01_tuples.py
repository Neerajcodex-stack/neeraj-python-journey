
# tuples are ordered but immutable collections (cannot be change after creation)


a = (3, 2, 22, 13)                            


# #Yaha pe parentheses () use hua hai — aur Python me
# [] → List
# () → Tuple

# Toh jese hi a = (...) likha, Python samajh gaya: ye tuple hai, jo immutable hota hai (matlab change nahi ho sakta).



print(a)
print(a[0])
         
a[3] = 32     #error TypeError: 'tuple' object does not support item assignment
        
b = (5,)          # agr muje single elemnt ko tuple elemnt bnna hai toh muje ()ke andr , bhi lagana parega kyuki ()senetece likne ke liye bbhi use hota hau that why we have to use (7')= tuple
                                                                         # (7)= not tuple







# use tuples when we do not want to change our collection accidently





