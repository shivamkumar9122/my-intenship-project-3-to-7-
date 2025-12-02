
mylist  =["apple","samsung","huawei","vivo","nokia","poco"]

type(mylist)

mylist.append("red magic")

print(mylist)

mylist.insert(1,"asus")



print(mylist)

mylist.count("apple")

mylist.append("asus")

mylist.count("asus")

mylist.sort()

print(mylist)

mylist.pop(3)

print(mylist)

mylist.remove("red magic")

print(mylist)

mylist.reverse()

print(mylist)

mytuple=("1","2","3","4","5","6","1","5")

type(mytuple)

mytuple.count("1")

set = {9,7,8,6,4,0,}

print(type(set))

print(set)

set1 = {1,3}

set2 = {4,5}

print(set1 | set2)

student = {"name":"Harshit","age":21}
student.values()

print(type(student))

gar={"harshit":"ankit"}

print(type(gar))

text = "HelloVgu"

print(text[0:5])

print(text.find("Vgu"))

print(text.replace("Vgu", "Harshit"))

text1 = "harish harshit"
print(text1.split())

print(" ".join(text1))



file= open ("mydoc.txt","w")

file.write("Hello I am written from python code")

file.close()

file= open ("mydoc.txt","r")
print(file.read())
file.close()
