from Database.db_connection import DatabaseConnection
class GameSessions:

    @staticmethod
    def create_game_sessions(id_gamesessions,user_id,game_id,session_start,session_end,playtime_minutes):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO gamesessions (id_gamesessions,user_id,game_id,session_start,session_end,playtime_minutes) VALUES (%s,%s, %s, %s, %s, %s)",
                (id_gamesessions,user_id,game_id,session_start,session_end,playtime_minutes)

            )
            connection.commit()
            print(f"✅ The Game Session {id_gamesessions} started at  {session_start} and ended at {session_end} with {playtime_minutes} minutes. This record was added !")
        except Exception as e:
            print(f"❌ Error adding Game session: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_game_sessions():
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute("SELECT * FROM gamesessions")
            game_sessions=cursor.fetchall()
            return game_sessions
        except Exception as e:
            print(f"❌ Error reading Game sessions: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

#NU STIU LA CE SA DAU UPDATE
    @staticmethod
    def update_game_session_(id_game_session,blank):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "UPDATE gamesessions SET balance=balance + %s WHERE id_gamesessions=%s",
                (blank,id_game_session)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating blank: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def delete_game_session(id_game_session):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM gamesessions WHERE id_gamesessions=%s",
                (id_game_session,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Game Session: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)
