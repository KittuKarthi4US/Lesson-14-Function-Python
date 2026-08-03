def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh lemonade, made just for you.")

greet_customer()

price_per_cup = float(input('Enter the price in dollars :'))
cups_sold = int(input('Enter the number of cups sold :'))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total cost : ", rounded_total)

amount_paid = float(input('Please enter the paid amount :'))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups >=5:
        return "Wow. That's a big order. Thank you for your support"
    else:
        return 'Thanke for coming to this lemonade stall. We hope to see you soon!'

thank_you = thank_you_message(cups_sold)

print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("Total Cost:", rounded_total)
print("Amount Paid:", amount_paid)
print("Change Due:", rounded_change)
print(thank_you)
print("===================================")