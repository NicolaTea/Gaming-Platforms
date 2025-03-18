from Models.user import User
from Models.games import Games
from Models.transactions import Transactions
from Database.db_connection import DatabaseConnection
from Transactions.dirty_read import dirty_read_simulation
from Transactions.lost_update import lost_update_simulation
from Transactions.non_repeatable_read import non_repeatable_read_simulation
from Transactions.phantom_read import phantom_read_simulation

def main():

    db_type = choose_database()


    DatabaseConnection.initialize(db_type)

    while True:
        print("\nMain Menu:")
        print("1. Manage Users")
        print("2. Manage Games")
        print("3. Manage Transactions")
        print("4. Concurrency Issues")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_games()
        elif choice == '3':
            manage_transactions()
        elif choice == '4':
            concurrency_menu()
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please try again.")


def choose_database():

    print("Select the database:\n1. PostgreSQL\n2. MySQL")
    db_choice = input("Enter your choice (1 or 2): ")
    db_type = "postgres" if db_choice == "1" else "mysql" if db_choice == "2" else "postgres"
    print(f"✅ Connected to {db_type.upper()} database.")
    return db_type



def manage_users():
    print("\nUser Management:")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User Balance")
    print("4. Delete User")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        update_user_balance()
    elif choice == '4':
        delete_user()
    else:
        print("❌ Invalid choice.")


def add_user():
    print("Enter user details to add.")
    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    balance = float(input("Enter Balance: "))
    User.create_user(user_id, name, email, password, balance)


def view_users():
    users = User.get_all_users()
    for user in users:
        print(user)


def update_user_balance():
    user_id = int(input("Enter User ID: "))
    amount = float(input("Enter Amount to Add: "))
    User.update_user_balance(user_id, amount)


def delete_user():
    user_id = int(input("Enter User ID to Delete: "))
    User.delete_user(user_id)



def manage_games():
    print("\nGame Management:")
    print("1. Add Game")
    print("2. View Games")
    print("3. Update Game Price")
    print("4. Delete Game")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_game()
    elif choice == '2':
        view_games()
    elif choice == '3':
        update_game_price()
    elif choice == '4':
        delete_game()
    else:
        print("❌ Invalid choice.")


def add_game():
    print("Enter game details to add.")
    game_id = int(input("Enter Game ID: "))
    title = input("Enter Title: ")
    genre = input("Enter Genre: ")
    price = float(input("Enter Price: "))
    developer = input("Enter Developer: ")
    Games.create_game(game_id, title, genre, price, developer)


def view_games():
    games = Games.get_all_games()
    for game in games:
        print(game)


def update_game_price():
    game_id = int(input("Enter Game ID: "))
    new_price = float(input("Enter New Price: "))
    Games.update_game_price(game_id, new_price)


def delete_game():
    game_id = int(input("Enter Game ID to Delete: "))
    Games.delete_game(game_id)



def manage_transactions():
    print("\nTransaction Management:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Update Transaction Amount")
    print("4. Delete Transaction")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_transaction()
    elif choice == '2':
        view_transactions()
    elif choice == '3':
        update_transaction_amount()
    elif choice == '4':
        delete_transaction()
    else:
        print("❌ Invalid choice.")


def add_transaction():
    transaction_id = int(input("Enter Transaction ID: "))
    user_id = int(input("Enter User ID: "))
    game_id = int(input("Enter Game ID: "))
    amount = float(input("Enter Amount: "))
    Transactions.create_transaction(transaction_id, user_id, game_id, amount)


def view_transactions():
    transactions = Transactions.get_all_transactions()
    for transaction in transactions:
        print(transaction)


def update_transaction_amount():
    transaction_id = int(input("Enter Transaction ID: "))
    new_amount = float(input("Enter New Amount: "))
    Transactions.update_transaction_balance(transaction_id, new_amount)


def delete_transaction():
    transaction_id = int(input("Enter Transaction ID to Delete: "))
    Transactions.delete_transaction(transaction_id)



def concurrency_menu():
    print("\nChoose Concurrency Problem:")
    print("1. Dirty Read")
    print("2. Lost Update")
    print("3. Non-repeatable Read")
    print("4. Phantom Read")
    print("5. Back to Main Menu")


    choice = input("Enter your choice (1-5): ")


    print("\nChoose Isolation Level:")
    print("1. READ UNCOMMITTED")
    print("2. READ COMMITTED")
    print("3. REPEATABLE READ")
    print("4. SERIALIZABLE")

    isolation_choice = input("Enter your choice (1-4): ")

    isolation_level = ""
    if isolation_choice == "1":
        isolation_level = "READ UNCOMMITTED"
    elif isolation_choice == "2":
        isolation_level = "READ COMMITTED"
    elif isolation_choice == "3":
        isolation_level = "REPEATABLE READ"
    elif isolation_choice == "4":
        isolation_level = "SERIALIZABLE"
    else:
        print("❌ Invalid Isolation Level choice.")
        return


    if choice == '1':
        dirty_read_simulation(isolation_level)
    elif choice == '2':
        lost_update_simulation(isolation_level)
    elif choice == '3':
        non_repeatable_read_simulation(isolation_level)
    elif choice == '4':
        phantom_read_simulation(isolation_level)
    elif choice == '5':
        return
    else:
        print("❌ Invalid choice.")

main()