from user import User
from admin import Admin
choice=0
while(choice!=3):
    if(__name__=="__main__"):
        print("\t\t1.Admin Menu")
        print("\t\t2.User Menu")
        print("\t\t3.Exit")
        choice=int(input("Enter your Menu: "))
        if(choice==1):
            name=input("Enter username: ")
            pas=input("Enter passward: ")
            if(name=="abcd" and pas=="abc@13"):
                Admin()
            else:
                print("Incorrect Username and passward.")
        elif(choice==2):
            User()
        elif(choice==3):
            pass
        else:
            print("Invalid Key")
