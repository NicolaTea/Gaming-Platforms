from Database.db_connection import DatabaseConnection

class Friendship:

    @staticmethod
    def create_friendship(id_friends,user_id1,user_id2,status):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO friends (id_friends,user_id1,user_id2,status) VALUES (%s,%s,%s,%s)",
                (id_friends,user_id1,user_id2,status)
            )
            connection.commit()
            print(f"✅ The Friendship between  {user_id1} and {user_id2} was successfully added !")
        except Exception as e:
            print(f"❌ Error creating The Friendship: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_friendship():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM friends")
            friendship = cursor.fetchall()
            return friendship
        except Exception as e:
            print(f"❌ Error reading the Friendships {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def update_friendship_status(id_friends, status):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE friends SET status=%s WHERE id_friends=%s",
                (id_friends, status)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating status: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def delete_friendship(id_friends):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM friends WHERE id_friends=%s",
                (id_friends,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Friendship: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)