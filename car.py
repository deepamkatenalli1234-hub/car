def car_details(car_id, brand, model, price):
    result = (
        f"Car ID : {car_id}\n"
        f"Brand  : {brand}\n"
        f"Model  : {model}\n"
        f"Price  : {price}"
    )
    return result


if __name__ == "__main__":
    # Sample input
    car_id = "CAR101"
    brand = "Toyota"
    model = "Innova"
    price = 2500000

    print(car_details(car_id, brand, model, price))
