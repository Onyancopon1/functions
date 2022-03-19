# this is main manu function
def main():
    # set up variables
    num_attending_fs = 0
    num_attending_ak = 0
    total_age_fs = 0
    total_age_ak = 0
    choice = 0

    while choice != 3:
        print("what do you want to do?")
        print()
        print("1 enter data")
        print("2 Display current statistics")
        print("3 exit the system")
        print()
        print("=" * 80)
        try:  # this is to prevent errors - integer only
            choice = check_number("Enter your choice "
                                  "(number between 1 to 3): ")
            if choice == 1:
                data = enter_data()

                # user chooses fun in the sun
                if data[0] == "F":
                    total_age_fs += int(data[1])
                    num_attending_fs += 1

                # user choose Active kids
                elif choice == 2:
                    statistics(num_attending_fs, num_attending_ak, total_age_fs,
                               total_age_ak)

            elif choice == 3:
                # when user has finished entering data - calculates and shows
                # averages before exiting.
                confirm_exit = int(input("Are you sure you want to exit? All the data"
                                         "will be lost!!\nEnter 'Y' to confirm or"
                                         "any other key to go back: ")).upper()
                if confirm_exit == "Y":
                    statistics(num_attending_fs, num_attending_ak, total_age_fs,
                               total_age_ak)
                    end_program()
                    break
                else:
                    choice = 0

            else:  # in the event of any integer not in the required range
                print("Must be an integer between 1 to 3 ")
        except ValueError:
            print("Not a valid choice")


def check_number(text):
    valid = 'false'
    while not valid:
        try:
            number = int(input(text))
            if ininstance(number, int):
                valid = True
                return number
        except ValueError:
            print("Woops...")


def enter_data():
    program = input("\nwhich programme did the child attend?\n"
                    "'F' for fun in the sun; or\n"
                    "'A' for active kids;or\n"
                    "any other key to go back:").upper()  # upper case
    if program == "A" or program == "F":
        question = "\nInput the child's age (in year)\n" \
                   "Note: age must be between 5 to 15: "
        age = check_number(question)

        # ensure age can only be between 5 to 15
        # (same as 'while age <5 or age >15:')
        while not 5 <= age <= 15:
            age = check_number(question)
        return program, age
    else:
        print()
        return "", 0


def statistic(num_attending_fs, num_attending_ak, total_age_fs, total_age_ak):
    # Need to protect against devide by zero error- if no data has been
    # entered for fun is the sun
    if num_attending_fs == 0:
        print("\nThe average for the :'fun in the sun' programme could not be"
              "calculated because no data has been entered for this programme")
    else:
        average_age_fs = total_age_fs / num_attending_fs
        print("f\nthe total number registered for 'fun in the sun' "
              f"programme is {round(average_age_fs)}")
        print(f"the total number registered for 'fun in the sun' is"
              f"{num_attending_fs}")
        # need to protect against devide by zero error  - if no data has been
        # entered for active kids
        if num_attending_ak == 0:
            print(f"\nThe average age of children in the 'active kids' programme"
                  f"is {round(average_age_ak)}")
            print(f"the total number registered for 'Active kids' is"
                  f"{num_attending_ak}")


def end_program():
    print("\Good bye")


# main menu routine
main()
