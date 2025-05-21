# 🔍 Refactoring a Larger Codebase with Inefficiencies

### 🎯 Student Learning Objectives

**Recognize Redundancy and Poor Design in Larger Codebases**  
Students will explore a more complex system built on the previous `BankAccount` class and identify issues such as repetition, inefficient logic, and tight coupling.

**Refactor for Modularity and Reuse**  
Students will learn how to redesign and modularize code using principles like abstraction, composition, and separation of concerns.

**Use AI to Support Design Decisions**  
Students will use AI tools (e.g., ChatGPT) to refactor and restructure larger codebases and gain insight into common design patterns.

**Simulate Real-World Collaboration**  
By engaging with AI-generated suggestions, students will mimic the experience of collaborating with a senior developer to improve clarity, scalability, and maintainability of software.

---

## 🧠 Scenario

You are given a larger, inefficient version of a banking system that builds on the previous `BankAccount` class. This system now includes:

- A `Bank` class that manages multiple accounts  
- Repeated logic for deposits, withdrawals, and balance checks  
- No separation of logic between the bank and account operations  
- No input validation or logging  
- Minimal reuse of functionality

Your task is to:
1. Identify redundant and inefficient parts of the code
2. Refactor it into a cleaner, more modular design
3. What do you think about ChatGPT's recommendations?
Do they all make sense to you? Why or why not? Consider how the suggestions simplify or optimize the system, and whether you would apply them in your own refactoring.

**Hint:** Ask ChatGPT to identify common design flaws and recommend object-oriented design patterns like composition or delegation.

## 🟨 Step 1: Original Inefficient Code

```python
# Starter Code: Inefficient Banking System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}: Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"{self.owner}: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.owner}: Withdrew {amount}. New balance is {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, owner, balance=0):
        self.accounts[owner] = BankAccount(owner, balance)

    def deposit(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].deposit(amount)

    def withdraw(self, owner, amount):
        if owner in self.accounts:
            self.accounts[owner].withdraw(amount)

    def display_balances(self):
        for account in self.accounts.values():
            print(f"{account.owner}: Balance = {account.balance}")

# Sample usage
bank = Bank()
bank.add_account("Alice", 100)
bank.add_account("Bob", 50)

bank.deposit("Alice", 50)
bank.withdraw("Bob", 70)
bank.display_balances()
```

---

## 🤖 Suggested AI Prompt

Once you've analyzed the inefficiencies in the code, you can use the following prompt with an AI assistant like ChatGPT:

> **Prompt:**
>
> "Please review this banking system implementation and identify design flaws, redundancies, and inefficiencies. Suggest object-oriented refactoring strategies and design patterns that would make this code more modular, maintainable, and robust."

Copy the full code above and paste it along with this prompt into ChatGPT or your AI tool of choice.

---

## ✅ Sample Improved Version

```python
# Refactored Banking System

class Transaction:
    def __init__(self, transaction_type, amount, timestamp=None):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp or datetime.now()
    
    def __str__(self):
        return f"{self.transaction_type}: ${self.amount:.2f} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class BankAccount:
    def __init__(self, owner, account_id, balance=0):
        self._owner = owner
        self._account_id = account_id
        self._balance = balance
        self._transactions = []
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def account_id(self):
        return self._account_id
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self._balance += amount
        self._transactions.append(Transaction("Deposit", amount))
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        self._balance -= amount
        self._transactions.append(Transaction("Withdrawal", amount))
        return self._balance
    
    def get_transaction_history(self):
        return self._transactions
    
    def __str__(self):
        return f"Account {self._account_id} - {self._owner}: ${self._balance:.2f}"


class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}
        self._next_account_id = 1000  # Starting account ID
    
    def create_account(self, owner, initial_balance=0):
        account_id = self._generate_account_id()
        account = BankAccount(owner, account_id, initial_balance)
        self._accounts[account_id] = account
        return account_id
    
    def _generate_account_id(self):
        account_id = self._next_account_id
        self._next_account_id += 1
        return account_id
    
    def get_account(self, account_id):
        if account_id not in self._accounts:
            raise ValueError(f"Account with ID {account_id} not found")
        return self._accounts[account_id]
    
    def deposit(self, account_id, amount):
        account = self.get_account(account_id)
        new_balance = account.deposit(amount)
        return new_balance
    
    def withdraw(self, account_id, amount):
        account = self.get_account(account_id)
        new_balance = account.withdraw(amount)
        return new_balance
    
    def transfer(self, from_account_id, to_account_id, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
            
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        
        return True
    
    def get_total_balance(self):
        return sum(account.balance for account in self._accounts.values())
    
    def display_all_accounts(self):
        return [str(account) for account in self._accounts.values()]

# Example usage
bank = Bank("Example Bank")
alice_id = bank.create_account("Alice", 100)
bob_id = bank.create_account("Bob", 50)

try:
    bank.deposit(alice_id, 50)
    bank.withdraw(bob_id, 30)
    print(f"Transfer successful: {bank.transfer(alice_id, bob_id, 25)}")
    
    for account_info in bank.display_all_accounts():
        print(account_info)
        
except ValueError as e:
    print(f"Error: {e}")
```

This refactored version introduces:
- A `Transaction` class to track account activity
- Proper encapsulation with private attributes and accessor methods
- Input validation throughout
- A unique identifier system for accounts
- Exception handling instead of print statements
- A transfer method as a higher-level operation
- Better organization and separation of concerns

---

## ✅ Sample Improved Version 2 (3.7 Sonnet)

```python
# Alternative Refactored Banking System with Domain-Driven Design principles

from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from uuid import uuid4

class TransactionType(Enum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()
    TRANSFER_OUT = auto()
    TRANSFER_IN = auto()

@dataclass
class Transaction:
    """Immutable record of an account transaction"""
    id: str
    account_id: str
    transaction_type: TransactionType
    amount: float
    timestamp: datetime
    description: str = ""
    
    @classmethod
    def create(cls, account_id: str, transaction_type: TransactionType, amount: float, description: str = ""):
        return cls(
            id=str(uuid4()),
            account_id=account_id,
            transaction_type=transaction_type,
            amount=amount,
            timestamp=datetime.now(),
            description=description
        )


class AccountService:
    """Service layer handling account operations and business rules"""
    
    def __init__(self, transaction_log=None):
        self._transaction_log = transaction_log or InMemoryTransactionLog()
    
    def deposit(self, account: 'BankAccount', amount: float, description: str = "") -> float:
        """Process a deposit and return the new balance"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        transaction = Transaction.create(
            account.id, 
            TransactionType.DEPOSIT, 
            amount,
            description
        )
        
        self._transaction_log.add(transaction)
        return account.apply_transaction(transaction)
    
    def withdraw(self, account: 'BankAccount', amount: float, description: str = "") -> float:
        """Process a withdrawal and return the new balance"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
            
        if amount > account.balance:
            raise ValueError(f"Insufficient funds: available {account.balance}, requested {amount}")
        
        transaction = Transaction.create(
            account.id, 
            TransactionType.WITHDRAWAL, 
            amount,
            description
        )
        
        self._transaction_log.add(transaction)
        return account.apply_transaction(transaction)
    
    def transfer(self, from_account: 'BankAccount', to_account: 'BankAccount', 
                 amount: float, description: str = "") -> Tuple[float, float]:
        """Transfer money between accounts and return both new balances"""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
            
        if from_account.id == to_account.id:
            raise ValueError("Cannot transfer to the same account")
            
        if amount > from_account.balance:
            raise ValueError(f"Insufficient funds for transfer: available {from_account.balance}, requested {amount}")
        
        # Create outgoing transaction
        outgoing = Transaction.create(
            from_account.id,
            TransactionType.TRANSFER_OUT,
            amount,
            f"Transfer to {to_account.owner}: {description}"
        )
        
        # Create incoming transaction with same UUID
        incoming = Transaction.create(
            to_account.id,
            TransactionType.TRANSFER_IN,
            amount,
            f"Transfer from {from_account.owner}: {description}"
        )
        
        # Log both transactions
        self._transaction_log.add(outgoing)
        self._transaction_log.add(incoming)
        
        # Apply changes to accounts
        from_balance = from_account.apply_transaction(outgoing)
        to_balance = to_account.apply_transaction(incoming)
        
        return (from_balance, to_balance)
    
    def get_transaction_history(self, account_id: str) -> List[Transaction]:
        """Retrieve all transactions for an account"""
        return self._transaction_log.get_by_account(account_id)


class InMemoryTransactionLog:
    """Simple in-memory transaction storage"""
    
    def __init__(self):
        self._transactions: List[Transaction] = []
    
    def add(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)
    
    def get_by_account(self, account_id: str) -> List[Transaction]:
        return [t for t in self._transactions if t.account_id == account_id]
    
    def get_all(self) -> List[Transaction]:
        return self._transactions.copy()


class BankAccount:
    """Domain entity representing a bank account"""
    
    def __init__(self, id: str, owner: str, balance: float = 0):
        self._id = id
        self._owner = owner
        self._balance = balance
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> float:
        return self._balance
    
    def apply_transaction(self, transaction: Transaction) -> float:
        """Apply a transaction to this account and return the new balance"""
        if transaction.account_id != self._id:
            raise ValueError(f"Transaction {transaction.id} does not belong to this account")
        
        if transaction.transaction_type == TransactionType.DEPOSIT or transaction.transaction_type == TransactionType.TRANSFER_IN:
            self._balance += transaction.amount
        elif transaction.transaction_type == TransactionType.WITHDRAWAL or transaction.transaction_type == TransactionType.TRANSFER_OUT:
            self._balance -= transaction.amount
        else:
            raise ValueError(f"Unknown transaction type: {transaction.transaction_type}")
            
        return self._balance
    
    def __str__(self) -> str:
        return f"Account {self._id} - {self._owner}: ${self._balance:.2f}"


class Bank:
    """Application service coordinating banking operations"""
    
    def __init__(self, name: str):
        self._name = name
        self._accounts: Dict[str, BankAccount] = {}
        self._account_service = AccountService()
    
    def create_account(self, owner: str, initial_balance: float = 0) -> str:
        """Create a new account and return its ID"""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
            
        account_id = str(uuid4())
        account = BankAccount(account_id, owner, initial_balance)
        self._accounts[account_id] = account
        
        # Record initial deposit if any
        if initial_balance > 0:
            self._account_service.deposit(account, initial_balance, "Initial deposit")
            
        return account_id
    
    def get_account(self, account_id: str) -> BankAccount:
        """Retrieve an account by ID"""
        if account_id not in self._accounts:
            raise ValueError(f"Account {account_id} not found")
            
        return self._accounts[account_id]
    
    def deposit(self, account_id: str, amount: float, description: str = "") -> float:
        """Deposit funds to an account"""
        account = self.get_account(account_id)
        return self._account_service.deposit(account, amount, description)
    
    def withdraw(self, account_id: str, amount: float, description: str = "") -> float:
        """Withdraw funds from an account"""
        account = self.get_account(account_id)
        return self._account_service.withdraw(account, amount, description)
    
    def transfer(self, from_account_id: str, to_account_id: str, amount: float, description: str = "") -> Tuple[float, float]:
        """Transfer funds between accounts"""
        from_account = self.get_account(from_account_id)
        to_account = self.get_account(to_account_id)
        return self._account_service.transfer(from_account, to_account, amount, description)
    
    def get_transaction_history(self, account_id: str) -> List[Transaction]:
        """Get transaction history for an account"""
        self.get_account(account_id)  # Verify account exists
        return self._account_service.get_transaction_history(account_id)
    
    def get_total_assets(self) -> float:
        """Calculate total assets held by the bank"""
        return sum(account.balance for account in self._accounts.values())
    
    def list_accounts(self) -> List[str]:
        """List all accounts in a human-readable format"""
        return [str(account) for account in self._accounts.values()]


# Example usage
if __name__ == "__main__":
    bank = Bank("Modern Banking, Inc.")
    
    try:
        # Create accounts
        alice_id = bank.create_account("Alice Smith", 100)
        bob_id = bank.create_account("Bob Jones", 50)
        
        print(f"Created accounts:\n" + "\n".join(bank.list_accounts()))
        print(f"Total bank assets: ${bank.get_total_assets():.2f}")
        
        # Perform operations
        bank.deposit(alice_id, 75.50, "Salary deposit")
        bank.withdraw(bob_id, 20, "ATM withdrawal")
        
        # Transfer funds
        from_balance, to_balance = bank.transfer(alice_id, bob_id, 30, "Lunch repayment")
        print(f"Transfer complete. Alice's balance: ${from_balance:.2f}, Bob's balance: ${to_balance:.2f}")
        
        # Show final account status
        print("\nFinal account status:")
        print("\n".join(bank.list_accounts()))
        
        # Show transaction history
        print("\nAlice's transaction history:")
        for tx in bank.get_transaction_history(alice_id):
            print(f"  {tx.transaction_type.name}: ${tx.amount:.2f} - {tx.description}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

This alternative refactoring introduces several advanced software design principles:

1. **Domain-Driven Design**: The code is structured around the core domain concepts (accounts, transactions) with clear separation of responsibilities.

2. **Service Layer**: An `AccountService` manages all transaction operations, applying business rules consistently.

3. **Immutable Transactions**: Transactions are immutable records of events, making the system more audit-friendly.

4. **Repository Pattern**: The `InMemoryTransactionLog` serves as a simple repository for transaction history.

5. **Type Annotations**: Python type hints improve code readability and enable better IDE support.

6. **Value Objects**: Using `dataclass` for the `Transaction` class and `Enum` for transaction types.

7. **UUID-based Identifiers**: More robust than sequential IDs for distributed systems.

8. **Command-Query Separation**: Methods either modify state or return information, rarely both.

9. **Rich Domain Model**: The `BankAccount` class contains business logic related to accounts.

This implementation would scale better to a larger financial system with more complex requirements like different account types, interest calculations, or integration with external systems. It also provides a stronger audit trail and better error handling.
