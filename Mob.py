class mob:
    def __init__(self,id,brand,price,size,time):
        self.id=id
        self.brand=brand
        self.price=price
        self.gsize=size
        self.time=time

    def __str__(self):
        return str(self.id)+","+str(self.brand)+","+str(self.price)+","+str(self.gsize)+","+str(self.time)