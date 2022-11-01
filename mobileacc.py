class mobpart:
    def __init__(self,id,pname,pprice,pdate):
        self.pid=id
        self.pname=pname
        self.price=pprice
        self.date=pdate
    
    def __str__(self):
        return str(self.pid)+","+(self.pname)+","+str(self.price)+","+str(self.date)

