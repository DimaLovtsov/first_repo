#get access

classes = {
 'A':27,
 'B':24,
 'C':29
}
print("There is", classes[('B')], "people in that class" )

#add items

classes["D"] = 32
print(classes)

#del

classes = {
 'A':27,
 'B':24,
 'C':29
}

del classes['C']
print(classes)

#change items
classes['B'] = 33

print(classes)

for classe in classes:
    print(classes[classe])