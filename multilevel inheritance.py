class vehicle:
    def vehicle_info(self):
        print('Inside vehicle class')
class car(vehicle):
    def car_info(self):
        print('Inside car class')
class truck(vehicle):
    def truck_info(self):
        print('Inside truck class')
class sportscar(car,vehicle):
    def sports_car_info(self):
        print('Inside sportscar class')
a_car=sportscar()
a_car.vehicle_info()
a_car.car_info()
a_car.sports_car_info()
