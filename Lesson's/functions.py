# def fn1(name, age, university):
#     print(name)
#     print(f"Age: {age}")
#     print(f"University: {university}")

# fn1("Nika Kachibaia", 21, "Iliauni")

#args

# def main(*args):
#     # print(args[0])
#     for i in args:
#         print(i**2)

# main(1,2,3,4,5)

#kvargs

# def main (*args, **kvargs):
#     print(args, kvargs)


# main(1,2,3,4, one=1, two=2)

#scope

a = 9

def main():
    a = 8
    print(a)



main()
print(a)