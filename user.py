from userdetail import userdet
from Mob import mob
from usermng import usermng
from datetime import datetime
def User():
    choice=0
    usermanage=usermng()
    while(choice!=6):
        print("\t\t------ User Menu ------")
        print("\t\t1.display available mobiles/accessories.")
        print("\t\t2.Search available mobiles.")
        print("\t\t3.add details of buyer.")
        print("\t\t4.edit details of buyer.")
        print("\t\t5.make payment.")
        print("\t\t6.Exit")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            print("\t\ta.Display available mobiles.")
            print("\t\tb.Display available accssories of mobile.")
            choice1=input("Enter choice: ")
            if(choice1=="a"):
                usermanage.displaymob()
            elif(choice1=="b"):
                usermanage.displaypart()
            else:
                print("Invalid choice...")
        elif(choice==2):
            name=input("Enter mobile brand name do you want to search: ")
            usermanage.Searchmob(name)
        elif(choice==3):
            newmobile=input("Enter mobile/mobile accessories id you are baying: ")  
            name=input("Enter name of bayer who bay mobile/accssories : ")
            mobileno=int(input("Enter current mobile number: "))
            address=input("Enter adddress of user: ")
            time=datetime.now()
            u1=userdet(newmobile,name,mobileno,address,time)
            usermanage.userdetails(u1)
        elif(choice==4):
            edit=int(input("Enter mobile id that you have to edit user detsils:  "))
            usermanage.useredit(edit)
        elif(choice==5):
            print("\t\twhat you are buying.")
            print("\t\ta.mobile")
            print("\t\tb.mobile accesories")
            choice=input("Enter choice: ")
            if(choice=="a"):
                id=int(input("Enter mobile id: "))
                usermanage.usermobpayment(id)
            elif(choice=="b"):
                id=int(input("Enter id of mobile accessories: "))
                usermanage.useraccpayment(id)
        elif(choice==6):
            pass
        else:
            print("Invalid choice,Please enter valid choice.... ")









