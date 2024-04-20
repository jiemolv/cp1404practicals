from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    flagfall = 4.50    # Extra charge for each new fare
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        total_fare = super().get_fare() + self.flagfall
        return round(total_fare, 1)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        return distance_driven

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
