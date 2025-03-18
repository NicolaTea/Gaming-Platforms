import threading
import time
from Database.db_connection import DatabaseConnection

def phantom_read_simulation(isolation_level):
    def transaction1():
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("BEGIN;")
            cursor.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level};")
            cursor.execute("SELECT * FROM users WHERE balance > 500;")
            users = cursor.fetchall()
            print(f"Transaction 1:Found users: {users}")
            time.sleep(5)
            cursor.execute("SELECT * FROM users WHERE balance > 500;")
            users_again = cursor.fetchall()
            print(f"Transaction 1:Found users after modification: {users_again}")
            cursor.execute("COMMIT;")
        except Exception as e:
            print(f"❌ Error Transaction 1: {e}")

    def transaction2():
        try:
            time.sleep(2)
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("BEGIN;")
            cursor.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level};")
            cursor.execute("INSERT INTO users (id_user, name_user, email_user, password_user, balance) VALUES (99, 'User99', 'user99@example.com', 'pass123', 600);")
            print("Transaction 2: Adding a new user with balance 600.")
            cursor.execute("COMMIT;")
        except Exception as e:
            print(f"❌ Error Transaction 2: {e}")

    t1 = threading.Thread(target=transaction1)
    t2 = threading.Thread(target=transaction2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"✅ Phantom Read Simulation ({isolation_level}) complete.")
