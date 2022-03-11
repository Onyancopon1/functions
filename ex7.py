"""Function to print name a given number of times
"""


def print_name(name,number):
    for person in range(0,number):
        print(name)



#main routine
name_= input("enter name to print: ")
number_= int(input("time to print: "))
print_name(name_, number_)

