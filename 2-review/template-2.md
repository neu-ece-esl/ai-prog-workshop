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

