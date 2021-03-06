
fruits  =["apple", "banana", "cherry"] #tanda [] untuk list
for x in fruits:
    print (x)


x = range (6) #berarti data 0-5
for n in x:
    print (n)

print ("------------------------------------------------------")

#for dengan range
x= range (3,6,2)
for n in x:
    print (n)

print("=================================")

#memakai continue
nilai = [13, 50, 55, 66, 77,23]
for i in nilai:
    if i<=50:
        continue
    print ("Nilai {} - Lulus".format(i))