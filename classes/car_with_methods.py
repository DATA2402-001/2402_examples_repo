class Car:

    def __init__(self, num_seats:int, car_type: str, model: str, odo: float) -> None:
        self.num_seats = num_seats
        self.car_type = car_type
        self.model = model
        self.odometer = odo
        self.km_to_next_oil_change = 5000

    def drive(self, distance: float) -> None:
        self.odometer += distance
        self.km_to_next_oil_change -= distance

    def change_oil(self) -> None:
        self.km_to_next_oil_change = 5000
    
    def needs_oil_change(self) -> bool:
        return self.km_to_next_oil_change <= 0


my_car = Car(2, 'sports car', 'stingray', 5)
my_car.drive(1000)
print(my_car.odometer, my_car.needs_oil_change())
my_car.drive(10_000)
print(my_car.odometer, my_car.needs_oil_change())
