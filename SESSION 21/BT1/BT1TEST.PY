"""
Unit test for Wallet class.
"""

import unittest

from wallet import (
    Wallet,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):
    """Test cases for Wallet."""

    def setUp(self):
        """Create wallet before each test."""
        self.wallet = Wallet()

    def test_deposit_success(self):
        """Test successful deposit."""
        self.wallet.deposit(500000)

        self.assertEqual(
            self.wallet.balance,
            500000
        )

    def test_transfer_insufficient_balance(self):
        """Test insufficient balance exception."""
        with self.assertRaises(
            InsufficientBalanceError
        ):
            self.wallet.transfer(
                "0987654321",
                500000
            )

    def test_invalid_amount(self):
        """Test invalid amount exception."""
        with self.assertRaises(
            InvalidAmountError
        ):
            self.wallet.deposit(-1000)


if __name__ == "__main__":
    unittest.main()