# Day 1 — Variables, Data Types, Operators
# Data types (int, float, str, bool, list, tuple, dict, set), type conversion, operators (arithmetic/comparison/logical), print()/input(), f-strings. Pairs with: Move Zeroes, Majority Element.

#Grocery Bill Calculator 

# Day 1 — Variables, Data Types, Operators
# Grocery Bill Calculator - 6.5/10

total = 0
eligible = False

def calculate_total(price, quantity):
    global total  # MISTAKE 5 (biggest): using global instead of returning and 
                  # letting the caller pass the value forward. Every function 
                  # below has this same issue — this is the core thing the 
                  # exercise was testing.
    total = float(price) * int(quantity)
    return total

def is_eligible_For_discount(total, quantity):  
    # MISTAKE 1 (smallest): "For" has a capital F — should be snake_case: 
    # is_eligible_for_discount
    global eligible  # MISTAKE 5 again — same global issue
    if total > 500 and quantity > 2:
        eligible = True
        return True
    else:
        eligible = False
        return False

def apply_discount(eligible):
    global total  # MISTAKE 5 again
    if eligible == True:  # MISTAKE 2 (minor): eligible is already a bool, 
                           # just write "if eligible:"
        discount = total/100 * 10
        total = total - discount
        print(total)  # MISTAKE 4 (bigger): the question explicitly said 
                       # "return final total" — printing here means this 
                       # function gives nothing back to whoever calls it. 
                       # It only "worked" because global total patched the 
                       # value in behind the scenes.

def display_receipt(name, quantity, total, eligible):
    print(f"""
            Receipt: {name} X {quantity} - Total: {total} (Discount applied = {eligible})
""")

item = input("Enter item name: ")
price = input("Enter price: ")
quantity = input("Enter quantity: ")
calculate_total(price, quantity)
is_eligible_For_discount(total, int(quantity))  
# MISTAKE 3 (minor): quantity is already converted to int inside 
# calculate_total — converting it again here is duplicate work
apply_discount(eligible)
display_receipt(item, quantity, total, eligible)