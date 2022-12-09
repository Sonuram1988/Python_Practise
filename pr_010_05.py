class Train:

    def __init__(self,name,seats,fair):
        self.name=name
        self.seats=seats
        self.fair=fair

    def info(self):
        print(f"name is {self.name} and seat is {self.seats}")
    
    def fairInfo(self):
        print(f"fair is Rs.{self.fair}")
    
    def bookTicket(self):
        if(self.seats)>0:
            print(f"Yours seats is confirmed and yours seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Train is full")

intercity=Train("Sonu Ram",2,300)
intercity.info()
intercity.fairInfo()
# print(intercity.name,intercity.seats,intercity.fair)
intercity.bookTicket()
intercity.info()
intercity.bookTicket()
intercity.info()
intercity.bookTicket()

