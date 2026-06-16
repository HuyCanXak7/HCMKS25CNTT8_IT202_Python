import unittest

from energy_monitor import (
    calculate_energy_financials
)


class TestEnergyFinancials(
    unittest.TestCase
):
    """Test financial calculations."""

    def test_no_discount(self):
        """Total < 50000 kWh."""
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 10000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                10000,
                0,
                30000000
            )
        )

    def test_discount_applied(self):
        """Total >= 50000 kWh."""
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 50000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                50000,
                3,
                145500000.0
            )
        )

    def test_multiple_devices(self):
        """Multiple devices."""
        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 1000,
                "new_index": 21000,
                "status": "Normal"
            },
            {
                "id": "M02",
                "location": "B",
                "old_index": 2000,
                "new_index": 42000,
                "status": "Normal"
            }
        ]

        result = (
            calculate_energy_financials(
                devices
            )
        )

        self.assertEqual(
            result,
            (
                60000,
                3,
                174600000.0
            )
        )


if __name__ == "__main__":
    unittest.main()