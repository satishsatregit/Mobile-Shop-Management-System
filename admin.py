from Mob import mob
from adminmng import adminmngmt
from datetime import datetime
from mobileacc import mobpart 
def Admin():
    choice = 0
    mobMgmt = adminmngmt()
    while(choice != 9):
        print("\t\t------ Admin Menu ------")
        print("\t\t1.Add  mobile details.")
        print("\t\t2.Add mobile accessories.")
        print("\t\t3.Search mobile.")
        print("\t\t4.Delete mobile.")
        print("\t\t5.Edit mobile.")
        print("\t\t6.Display available data.")
        print("\t\t7.Display History.")
        print("\t\t8.User Details.")
        print("\t\t9.Exit")
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            id = int(input("Enter the mobile id: "))
            brand = input("Enter the brand name: ")
            price = float(input("Enter the price: "))
            size=float(input("Enter size of mobile screen in inches: "))
            time=datetime.now()
            e1 = mob(id,brand,price,size,time)
            mobMgmt.addmob(e1)
        elif(choice == 2):
            id=int(input("Enter id to accessories: "))
            name=input("Enter name of accessories: ")
            price=float(input("Enter price of accessories: "))
            time=datetime.now()
            p1=mobpart(id,name,price,time)
            mobMgmt.addpart(p1)
        elif(choice == 3):
            print("\ta.Search by id")
            print("\tb.Search by brand")
            ch = input("Enter your choice (a or b): ")
            if(ch.lower() == "a"):
                id =int(input("Enter the id to search"))
                mobMgmt.searchbyid(id)
            elif(ch.lower() == "b"):
                name = input("Enter brand name to search")
                mobMgmt.searchbybrand(name)
            else:
                print("Invalid choice")
        elif(choice == 4):
            id = int(input("Enter the id you want to delete: "))
            mobMgmt.DeletebyId(id)
        elif(choice == 5):
            id = int(input("Enter the id you want to edit: "))
            mobMgmt.editByid(id)
        elif(choice == 6):
            mobMgmt.ShowallMob()       
        elif(choice == 7):
            mobMgmt.showhist()
        elif(choice == 8):
            mobMgmt.showuser()
        elif(choice==9):
            pass
        else:
            print("Invalid choice")
         
    