#ATM using functions

balance = 10000
def display_menu():
    print("Welcome to the ATM")
    print("Choose the operation:")
    print("1. Credit")
    print("2. Debit")
    print("3. Mini Statement")
    print("4. Balance")
def credit(balance):
    amount=int(input('Enter amount: '))
    balance+=amount
    print("Amount credited:",amount)
    print("New Balance:",balance)
    return balance
def debit(balance):
    amount=int(input('Enter amount: '))
    if balance>=amount:
        balance-=amount
        print("Amount debited",amount)
        print("New Balance:",balance)
        return balance
    else:
        print("Insufficient Balance")
        return balance
def miniStatement(balance):
    print("Your current balance is ",balance)
def checkBalance(balance):
    print ("Current Account Balance : Rs.",balance)
for i in range(4):
    display_menu()
    choice=int(input("Enter your operation:"))
    if choice==1:
        balance=credit(balance)
    elif choice==2:
        balance=debit(balance)
    elif choice==3:
        balance=miniStatement(balance)
    elif choice==4:
        print("Thanks you!🙏\nVisit Again😊")
        break
    else:
        print("Invalid Operation")
