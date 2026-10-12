class ApplyTransactionCommand:
    """Encapsulates applying one transaction to a balance."""

    def __init__(self, balance, transaction):
        self.balance = balance
        self.transaction = transaction

    def execute(self):
        self.balance.apply_transaction(self.transaction)


class TransactionProcessor:
    """Executes transaction commands and keeps a processing history."""

    def __init__(self):
        self.history = []

    def process(self, command):
        command.execute()
        self.history.append(command)
