"""
Unit test for Highlands POS.
"""

import unittest

from bt2 import (
    calculate_total,
    add_to_order,
    InvalidQuantityError
)


class TestHighlandsPOS(unittest.TestCase):
    """Test Highlands POS."""

    def test_calculate_total(self):
        """Test total calculation."""
        order = [
            {
                "code": "P1",
                "quantity": 2
            },
            {
                "code": "F1",
                "quantity": 1
            }
        ]

        result = calculate_total(order)

        self.assertEqual(
            result,
            125000
        )

    def test_invalid_quantity(self):
        """Test invalid quantity."""
        order = []

        with self.assertRaises(
            InvalidQuantityError
        ):
            add_to_order(
                order,
                "P1",
                -1
            )


if __name__ == "__main__":
    unittest.main()