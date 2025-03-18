import threading
import time
from Database.db_connection import DatabaseConnection

def lost_update_simulation(isolation_level):
    def transaction1():
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("BEGIN;")
            cursor.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level};")
            cursor.execute("SELECT balance FROM users WHERE id_user = 1;")
            balance = cursor.fetchone()[0]
            cursor.execute(f"UPDATE users SET balance = {balance + 50} WHERE id_user = 1;")
            print("Transaction 1: Update balance with 50.")
            time.sleep(5)
            cursor.execute("COMMIT;")
        except Exception as e:
            print(f"❌ Error Transaction 1: {e}")

    def transaction2():
        try:
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            cursor.execute("BEGIN;")
            cursor.execute(f"SET TRANSACTION ISOLATION LEVEL {isolation_level};")
            cursor.execute("SELECT balance FROM users WHERE id_user = 1;")
            balance = cursor.fetchone()[0]
            cursor.execute(f"UPDATE users SET balance = {balance + 30} WHERE id_user = 1;")
            print("Transaction 2: Update balance with 30.")
            cursor.execute("COMMIT;")
        except Exception as e:
            print(f"❌ Error Transaction 2: {e}")

    t1 = threading.Thread(target=transaction1)
    t2 = threading.Thread(target=transaction2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"✅ Lost Update Simulation ({isolation_level}) complete.")
