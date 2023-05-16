#პირველის პასუხი

def showHigh(number1, number2, number3):
    max_num = max(number1, number2, number3)
    print("Highest number is:", max_num)
  

showHigh(4, 21, 17)

#მეორეს პასუხი

def main(*args):
    total_sum = sum(args)
    print("The total sum is:", total_sum)

main(1,2,3,4,5)

#მესამეს პასუხი

def show_names(names):
    for name in names:
        print(name)

name_list = ["Nika", "Luka", "Ana", "Elene"]
show_names(name_list)