"""keep track of ticket sales at a cinema
"""


#this function runs the main program and coordinates calls to other functions
def main_routine():
    adult_tickets=0
    students_tickets=0
    child_tickets=0
    gift_tickets=0
    total_sales=0
    tickets_sold=0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted !="N":
        ticket=sell_ticket()

        #get the number of tickets wanted in th category chosen
        num_tickets=int(input("How many of these ticket do you want : "))
        confirm=input(f"confirm purchase of {num_tickets} type {ticket}"
                      f"ticket(s)? (Y/N):").upper()
        if confirm=="Y":  #Giving user the option to cancel the sale
            price =num_tickets *float(get_price(ticket))
            total_sales+=price
            tickets_sold+=num_tickets
            if ticket == "A":
                adult_tickets +=num_tickets
            elif ticket== "S":
                students_tickets +=num_tickets
            elif ticket== "C":
                child_tickets +=num_tickets
            else:
                gift_tickets +=num_tickets

                ticket_wanted=input("nDo you want to sell"
                                    "another tickets?(Y/N)").upper()


   print(f"The total tickets sold today was {ticket_sold}\n"
         f"this was made up of:\n"
         f"\t{adult_tickets}for adult: and \n"
         f"\t{student_tickets}for student: and \n"
         f"\t{child_tickets}for child: and \n
         f"\t{gift_tickets}for adult: and \n" )
   print(f"sales for the day came to ${total_sales:2f}")
   print("====================================================================")

#Get the category of ticket the purchaser wants
def sell_tickets():
   ticket_type_=input("what kind of tickets do you want:\n"
                      "\tA for adult,or \n"
                      "\tS for students,or\n"
                      "\tC for child,or\n"
                      "\tG for gift voucher\n"
                      ">> ").upper() #uppercase to minimise input errors
   return ticket_type_


#Get the price for each ticket i category of ticket chosen
def get_price(type_):
    prices=[["A",12.5],["S",9],["C",7],["G",0]]
    for price in prices:
        if price[0]==type_:
            return price[1]


#main routine
print("********************* fanfare movie  - ticketing system ****************\n)
main_routine()








while
int(input("do you want to sell another ticket "))
