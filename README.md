# ATM Simulator with Functions

This is a simple Python-based console application that simulates basic ATM operations such as credit, debit, mini statement, and balance inquiry. The program uses modular functions to structure the operations, making it efficient and easy to understand.

---

## Features

1. **Credit**  
   Deposit money into the account and view the updated balance.
   
2. **Debit**  
   Withdraw money from the account with a sufficient balance check.
   
3. **Mini Statement**  
   View the current balance in the account.
   
4. **Exit**  
   End the session with a friendly message.

---

## Usage

1. The program starts with a welcome message and displays the menu options.
2. Choose the desired operation by entering the corresponding number:
   - `1`: Credit
   - `2`: Debit
   - `3`: Mini Statement
   - `4`: Exit
3. Follow the prompts to operate, such as entering the amount for credit or debit.
4. Exit the program by selecting option `4`.

---

## Example Run

```plaintext
Welcome to the ATM
Choose the operation:
1. Credit
2. Debit
3. Mini Statement
4. Balance
Enter your operation: 1
Enter amount: 2000
Amount credited: 2000
New Balance: 12000
```

---

## Requirements

- Python 3.6 or higher.

---

## Notes

- The initial account balance is set to `10000`. You can modify this value in the code.
- The program checks for sufficient balance before processing debit operations.
- All transactions are handled during the session, and the balance resets after the program ends (no persistent storage).

--- 

Feel free to explore, modify, and improve the project. Contributions are welcome!
