"""This module serves as the entry point for the program."""

from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from transaction.external_income_transaction import ExternalFreelanceIncome
from transaction.transaction import Transaction
from transaction.transaction_adapter import TransactionAdapter
from transaction.transaction_category import TransactionCategory
from transaction.transaction_command import ApplyTransactionCommand
from transaction.transaction_command import TransactionProcessor


def main():
    print("Adding transactions...")

    balance = Balance.get_instance()
    balance.reset()
    balance.register_observer(PrintObserver())
    balance.register_observer(LowBalanceAlertObserver(threshold=50))

    transactions = [
        Transaction(100, TransactionCategory.INCOME),
        Transaction(50, TransactionCategory.EXPENSE),
        Transaction(200, TransactionCategory.INCOME),
        Transaction(75, TransactionCategory.EXPENSE),
    ]

    freelance_income = ExternalFreelanceIncome(
        1200,
        "INV-98765",
        "Mobile App Project",
    )
    adapted_transaction = TransactionAdapter(freelance_income).to_transaction()
    all_transactions = transactions + [adapted_transaction]

    processor = TransactionProcessor()
    for transaction in all_transactions:
        command = ApplyTransactionCommand(balance, transaction)
        processor.process(command)

    print(balance.summary())


if __name__ == "__main__":
    main()
