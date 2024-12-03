class BankAccount: 
    # Class-level dictionary to store all accounts
    Accounts = {}

    def __init__(self, holders_name: str, account_number: int, balance: int, age: int, next_of_kin: str, password: str, email: str):
        self.account_number = account_number 
        self.holders_name = holders_name
        self.balance = balance
        self.age = age 
        self.next_of_kin = next_of_kin
        self.password = password 
        self.email = email

    # Method to create an account
    def createAccount(self): 
        if self.account_number in BankAccount.Accounts:
            return print(f"An account with this number already exists: {self.account_number}")
        
        BankAccount.Accounts[self.account_number] = {
            'Holder Name': self.holders_name,
            'Balance': self.balance,
            'Age': self.age,
            'Next of Kin': self.next_of_kin,
            'Password': self.password, 
            'Email': self.email
        }

        print(f"Your account has been successfully created: {BankAccount.Accounts[self.account_number]}")
    
    # A method to show all accounts
    @classmethod
    def showAccounts(cls): 
        if not cls.Accounts:
            print("No accounts available.")
        else:
            print("All Accounts:")
            print(BankAccount.Accounts)

# Example Usage



# Show all accounts
BankAccount.showAccounts()
