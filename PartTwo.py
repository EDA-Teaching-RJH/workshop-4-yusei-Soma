price=75
total_inserted=0
valid = [5, 10, 20, 50]

while total_inserted<price:
        coin=int(input("Please insert a coin(5p, 10p, 20p, 50p):"))

        if coin in valid:
            total_inserted += coin
        else:
            print("Invaild coin. Please insert 5p, 10p, 20p, 50p.")

change= total_inserted - price
if change>0:
        print(f"Here is your coffee and your change:{change}p.")
else:
        print("No change needed. Here is your coffee!")