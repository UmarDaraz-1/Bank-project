data = {}
list1 = ["Name", "Address", "Phone", "Amount"]

def accountCreate():
    account_num = input("Enter account number: ")
    for i in list1:
        list2.append(input("Enter %s: "%i))

    data[account_num] = dict(zip(list1 , list2))
    print("Account Created Succesfully")
    return

def bankingFunctions():
    choice = int(input("1. Check Bank Balance\n 2. Deposit Amount\n 3. Withdraw Amount\n"))
    if choice == 1:
        print("Available Balance: ", data[account_num]["Amount"])
        
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        new_amount = int(data[account_num]['Amount']) + amount
        data[account_num]["Amount"] = new_amount
        print("Deposit Succesfully")
        print("Available Balance: ", data[account_num]["Amount"])
        
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        new_amount = int(data[account_num]['Amount']) - amount
        data[account_num]["Amount"] = new_amount
        print("Withdraw Succesfully")
        print("Available Balance: ", data[account_num]["Amount"])

while True:
    list2 = []
    choice = int(input("1. New Customer\n 2. Existing Customer\n 3. Exit\n Select Your Choice: "))

    if choice == 1:
        accountCreate()
        
    elif choice == 2:
        account_num = input("Enter your account number: ")
        if account_num in data:
            print("===Account is found===")
            bankingFunctions()
        else:
            print("Account is not exist")
