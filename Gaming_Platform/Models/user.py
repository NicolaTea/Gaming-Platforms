from Database.db_connection import DatabaseConnection
class User:

    @staticmethod
    def create_user(id_user,name_user,email_user,password_user,balance):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (id_user,name_user,email_user,password_user,balance) VALUES (%s, %s, %s, %s, %s)",
                (id_user, name_user, email_user, password_user, balance)

            )
            connection.commit()
            print(f"✅ User {name_user} added successfully!")
        except Exception as e:
            print(f"❌ Error adding user: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_users():
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            users=cursor.fetchall()
            return users
        except Exception as e:
            print(f"❌ Error reading user: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def update_user_balance(id_user,amount):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET balance=balance + %s WHERE id_user=%s",
                (amount,id_user)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating user's balance: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def delete_user(id_user):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM users WHERE id_user=%s",
                (id_user,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting user: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)
