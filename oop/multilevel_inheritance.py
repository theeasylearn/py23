class vehicle:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def vehicle_details(self):
        print(self.start)
        print(self.stop)
#child class  
class car(vehicle):
    def __init__(self, start, stop,type,fuel):
        super().__init__(start, stop)
        self.type = type
        self.fuel = fuel
        
    def car_details(self):
        print(self.type)
        print(self.fuel)

#leaf class         
class bmw(car):
    def __init__(self, start, stop, type, fuel,logo,engine):
       super().__init__(start, stop, type, fuel)
       self.logo = logo
       self.engine = engine
        
    def bmw_details(self):
        print(self.logo)
        print(self.engine)
        
bmw1 = bmw("acelerator","break","sports","petrol","BMW",2300)
bmw1.bmw_details()
bmw1.car_details()
bmw1.vehicle_details()
