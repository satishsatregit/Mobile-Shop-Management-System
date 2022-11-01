class usermng:
    def displaymob(self):
            found= True
            if(found):
                with open("mobile.txt","r") as fp:
                    print(fp.read())
            else:
                print("NOT AVAILABLE")

    def displaypart(self):
            found= True
            if(found):
                with open("mobileacc.txt","r") as fp:
                    print(fp.read())
            else:
                print("NOT AVAILABLE")
    
    def Searchmob(self,name):
        try:
            with open("mobile.txt","r") as fp:
                for i in fp:
                    try:
                        (i.lower()).index(name.lower())
                        print("Found :",i)
                        break
                    except:
                        pass                        
                else:
                    print("Record not found")            
        except:
            print("File does not exist..")

    def userdetails(self,u):
        try:
            with open("mobile.txt","r") as fp:
                if u in fp:
                    with open("userdata.txt","a") as fp1:
                        fp1.write(str(u)+"\n")
                else:
                    print("ID not found.")
        except:
            print("file not found.")

    def useredit(self,id):
        mobilelist=[]
        found=False
        try:
            with open("userdata.txt","r") as fp2:
                for m in fp2:
                    try:
                        m.index(str(id),0,4)
                    except:
                        pass
                    else:
                        found=True
                        m=m.split(",")
                        print(m)
                        edit=input("do you wish to change users name (y/n): ")
                        if(edit.lower()=="y"):
                            m[1]=input("Enter new name: ")
                        elif(edit.lower()=="n"):
                            pass
                        edit=input("do you want to change mobile number(user)(y/n): ")
                        if(edit=="y"):
                            m[2]=input("Enter new mobile number.")
                        elif(edit.lower()=="n"):
                            pass
                        edit=input("do you want to change address(y/n): ")
                        if(edit=="y"):
                            m[3]=input("Enter new address.")
                        elif(edit.lower()=="n"):
                            pass
                        m=",".join(m)
                    mobilelist.append(m)
            if(found):
                with open("userdata.txt","w") as fp4:
                    for mob in mobilelist:
                        fp4.write(mob)
            else:
                print("Data not found.")
        except:
            print("File not found")
            return
    
    def usermobpayment(self,id):
        moblist=[]
        found=False
        try:
            with open("mobile.txt","r") as fp6:
                for i in fp6:
                    try:
                        i.index(str(id),0,4)
                    except:
                        moblist.append(i)
                    else:
                            found=True
                            with open("History.txt","a") as fp9:
                                fp9.write(i)
                                i=i.split(",")
                                print("-------------BILL---------------")
                                print("Total : ",i[2])
                if(found):
                    with open("mobile.txt","w") as fp7:
                        for i in moblist:
                            fp7.write(i)
                else:
                    print("record not found")
        except:
            print("file not found")
                
    def useraccpayment(self,id):
        moblist=[]
        found=False
        try:
            with open("mobileacc.txt","r") as fp6:
                for i in fp6:
                    try:
                        i.index(str(id),0,4)
                    except:
                        moblist.append(i)
                    else:
                            found=True
                            with open("History.txt","a") as fp9:
                                fp9.write(i)
                                i=i.split(",")
                                print("-------------BILL-------------")
                                print("Total : ",i[2])
                if(found):
                    with open("mobileacc.txt","w") as fp7:
                        for i in moblist:
                            fp7.write(i)
                else:
                    print("record not found")
        except:
            print("file not found")                         
                
                    
                        
  






 
                        