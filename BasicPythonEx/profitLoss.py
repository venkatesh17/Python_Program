
def profitloss():
    # Python Program to Calculate Profit or Loss

    actual_cost = 120 # float(input(" Please Enter the Actual Product Price: "))
    sale_amount = 150 # float(input(" Please Enter the Sales Amount: "))

    if actual_cost > sale_amount:
        amount = actual_cost - sale_amount
        print("Total Loss Amount = {0}".format(amount))
    elif sale_amount > actual_cost:
        amount = sale_amount - actual_cost
        print("Total Profit = {0}".format(amount))
    else:
        print("No Profit No Loss!!!")
