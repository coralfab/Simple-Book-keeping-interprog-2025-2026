transaction = []

def record_transaction():
    while True:
        print("Recording transactions!\n")
        
        while True: # Will ask the date of the transaction
            calendar = input("Date of transaction (YYYY/MM/DD): ").strip()
            parts = calendar.split("/")
            
            if len(parts) != 3:
                print("Invalid format! Ex. 2025/01/01")
                continue
            
            if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
                print("Invalid format! Ex. 2025/01/01")
                continue

            if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
                print("Invalid format numbers only! Ex. 2025/01/01")
                continue
            break
                
        #Will ask what type of transaction was received    
        while True:
            type_money = input("What type of transaction (expense/income): ").strip().lower()
            if type_money == "expense" or type_money == "income":
                break
            else:
                print("Invalid input! expense/income only!")
        
        #Wil ask information about expense/income son
        description = input("Description about transaction: ").strip()
        
        #Will ask about amount of money received bro
        while True:
            money_input = input("Amount: ").strip()
            
            if money_input == "":
                print("Invalid input!")
                continue
            
            if not money_input.isdigit():
                print("Invalid input! Numbers only!")
                continue
            
            money = int(money_input)
            if money <= 0:
                print("Invalid input must be greater than 0!")
                continue
            break
            
        print("=====================")       
        print("Transaction recorded!")
        print(f"Date: {calendar}")
        print(f"Type: {type_money}")
        print(f"Description: {description}")
        print(f"Amount: {money}")
        print("=====================") 
        
        transaction.append([calendar, type_money, description, money])
    
        #This will if the user wants to recond another transaction
        while True:
            back = input("\nDo you want to record another transaction? (Y/N): ").strip().lower()
            if back == "y":
                break 
            if back == "n":
                return     
            else:
                print("Invalid input! Enter Y or N:")