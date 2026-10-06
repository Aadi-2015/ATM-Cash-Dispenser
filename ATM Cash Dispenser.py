# ATM Cash Dispenser
print("=======ATM CASH DISPENSER=======")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customer_served = 0
total_dispensed = 0

serving = True
while serving:
    name = input("Enter Customer Name: ")
    amount = int(input(f"Hello {name}, Enter the amount of withdrawl: "))
    if amount <= 0:
        print("Invalid input, please enter a positive number.")
        continue
    print(f"\n Dispensing {amount}  units for {name}:")
    remaining = amount
    idx = 1
    
    while idx <=6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        
        if count > 0:
            print(f"  {count} x {value} - unit note(s) = {count * value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value  == 5: total_5 += count
            else: total_1 += count
        idx += 1 
        customer_served += 1
        total_dispensed += amount   
        print(f"Transaction Complete {name}!")
        again = input("New customer?(yes/no): ").strip().lower()
        if again != "yes":
            serving = False
print("\n ===DAILY DENOMIMATION REPORT===")
for slot in range(1,7):
# per loop    
          if slot == 1: value , total = 100 , total_100 
          elif slot == 2: value , total = 50 , total_50
          elif slot == 3: value , total =  20 , total_20
          elif slot == 4: value , total = 10 , total_10
          elif slot == 5: value , total = 5 , total_5
          else: value , total = 1 , total_1
          if total > 0:
              print(f"  {value} - unit note(s) dispended {total} ",end = "")
              for note in range(total):
                  print("=",end = "")
          print()        

print(f"Customer served   : {customer_served}")
print(f"Total Dispensed   : {total_dispensed} units.")
print("ATM  session closed , Goodbye!")          