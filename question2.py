import os 
import datetime

def create_customer(name, account_number, balance=0.0):
    """Add new customer to customers.txt"""
    try:
        with open("customers.txt", "a") as f:
            f.write(f"{name},{account_number},{balance}\n")
        print(f"Customer {name} created with account {account_number}")
    except Exception as e:
        print(f"Error creating customer: {e}")

def find_customer(account_number):
    """Find customer by account number"""
    try:
        with open("customers.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 3 and data[1] == account_number:
                    return {"name": data[0], "account": data[1], "balance": float(data[2])}
        return None
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error finding customer: {e}")
        return None

def update_balance(account_number, new_balance):
    """Update customer balance in file"""
    try:
        customers = []
        with open("customers.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 3:
                    if data[1] == account_number:
                        customers.append(f"{data[0]},{data[1]},{new_balance}")
                    else:
                        customers.append(line.strip())
        
        with open("customers.txt", "w") as f:
            for customer in customers:
                f.write(customer + "\n")
    except Exception as e:
        print(f"Error updating balance: {e}")

def log_transaction(account_number, transaction_type, amount, new_balance):
    """Log transaction to transactions.txt"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("transactions.txt", "a") as f:
            f.write(f"{timestamp},{account_number},{transaction_type},{amount},{new_balance}\n")
    except Exception as e:
        print(f"Error logging transaction: {e}")

def deposit(account_number, amount):
    """Make deposit to account"""
    try:
        customer = find_customer(account_number)
        if not customer:
            print("Account not found")
            return
        
        if amount <= 0:
            print("Amount must be positive")
            return
            
        new_balance = customer["balance"] + amount
        update_balance(account_number, new_balance)
        log_transaction(account_number, "DEPOSIT", amount, new_balance)
        print(f"Deposited ${amount}. New balance: ${new_balance}")
        
    except Exception as e:
        print(f"Error processing deposit: {e}")

def withdraw(account_number, amount):
    """Make withdrawal from account"""
    try:
        customer = find_customer(account_number)
        if not customer:
            print("Account not found")
            return
            
        if amount <= 0:
            print("Amount must be positive")
            return
            
        if customer["balance"] < amount:
            print("Insufficient funds")
            return
            
        new_balance = customer["balance"] - amount
        update_balance(account_number, new_balance)
        log_transaction(account_number, "WITHDRAWAL", amount, new_balance)
        print(f"Withdrew ${amount}. New balance: ${new_balance}")
        
    except Exception as e:
        print(f"Error processing withdrawal: {e}")

# Example usage
if __name__ == "__main__":
    # Create customers
    create_customer("John Doe", "12345", 1000)
    create_customer("Jane Smith", "67890", 500)
    
    # Make transactions
    deposit("12345", 200)
    withdraw("12345", 150)
    deposit("67890", 300)
    withdraw("67890", 100)
