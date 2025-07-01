#Shopping system

customer=[]
rashan_list=[]
uid=0
Total=0
count=0
while True:
    entry1= int(input("\n\n......Wellcome to Our Store.....\n"
                    "1- To buy.\n" \
                    "0- To Exit.\n"
                    ": "))

    if entry1 ==1:
        name= input("Enter Your Name: ")
        uid= int(input("Enter customer Id here: "))
        customer.append((name,uid))


        while True:
            entry2= int(input("1- Visit Store.\n" \
            "2- Your Cart.\n" \
            "0 Exit.\n"
            ": "))
            if entry2==0:
                break
            elif entry2== 1:
                exit=1
                while exit!=0:
                    exit= int(input("1- Buy Products.\n"
                    "0- Exit.\n "))
                    entry=0
                    price=0
                    amount=0
                    if exit==1:
                        list= int(input("1- Eggs....1 Dozen25..300 RS\n" \
                        "2. Meat....1 Kg..600 Rs\n" \
                        "3. Cooking Oil....1 Kg..450 Rs\n" \
                        "4. Bread....1 pack..100 Rs\n" \
                        "5. Salt....1 Kg..50 Rs\n" \
                        "6. Juices....1 pack..150 Rs\n" \
                        "7. Butter....1Kg..200Rs\n" \
                        ": "))
                        amount= int(input("How Much: "))
                        if list==1:
                            entry="Eggs"
                            price=amount*300
                        elif list==2:
                            entry="Meat"
                            price=amount*600
                        elif list==3:
                            entry="Cooking Oil"
                            price=amount*450
                        elif list==4:
                            entry="Bread"
                            price=amount*100
                        elif list==5:
                            entry="Salt"
                            price=amount*50
                        elif list==6:
                            entry="Juices"
                            price=amount*150
                        elif list==7:
                            entry="Butter"
                            price=amount*200

                    
                        rashan_list.append((entry,price,amount))
                        Total= Total+price
                        count+1
                            
                        
                    elif exit== 0:
                        break              

            elif entry2==2:
                while True:
                    entry3=0
                    print("\n\n1-Your Cart")
                    for letter in rashan_list:
                        if letter == 0:
                            print("There is nothing in your Report")
                        print(f"Products:{letter} ")
                    print(f"Your Total Shopping Amount is: {Total}")
                    entry3=int(input("\n\n1- Remove products\n" \
                    "2- Checkout Products.\n"
                    "0- Exit."))
                    if entry3==1:
                        
                        delete= int(input("Enter entry number to Remove: "))
                        Total=Total-rashan_list[delete-1][1]
                        del rashan_list[delete-1]
                        
                    elif entry3==2:
                        print("\n\n")
                        print("Total Amount: ",Total)
                        credit=int(input("Enter Your Credit Card: "))
                        print(f"{Total} Amount has been deducted form your Credit No: {credit}\n"
                            "Thanks for Shopping")
                        length= len(rashan_list)
                        Total=0
                        rashan_list.clear()
                            
                    elif entry3==0:
                        break
                    
            
    elif entry1 ==0:
        break
