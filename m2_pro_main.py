#store_fun file is imported
import store_fun as fn

#main function is defined
def main():
    
    print("\nIMPORTANT How cost is calculated:\n")
    
    print("Each item in the store costs $1 dollar")
    print("Customer buying 10 or more items recieves 5% discount")
    print("Customer LESS than 10 items, recieves 0 discount")
    print("6.2% sales tax is applied")
    
    choice = '0'

    while choice != '2':
        
        # call menu function
        menu()
        
        #enter choice
        choice = input("\nEnter Choice: ")
        
        #evaluate what user entered
        if choice == '1':

            # get input
            count = int(input("Enter number of items: "))
                
            # calculate cost, tax rate, and tax
            cost = fn.calcCost(count)
            taxrate = 0.062
            tax = cost * taxrate
            
            # display results
            fn.display(cost, tax)
       
        elif choice == '2': # exit
            print("\nProgram Terminating....")
        
        else:
            
            print("Invalid Entry!!!!\n")

#menu function is defined
def menu():
    """
    function displays menu options
    
    Returns
    -------
    None.
    
    """
        
    print("1) Calculate Cost")
    print("2) Exit")



if __name__ == "__main__":
    
    main()