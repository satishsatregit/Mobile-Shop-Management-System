from Mob import mob

class adminmngmt:
    def addmob(self,m):
        try:
            with open("mobile.txt","a") as fp:
                fp.write(str(m)+"\n")
        except:
            print("file not found.")
        
    def addpart(self,p):
        try:
            with open("mobileacc.txt","a") as fp2:
                fp2.write(str(p)+"\n")
        except:
            print("file not found.")    
    def searchbyid(self,id):
        try:
            with open("mobile.txt","r") as fp:
                for i in fp:
                    try:
                        i.index(str(id),0,4)
                        print("found",i)
                        break
                    except:
                        pass
                else:
                    print("mobile not present.")        
        except:
            print("file is not present.")
        
    def searchbybrand(self,name):
        try:
            with open ("mobile.txt","r") as fp:
                for i in fp:
                    try:
                        (i.lower()).index(name.lower())
                        print("It is found.",i)
                        break
                    except:
                        print('not present')
                else:
                    "mobile not present."
        except:
            print("file is not present.")

    def DeletebyId(self,id):
        allmob=[]
        found=False
        try:
            with open ("mobile.txt","r") as fp2:
                for i in fp2:
                    try:
                        i.index(str(id),0,4)
                    except:
                        allmob.append(i)
                    else:
                        found=True
            if(found):
                with open("mobile.txt","w") as fp3:
                    for i in allmob:
                        fp3.write(i)
            else:
                print("record not found.")
        except:
            print("file not found.")
            return
    
    def editByid(self,id):
        allmob=[]
        found=False
        try:
            with open("mobile.txt","r") as fp4:
                for i in fp4:
                    try:
                        i.index(str(id),0,4)
                    except:
                        pass
                    else:
                        found=True
                        i=i.split(",")
                        print(i)
                        ans = input("Do you wish to change brand name? (y/n): ")
                        if(ans.lower() == "y"):
                            i[1] = input("Enter new brand name: ")
                        elif(ans.lower()=="n"):
                            pass                       
                        ans = input("Do you wish to change salary? (y/n): ")
                        if(ans.lower() == "y"):
                            i[2] = input("Enter new price: ")    
                            i[2] += "\n"
                        elif(ans.lower()=="n"):
                            pass
                        ans=input("Do you want to change size(screen): ")                
                        if(ans.lower()=="y"):
                            i[3]=input("Enter new size of screen: ")
                            i[3]+="\n"
                        elif(ans.lower()=="n"):
                            pass
                        i = ",".join(i)

                    allmob.append(i)
            if(found):
                with(open("mobile.txt","w"))as fp4:
                    for i in allmob:
                        fp4.write(i)
            else:
                print("record not found.")
        except:
            print("file is not present.")
    
    def ShowallMob(self):
        try:
            print("-----------MOBILE LIST-----------------")
            with open("mobile.txt","r") as fp1:
                print(fp1.read())
            print("-----------MOBILE ACCESSORIES----------")
            with open("mobileacc.txt","r") as fp2:
                print(fp2.read())
        except:
            print("file not found.")   

    def showhist(self):
        found=True
        if(found):
            with open("History.txt","r") as fp1:
                print(fp1.read())
        else:
            print("record not found..")

    def showuser(self):
        found=True
        if(found):
            with open("userdata.txt","r") as fp:
                print(fp.read())    
        else:
            print("NO DATA AVAILABLE..")
    
    