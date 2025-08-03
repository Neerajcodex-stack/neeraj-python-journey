# STRING FORMATTING

template = "Dear {}, you awesome.take this {}$ bag"

a = "john"
a1 = 10000
b = "jack"
a2 = 1000
c = "marie"
a3 = 300


s1 = template.format(a, a1)
print(s1)

print(f"{a}) you are awesome and take this {a1}$ bag") 