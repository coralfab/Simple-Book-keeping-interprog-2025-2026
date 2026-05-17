import records as rec

def view_transaction():
    while True:
        print("\n----- Transaction History ----- ")
        if not rec.transaction:
            print("No transaction made yet")
            input("\nEnter any input to go back to menu: ")
            break
        else:
            number = 1
            for index in rec.transaction:
                print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                number += 1

        view = input("Select a record number to view/(Type exit to go back): ").strip().lower()

        if view.lower() == "exit":
            break

        if view == "":
            print("Invalid input!")
            continue
        
        if not view.isdigit():
                print("Invalid input! Numbers only!")
                continue
            
        view = int(view)
        if view < 1 or view > len(rec.transaction):
            print("Invalid number! Record number doesn't exist yet!")
            continue

        record = rec.transaction[view - 1]
        print("--- Record Details ---")
        print(f"Date: {record[0]}")
        print(f"Type: {record[1]}")
        print(f"Description: {record[2]}")
        print(f"Amount: {record[3]}")
        print("----------------------")


        while True:
            back = input("Do you want to view again? Y/N: ").strip().lower()
            if back == "y":
                break  
            elif back == "n":
                return
            else:
                print("Invalid input Y/N only!")  
        
    
def remove_transaction():
    while True:
            print("\n----- Transaction History-----  ")

            if not rec.transaction:
                print("      No transaction made yet")
                input("\nEnter any input to go back to menu: ")
                break
                

            number = 1
            for index in rec.transaction:
                print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                number += 1

            remove = input("Select a record number to delete/(Type exit to go back): ").strip()

            if remove.lower == "exit":
                break

            if not remove.isdigit():
                print("Invalid input! Numbers only!")
                continue

            remove = int(remove)

            if remove < 1 or remove > len(rec.transaction):
                print("Invalid number! Record number doesn't exist yet!")
                continue

            removed_record = rec.transaction.pop(remove - 1)

            print("\n =======================") 
            print("Removed successfully")
            print(f"Date: {removed_record[0]}")
            print(f"Type: {removed_record[1]}")
            print(f"Description: {removed_record[2]}")
            print(f"Amount: {removed_record[3]}")
            print(" ======================= ") 
            

            if not rec.transaction:
                print("\n----- Updated Transaction History ----- ")
                print("        No transaction made yet")
                input("\n Enter any input to go back to menu: ")
                break
            else:
                print("\n----- Updated Transaction History ----- ")
                number = 1
                for index in rec.transaction:
                    print(f"{number} - {index[0]} - {index[1]} - {index[2]} - {index[3]}")
                    number += 1
            while True:
                again = input("\nDo you want to remove another record? (Y/N): ").strip().lower()
                if again == "y":
                    break  
                elif again == "n":
                    return
                else:
                    print("Invalid input Y/N only!")
                    continue  
                    
                   
while True:
    print("\n====== SIMPLE BOOKKEEPING PROGRAM ======")
    print("   1. Record Transaction")
    print("   2. View transaction history")
    print("   3. Remove transaction record")
    print("   4. Exit program")
    
    #Will ask the user to choose between the choices
    choice = (input("Choose a number (1 - 4): ")).strip()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Invalid input select a number from the choices!")
        continue
    choice = int(choice)
    
    if choice == 1:
        rec.record_transaction()
 
        
    elif choice == 2:
        view_transaction()
        
                   
    elif choice == 3:
        remove_transaction()
                                        
                
    elif choice == 4:
        if not rec.transaction:
            print("Exiting program...")
            break
        else:
            while True:
                confirm = input("Are you sure you want to exit? Your saved transaction records will be gone! (Y/N): ").strip().lower()
                if confirm == "y":
                    break
                if confirm == "n":
                    print("Exit cancelled going back to menu...")
                    break
                else:
                    print("Invalid input! Please enter Y or N.")
            if confirm == "y":
                print("Exiting program...")
                break
            