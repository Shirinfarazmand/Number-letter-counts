import inflect
x= 0
for i in range(1,1001):
    p = inflect.engine()
    n = p.number_to_words(i)
    n = n.replace(" ", "")
    n = n.replace("-","")
    x += len(n)
    

print(x)


