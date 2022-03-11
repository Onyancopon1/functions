#calculate overdue fines for books at a libraly
def calc_fines(days_overdue):
    base_charge=.5
    daily_charge=.8
    max_charge=30
    gross_charge=base_charge+(days_overdue * daily_charge)
    if gross_charge > max_charge:
        fine=max_charge
    else:
        fine=gross_charge
    return fine


#main routine
days_overdue_=int(input("enter days overdue:"))
print(f"for{days_overdue_}the fine is ${calc_fines(days_overdue_):.2f} ")

