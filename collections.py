thislist = ["Apple", "Banana", "Cherry"]
thisTupple = ("Apple", "Banana", "Cherry")
thisSets = {"Apple", "Banana", "Cherry"} 

print(thislist)
print(thisTupple)

print(thislist[0])
print(thisTupple[2])
#print(thisSets[2]) #set tidak berurut

for x in thisSets:
    if x=="Banana":
        print(x)

#menambahkan data pada list
thislist.append("Anggur")
print(thislist)

#list lebih direkomendasikan untuk data yang berurutan

#pada tupple
addTupple="Anggur"
thisTupple=(*thisTupple,addTupple) #*untuk menghilangkan kurung
print(thisTupple)

#pada sets
thisSets.add("Anggur")
print(thisSets)

#menghapus
thislist.remove("Banana")
print(thislist)
#clear untuk menghapus data semuanya
thislist.pop(2) #remove berdasarkan index
print(thislist)

del thislist[0]#delete berdasarkanindex juga
print(thislist)

#pada Tupple

#pada set
thisSets.remove("Banana")
print(thisSets)