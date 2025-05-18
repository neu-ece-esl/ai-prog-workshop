# 🔍 Debugging Object-Oriented Code in Python

### 🎯 Student Learning Objectives

**Leverage AI Tools for Code Review**: 
Students will effectively use AI tools (e.g., ChatGPT) to assist in debugging, understanding, and improving existing Python code.

**Critically Evaluate AI Suggestions**: 
Students will assess the correctness and quality of AI-generated code recommendations and make informed decisions about when and how to apply them.

**Develop Better Coding Habits**: 
Students will gain practical experience in writing cleaner, safer, and more maintainable Python code by combining manual reasoning with AI-assisted guidance.

**Level Up Code Style Through Expert-Like Feedback**:
By engaging with AI suggestions, students will experience a form of collaborative coding that mimics working with an advanced mentor—leading to more professional, readable, and efficient code practices.

---

## 🧠 Scenario

In this scenario, a simple `BankAccount` class is provided with minor bugs and structural issues. Please review the class to identify any logic errors or design flaws. Then, refactor it using object-oriented best practices, including:
- Encapsulation  
- Input validation  
- Returning values instead of printing directly  

**Hint:** You can ask AI tools like ChatGPT to help you identify and fix logic errors or design flaws.

## 🟨 Step 1: Original Buggy Code

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")

# Run the code
account = BankAccount("Alice", 100)
account.withdraw(150)  #  Should NOT allow this!
account.display_balance()
```

---

## 🤖 Suggested AI Prompt

Once you've identified the potential issues in the code, you can use the following prompt with an AI assistant like ChatGPT:

> **Prompt:**
>
> "Please review this Python class and identify any logic bugs or design flaws."

Copy the full code above and paste it along with this prompt into ChatGPT or your AI tool of choice.

---

## ✅ Sample Improved Version

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

# Run improved code
account = BankAccount("Alice", 100)
try:
    account.withdraw(150)  # Should raise an error
except ValueError as e:
    print(f"Error: {e}")
print(f"Current balance: {account.get_balance()}")
```
