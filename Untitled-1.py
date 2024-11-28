import random

class HSBC_ATM:
    __accounts={}
    
    def init(self):
        self.__accounts = {}
        self.current_account = None

    def create_account(self):
        x=True
        while x==True:
            account_number=None
            try:
                name = str(input("Enter your name: "))
                account_number = int(input("Enter your account number: "))

            except:
                print ("name or number invalid")
            else:
                x=False
        if account_number in self.__accounts:
            print("An account with this number already exists.")
        else:
            while name.strip() == '':
                print("Name and account number cannot be empty. Please try again.")
                name=input("reinput your name correctly :")
            while str(account_number).find("0",0) ==-1 and str(account_number).find("1",0) ==-1 and str(account_number).find("2",0) ==-1 and str(account_number).find("3",0) ==-1 and str(account_number).find("3",0) ==-1 and str(account_number).find("4",0) ==-1 and str(account_number).find("5",0) ==-1 and str(account_number).find("6",0) ==-1 and str(account_number).find("7",0) ==-1 and str(account_number).find("8",0) ==-1 and str(account_number).find("9",0) ==-1:
                print("Name and account number cannot be empty. Please try again.")
                account_number=input("enter your account number corectly : ")
            
            

            self.__accounts[account_number] = {"name": name, "balance": 0}
            self.current_account = account_number
            print("Congratulations! Account created successfully")
            

    def check_details(self):
        if self.current_account:
            account = self.__accounts[self.current_account]
            print("ACCOUNT DETAIL")
            print(f"Account Holder: {account['name']}")
            print(f"Account Number: {self.current_account}")
            print(f"Available balance: LE.{account['balance']}")

    def check_balance(self):
        if self.current_account:
            balance = self.__accounts[self.current_account]['balance']
            print(f"Available balance: LE. {balance}")

    def deposit_amount(self):
        if self.current_account:
            amount = float(input("How much you want to deposit(LE.):"))
            self.__accounts[self.current_account]['balance'] += amount
            print(f"Current account balance: LE. {self.__accounts[self.current_account]['balance']}")
            print("printing receipt")
            print("Transaction is now complete.")
            print(f"Transaction number: ", random.randint(1000, 9999) ) 

    def withdraw_amount(self):
        if self.current_account:
            amount = float(input("How much you want to withdraw(LE.):"))
            if amount > self.__accounts[self.current_account]['balance']:
                print(f"Insufficient fund!\nYour balance is LE.{self.__accounts[self.current_account]['balance']} only.\nTry with lesser amount than balance.")
                print("printing receipt")
                print("Transaction is now complete.")
                print(f"Transaction number: ", random.randint(0, 9999) ) 
            else:

                self.__accounts[self.current_account]['balance'] -= amount
                print(f"LE.{amount} withdrawal successful!")
                print(f"Current account balance: LE. {self.__accounts[self.current_account]['balance']}")

    def transaction_menu(self):
        choice = 0
        
        while choice != 5:
            print("            TRANSACTION  ")
            print("            Menu: ")
            print("            1. Account Detail ")
            print("            2. Check Balance ")
            print("            3. Deposit ")
            print("            4. Withdraw ")
            print("            5. Exit ")
            try:
                choice = int(input("Enter 1, 2, 3, 4 or 5: "))
                if choice < 1 or choice > 5:
                    print("Invalid choice. Please enter a number from 1 to 5.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")
                continue
            if choice == 1:
                self.check_details()
            elif choice == 2:
                self.check_balance()
            elif choice == 3:
                self.deposit_amount()
            elif choice == 4:
                self.withdraw_amount()
            elif choice == 5:
            

                if self.current_account:
                    account = self.__accounts[self.current_account]
                    print(f"Account holder: {account['name']}")
                    print(f"Account number: {self.current_account}")
                    print(f"Available balance: LE.{account['balance']}")
                print(f"Thanks for choosing us as your bank , have agood day :) \n made with some student in HNU all copywrites are saved ")
                datas = [
                  [ 'thanks', 'for', 'all', ' ---- ', ' ---- ' ],
                  [ 'mohamed', 'wafik', 'mohamed', 'code', 'decoration' ],
                  [ 'ahmed', 'ezzat', 'awwad', 'code', 'structure' ],
                  [ 'mahmoud', 'ahmed', 'saad', 'code', 'Supervised']
                ]

                for j, data in enumerate(datas):
                  if j == 0:
                    # print(list(data))
                    max = 0
                    for i in datas:
                      max_len =  len(''.join(i))
                      if max_len > max:
                        max = max_len
                        max = max + 4 * len(datas[0])
                    max=79
                    print(f"max is {max}")
                    print('+' + '-' * max + '+')
                    v1, v2, v3, v4, v5 = datas[0]
                    print(f"|{v1:^15s}|{v2:^15s}|{v3:^15s}|{v4:^15s}|{v5:^15s}|")
                    print('+' +  '-' * max + '+')
                    continue
                  else:
                    # print( '+' + '-' * max + '+')
                    v1, v2, v3, v4, v5 = data
                    print(f"|{v1:^15s}|{v2:^15s}|{v3:^15s}|{v4:^15s}|{v5:^15s}|")
                    print('+' +  '-' * max + '+')
                    # print(type(data))
           

    def run(self):
        p=0
        print("WELCOME TO BANK OF HSBC")
        self.create_account()
        while True:
            sh = input("Do you want to do any transaction? (y/n): ").lower()
            if sh == 'y':
                self.transaction_menu()
                break  # Exit the loop if 'y' is entered
            elif sh == 'n':
                exit()
            else:
                print("Invalid entry. Please enter 'y' or 'n'.")
        
                        
obj=  HSBC_ATM()
obj.run()