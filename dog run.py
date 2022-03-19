#separate functions for each menu item
def drop_off():
    dog_name=input("Enter the name of the dog: ")
    roll.append(dog_name)


def pick_up():
    dog_name=input("enter the name of dog you want to pick up: ")
    if dog_name in roll:
        roll.remove(dog_name)
        print(f"{dog_name}has been removed from the roll")
    else:
        print("Sorry, we have no dog by that name")


def calc_cost(number):
    rate=22.50
    days=int(input("how many days to charge for: "))
    cost=number*days*rate
    print(f"the cost for {number}of dogs for {days} days is ${cost}")


def print_roll():
    print("dogs currently staying with DogsRus: ")
    for dog in roll:
        print(f"\t{dog}")
    print()


def end_program():
    print("Good bye ")


#main routine
roll=[]

print(
    "-------------------------------------------------------------------------------------------")
print("welcome to DogsRus dog sitting service")
print("what would you like to do? choose one of the item below")
print(
    "-------------------------------------------------------------------------------------------")

choice=0
while choice !=5:
    print("what do you want to do? :")
    print("------------------------")
    print("1 drop off a dog ")
    print("2 pick up a dog")
    print("3 calculate cost")
    print("4 print dog roll")
    print("5 exit the system")
    print()
    print("=====================================================================================")

    choice=int(input("Enter your choice(number between 1 to 5):"))
    if choice == 1:
        drop_off()

    elif choice == 2:
        pick_up()

    elif choice ==3:
        calc_cost(len(roll))

    elif choice == 4:
        print_roll()

    elif choice ==5:
        end_program()

    else: #in the event of any integer not in the required range
        print("Must be an integer between 1 and 5")






