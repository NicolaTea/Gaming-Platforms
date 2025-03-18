from Database.db_connection import DatabaseConnection

class Transactions:
        @staticmethod
        def create_transaction(id_transactions, user_id, game_id, amount):
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "INSERT INTO transactions (id_transactions, user_id, game_id, amount, date) VALUES (%s,%s,%s,%s,CURRENT_TIMESTAMP)",
                    (id_transactions, user_id, game_id, amount)
                )
                connection.commit()
                print(f"✅ The Transactions  {id_transactions} was successfully added !")
            except Exception as e:
                print(f"❌ Error creating The Transactions: {e}")
                connection.rollback()
            finally:
                cursor.close()
                DatabaseConnection.return_connection(connection)

        @staticmethod
        def get_all_transactions():
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM transactions")
                transactions = cursor.fetchall()
                return transactions
            except Exception as e:
                print(f"❌ Error reading the Transactions {e}")
                return []
            finally:
                cursor.close()
                DatabaseConnection.return_connection(connection)

        @staticmethod
        def update_transaction_balance(id_transactions, amount):
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "UPDATE transactions SET amount=amount + %s WHERE id_transactions=%s",
                    (amount, id_transactions)
                )
                connection.commit()
            except Exception as e:
                print(f"❌ Error updating amount: {e}")
                connection.rollback()
            finally:
                cursor.close()
                DatabaseConnection.return_connection(connection)

        @staticmethod
        def delete_transaction(id_transactions):
            connection = DatabaseConnection.get_connection()
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "DELETE FROM transactions WHERE id_transactions=%s",
                    (id_transactions,)
                )
                connection.commit()
            except Exception as e:
                print(f"❌ Error deleting Transaction: {e}")
                connection.rollback()
            finally:
                cursor.close()
                DatabaseConnection.return_connection(connection)