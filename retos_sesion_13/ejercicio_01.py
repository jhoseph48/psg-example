a = 2  
b = 1  

print("1", a)
print("2", b)

for i in range(3, 21): 
    siguiente = a + b
    print(i, siguiente)
    a = b
    b = siguiente