#python return square brackets
name = ["radhika","anand","goswami"]
print(name)

#if i want to access one of the elements from the array
#let's do it with the first
print(name[0])
#every first is a [0]

#now if we accessed something negative
print(name[-1])
#it will give the last element 

#trying out by writing my full name as Radhika Anand Goswami
print("My full name is",name[0].title(),name[1].title(),name[2].title())

#to print a variable
f_name = f"{name[0]}"
print(f_name.title())

#modifying string so my name will print as ['rads', 'anand', 'goswami']
name[0] = 'rads'
print(name)

#deleting items from the list so it will read radhika goswami
del name[1]
print(name)

#adding the name to the list
name.insert(1,'anand')
print(name)

#appending a name to the last
name.append('goswami')
print(name)


