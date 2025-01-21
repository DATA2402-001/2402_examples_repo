class Car:

    def __init__(self, num_seats:int, car_type: str, model: str, odo: float) -> None:
        self.num_seats = num_seats
        self.car_type = car_type
        self.model = model
        self.odometer = odo

fleet = [
    Car(3, 'truck', 'sierra', 500_000),
    Car(2, 'sports car', 'stingray', 3),
    Car(10, 'van', 'large van', 1000)
]

for car in fleet:
    if car.num_seats > 2:
        print(car.model)