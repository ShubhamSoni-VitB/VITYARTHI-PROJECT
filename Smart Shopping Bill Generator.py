#Smart Shopping Bill Generator
# Vityarthi Project

print("=" * 50)
print("\tSMART SHOPPING BILL")
print("=" * 50)

Consumer = input("Enter consumer name: ")
city = input("Enter city: ")

print("\nConsumer Name:", Consumer)
print("City:", city)

number = int(input("\nHow many items did you purchase? "))

if number <= 0:
    print("Invalid number of items.")

else:
    total = 0
    total_quantity = 0

    for i in range(number):

        print("\nEnter details for item", i + 1)


        item = input("Item name: ")
        mrp = float(input("Price: "))
        quantity = int(input("Quantity: "))

        amount = mrp * quantity

        total = total + amount
        total_quantity = total_quantity + quantity

        print("Amount for", item, "=", amount)

    # Discount calculation
        
    if total >= 5000:
            discountrate = 20
    elif total >= 3000:
            discountrate = 15
    elif total >= 1000:
            discountrate = 10
    else:
            discountrate = 0

    Discount = total * discountrate / 100
    After_Discount = total - Discount  

        # GST calculation

    gstrate = 5
    gst = After_Discount * gstrate / 100

    finalAmount = After_Discount + gst

    print("\n" + "=" * 50)
    print("\tSHOPPING BILL")
    print("=" * 50)

    print("Consumer:", Consumer)
    print("City:", city)
    print("Number of Items:", number)
    print("Total Quantity:", total_quantity)

    print("-" * 50)

    print("Total Amount:", round(total, 2))
    print("Discount Rate:", discountrate, "%")
    print("Discount Amount:", round(Discount, 2))
    print("Amount After Discount:", round(After_Discount, 2))
    print("GST:", round(gst, 2))
    print("Final Amount to be Paid:", round(finalAmount, 2))

 # Shopping Offer Eligibility
        
    if total >=1000 and Discount > 0:
        print ("\nYou are eligible for a shopping offer.")
    else:
        print("\nYou are not eligible for any shopping offer.")

    # Payment Method Selection
    
    print("\nSelect Payment Method")
    print("1. Cash")
    print("2. UPI")
    print("3. Credit Card")
    print("4. Debit Card")

    payment = input("Enter your choice: ")

    if payment == "1":
                payment_method = "Cash"
    elif payment == "2":
                payment_method = "UPI"
    elif payment == "3":
                payment_method = "Credit Card"
    elif payment == "4":
                payment_method = "Debit Card"
    else:
                payment_method = "Invalid"

    print("Payment Method:", payment_method)    

              # Membership operator  

    storename = "Smart Mart"

    if "Smart" in storename:
        print("Welcome to Smart Mart")

    # Checking Data Types

    print("\nData Types:")
    print(type(Consumer))
    print(type(number))
    print(type(total))
        
    print("\n" + "=" * 50)
    print("THANK YOU,", Consumer)
    print("PLEASE VISIT US AGAIN!")
    print("=" * 50)
