class userdet:
    def __init__(self,mobid,name,mob,add,time):
        self.mobileid=mobid
        self.name=name
        self.mob=mob
        self.address=add
        self.time=time
       

    def __str__(self):
        return str(self.mobileid)+","+str(self.name)+","+str(self.mob)+","+str(self.address)+","+str(self.time)
        