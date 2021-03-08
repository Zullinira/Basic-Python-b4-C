for i in range(3):
    for j in range (3):
        if i==0 and j==2 :
            continue
        print ("x", end=" ")
    print()

lisdata = [[1,2],[3,4]]
for i in range(2):
    for j in range(3):
        print("{}  {}".format(i,j), end="")
    print()

for i in lisdata:
    for j in i:
        print(j*5)