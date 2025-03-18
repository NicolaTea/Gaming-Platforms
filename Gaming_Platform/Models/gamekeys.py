from Database.db_connection import DatabaseConnection
class GameKeys:

    @staticmethod
    def create_game_key(id_gamekeys,game_id,key_code,user_id):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO gamekeys (id_gamekeys,game_id,key_code,user_id) VALUES (%s, %s, %s, %s)",
                (id_gamekeys,game_id,key_code,user_id)

            )
            connection.commit()
            print(f"✅ This record was added !")
        except Exception as e:
            print(f"❌ Error adding Game Key: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_game_keys():
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute("SELECT * FROM gamekeys")
            game_k=cursor.fetchall()
            return game_k
        except Exception as e:
            print(f"❌ Error reading Game Keys: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def update_competition_prize_pool(id_game_key,key_code):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "UPDATE gamekeys SET key_code=%s WHERE id_gamekeys=%s",
                (key_code,id_game_key)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating key code: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def delete_game_key(id_game_key):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM gamekeysWHERE id_gamekeys=%s",
                (id_game_key,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Game Key: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)
