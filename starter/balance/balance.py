from transaction.transaction_category import TransactionCategory


class Balance:
    """Singleton responsible for tracking the current balance."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._balance = 0.0
            cls._instance._observers = []
        return cls._instance

    def __init__(self):
        """Return the existing Balance instance without resetting its state."""

    @classmethod
    def get_instance(cls):
        """Return the single Balance instance."""
        return cls()

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0.0

    def register_observer(self, observer):
        """Register an observer to receive balance updates."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        """Stop an observer from receiving balance updates."""
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(self, transaction):
        for observer in self._observers:
            observer.update(self._balance, transaction)

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount

    def add_expense(self, amount):
        """Subtract an expense from the balance."""
        self._balance -= amount

    def apply_transaction(self, transaction):
        """Apply a transaction and notify registered observers."""
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Unsupported transaction category")

        self._notify_observers(transaction)

    def get_balance(self):
        """Return the current net balance."""
        return self._balance

    def summary(self):
        """Return a formatted summary of the net balance."""
        return f"Current balance: ${self._balance:.2f}"
