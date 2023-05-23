class Bank:
    def __init__(self):
        self.client_details_list=[]
        self.loggedin=False
        self.amount=0
        self.Transfer_amount=0

    def register(self,name,phone,password):
        amount=self.amount
        conditions=True

        if(len(str(phone))<10 or len(str(phone))>10):
            print("Invalid Phone number")
            conditions=False

        if(len(str(password))<5 or len(str(password))>15):
            print("Invalid password!Enter password between 5 and 15 characters")
            conditions=False

        if(conditions==True):
            print("Account Created Successfully")
            self.client_details_list=[name,phone,password,amount]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")

    def login(self,name,phone,password):
        with open(f"{name}.txt","r") as f:
            details=f.read()
            self.client_details_list=details.split("\n")
            if str(phone) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin=True

            if(self.loggedin==True):
                print(f"{name} logged in")
                self.amount=int(self.client_details_list[3])
                self.name=name

            else:
                print("Wrong details!")

        
    def add_amount(self,amount):
        if(amount>0):
            self.amount=self.amount+amount
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_details_list=details.split("\n")

            with open(f"{self.name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.amount)))

            print("Amount added successfully")

        else:
            print("Enter the correct amount")


    def Transfer_cash(self,amount,name,phone):
        #Here name is the person who receives the amount
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.Transfer_amount = True

        
        if self.Transfer_amount== True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.amount - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balacne left =",left_cash)
            self.amount = left_cash



    def password_change(self,password):
        if(len(str(password))<5 or len(str(password))>15):
            print("Invalid password!Enter password between 5 and 15 characters")

        else:
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_details_list=details.split("\n")

            with open(f"{self.name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))

            print("Password Changed successfully")

    def phone_change(self,phone):
        if(len(str(phone))<10 or len(str(phone))>10):
            print("Invalid Phone number")

        else:
            with open(f"{self.name}.txt","r") as f:
                details=f.read()
                self.client_details_list=details.split("\n")

            with open(f"{self.name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[1]),str(phone)))

            print("Phone number Changed successfully")



    

            




if __name__=="__main__":
    Bank_object=Bank()
    print("Welcome to our Bank")
    print("1.Login")
    print("2.Create a new account")
    user=int(input("Please enter your choice:"))

    if user==1:
        print("Logging in")
        name=input("Enter your name:")
        phone=int(input("Enter your mobile no:"))
        password=input("Enter password:")
        Bank_object.login(name,phone,password)
        while True:
            if Bank_object.loggedin:
                print("1.Add amount:")
                print("2.Check Balance:")
                print("3.Transfer amount:")
                print("4.Edit profile:")
                print("5.Log out")
                login_user=int(input("Enter choice:"))
                if(login_user==1):
                    print("Balance=",Bank_object.amount)
                    amount_added=int(input("Enter the amount to be added:"))
                    Bank_object.add_amount(amount_added)
                    print("Choose the option:")
                    print("1.Back menu")
                    print("2.Logout")
                    choose=int(input())
                    if(choose==1):
                        continue
                    elif(choose==2):
                        break

                elif(login_user==2):
                    print("Balance:",Bank_object.amount)
                    print("Choose the option:")
                    print("1.Back menu")
                    print("2.Logout")
                    choose=int(input())
                    if(choose==1):
                        continue
                    elif(choose==2):
                        break

                elif(login_user==3):
                    print("Balance =",Bank_object.amount)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.amount:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Transfer_cash(amount,name,ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.amount:
                        print("Not enough balance")
                    
                elif(login_user==4):
                    print("\n1.Password Change")
                    print("\n2.Mobile no.Change")

                    edit_profile=int(input())
                    if(edit_profile==1):
                        new_password=input("Enter the password:")
                        Bank_object.password_change(new_password)

                        print("Choose the option:")
                        print("1.Back menu")
                        print("2.Logout")
                        choose=int(input())
                        if(choose==1):
                            continue
                        elif(choose==2):
                            break

                    elif(edit_profile==2):
                        new_ph=input("Enter mobile no.")
                        

                        Bank_object.phone_change(new_ph)

                        print("Choose the option:")
                        print("1.Back menu")
                        print("2.Logout")
                        choose=int(input())
                        if(choose==1):
                            continue
                        elif(choose==2):
                            break



                elif(login_user==5):
                    break


            
                

    if user==2:
        print("Creating a new account")
        name=input("Enter your name:")
        phone=int(input("Enter your mobile no:"))
        password=input("Enter password:")
        Bank_object.register(name,phone,password)
        










            





        
              



    
