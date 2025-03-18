from Database.db_connection import DatabaseConnection
class Competitions:

    @staticmethod
    def create_competitions(id_competitions,game_id,name_competitions,prize_pool,start_date,end_date):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO competitions (id_competitions,game_id,name_competitions,prize_pool,start_date,end_date) VALUES (%s,%s, %s, %s, %s, %s)",
                (id_competitions,game_id,name_competitions,prize_pool,start_date,end_date)

            )
            connection.commit()
            print(f"✅ This record was added !")
        except Exception as e:
            print(f"❌ Error adding Competition: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_competitions():
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute("SELECT * FROM competitions")
            comp=cursor.fetchall()
            return comp
        except Exception as e:
            print(f"❌ Error reading Competitions: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def update_competition_prize_pool(id_competition,prize_pool):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "UPDATE competitions SET prize_pool=prize_pool+%s WHERE id_competitions=%s",
                (prize_pool,id_competition)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating prize_pool: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def delete_competition(id_competitions):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM gamesessions WHERE id_competitions=%s",
                (id_competitions,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Competition: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)
