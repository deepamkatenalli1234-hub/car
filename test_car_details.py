from car_details import car_details


def test_car_details_output():
    result = car_details("CAR101", "Toyota", "Innova", 2500000)

    expected = (
        "Car ID : CAR101\n"
        "Brand  : Toyota\n"
        "Model  : Innova\n"
        "Price  : 2500000"
    )

    assert result == expected
