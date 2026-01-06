class Car:
    def __init__(self, car_id, brand, model, year, scores):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def category(self):
        avg = self.average()
        if avg >= 90: return "Luxury"
        elif avg >= 80: return "High Performance"
        elif avg >= 65: return "Standard"
        elif avg >= 50: return "Basic"
        elif avg >= 40: return "Below Average"
        else: return "Poor"

    def show(self):
        print(f"\nCar {self.car_id} - {self.brand} {self.model} ({self.year})")
        print(f"Scores: {self.scores}, Avg: {self.average():.2f}, Category: {self.category()}")

def main():
    car = Car(
        input("Car ID: "),
        input("Brand: "),
        input("Model: "),
        input("Year: "),
        [int(input(f"Score {i}: ")) for i in range(1, 4)]
    )
    car.show()

if __name__ == "__main__":
    main()