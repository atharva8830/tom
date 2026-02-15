name = "atharva"

i = 0 
j = len(name) -1 

while (i<j):
    temp = name[i]
    name[i] = name[j]
    name[j] = temp 
    i+=1 
    j-=1

print (name)