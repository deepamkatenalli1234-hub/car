import car
from car_details import car_details


class TestCarDetails(unittest.TestCase):

    def test_car_details_output(self):
        result = car_details("CAR101", "Toyota", "Innova", 2500000)

        expected_output = (
            "Car ID : CAR101\n"
            "Brand  : Toyota\n"
            "Model  : Innova\n"
            "Price  : 2500000"
        )

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
