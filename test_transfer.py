import unittest

from transfer import transfer_money


class TransferMoneyTests(unittest.TestCase):
    def test_successful_transfer(self):
        sender = {"balance": "100.00"}
        receiver = {"balance": "25.00"}

        success, message = transfer_money(sender, receiver, "40.00")

        self.assertTrue(success)
        self.assertEqual("Transfer successful", message)
        self.assertEqual("60.00", format(sender["balance"], ".2f"))
        self.assertEqual("65.00", format(receiver["balance"], ".2f"))

    def test_invalid_amount_does_not_crash(self):
        sender = {"balance": "100.00"}
        receiver = {"balance": "25.00"}

        success, message = transfer_money(sender, receiver, None)

        self.assertFalse(success)
        self.assertEqual("Invalid amount", message)
        self.assertEqual("100.00", sender["balance"])
        self.assertEqual("25.00", receiver["balance"])

    def test_invalid_account_does_not_crash(self):
        success, message = transfer_money(None, {"balance": "25.00"}, "10")

        self.assertFalse(success)
        self.assertEqual("Invalid account data", message)


if __name__ == "__main__":
    unittest.main()
