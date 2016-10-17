lista=[]
for a in range(0, 101):
    lista.append(True)

n = 1
for i in range(0, 101):
    
    for x in range(0, 101, n):
        if lista[x] == True:
            lista[x] = False
        else:
            lista[x] = True
        
    n = n + 1

for i in range(1, 101):
    if lista[i] == False:
        print(i)
