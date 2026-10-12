import unittest

from balance.balance import Balance
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_command import ApplyTransactionCommand
from transaction.transaction_command import TransactionProcessor


class TestTransactionCommand(unittest.TestCase):
    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_command_applies_transaction(self):
        transaction = Transaction(100, TransactionCategory.INCOME)
        command = ApplyTransactionCommand(self.balance, transaction)

        command.execute()

        self.assertEqual(self.balance.get_balance(), 100)

    def test_processor_executes_and_records_command(self):
        transaction = Transaction(40, TransactionCategory.EXPENSE)
        command = ApplyTransactionCommand(self.balance, transaction)
        processor = TransactionProcessor()

        processor.process(command)

        self.assertEqual(self.balance.get_balance(), -40)
        self.assertEqual(processor.history, [command])


if __name__ == "__main__":
    unittest.main()
