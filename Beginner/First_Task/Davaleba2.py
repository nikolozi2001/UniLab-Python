var1 = 51
var2 = 51.5
var3 = "bone"
var4 = ['Nika Kachibaia', 'elem5', 'elem9', 'duplicate', 'duplicate']
var5 = ("white", "black", "blue", "red")
var6 = {
    "grass": "green",
    "roses": "red",
}
# var7 =

######### ამის ქვემოთ არაფერი შეცვალოთ ########

print(type(var1) == int)
print(type(var2) == float)
print(var1 > 50)
print(var1 <= var2)
print(var2.is_integer() == False)

print(type(var3) == str)
print(var3[1] == "o")
print(var3.endswith("e"))

print(type(var4) == list)
print(len(var4) == 5)
print(var4[2] == 'elem9')
print(var4.index('elem5') == 1)
print(var4.count('duplicate') == 2)

print(type(var5) == tuple)
print(var5[3] == "red")

print(type(var6) == dict)
print(var6.get("grass") == "green")