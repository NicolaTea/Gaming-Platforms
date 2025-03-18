import threading
import time
from Database.db_connection import DatabaseConnection

def non_repeatable_read_simulation(isolation_level):
    def transaction1():
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("BEGIN;")
            cursor.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level};")
            cursor.execute("SELECT balance FROM users WHERE id_user = 1;")
            balance = cursor.fetchone()[0]
            print(f"Transaction 1: Reading initial balance: {balance}")
            time.sleep(5)
            cursor.execute("SELECT balance FROM users WHERE id_user = 1;")
            balance_again = cursor.fetchone()[0]
            print(f"Transaction 1: Read balance after modification: {balance_again}")
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
            cursor.execute("UPDATE users SET balance = balance + 50 WHERE id_user = 1;")
            print("Transaction 2: Modify user's balance (50 added).")
            cursor.execute("COMMIT;")
        except Exception as e:
            print(f"❌ Error Transaction 2: {e}")

    t1 = threading.Thread(target=transaction1)
    t2 = threading.Thread(target=transaction2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"✅ Non-repeatable Read Simulation ({isolation_level}) complete.")
