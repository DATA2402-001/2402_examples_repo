class Person:

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class Car:

    def __init__(self, num_seats:int, car_type: str, model: str, odo: float, owner: Person) -> None:
        self.num_seats = num_seats
        self.car_type = car_type
        self.model = model
        self.odometer = odo
        self.owner = owner
    
    def __repr__(self) -> str:
        """
        ___repr___ method defines the text representation
        of the object
        """
        return f'{self.model} with {self.odometer}km'


eric = Person('eric', 'echalmers@mtroyal.ca')


fleet = [
    Car(3, 'truck', 'sierra', 500_000, eric),
    Car(2, 'sports car', 'stingray', 3, eric),
    Car(10, 'van', 'large van', 1000, eric)
]


for car in fleet:
    if car.num_seats > 2:
        print(car)

