from Database.db_connection import DatabaseConnection
class CompetitionsParticipants:

    @staticmethod
    def create_competitions_participants(id_competitionparticipants,competition_id,user_id,ranking):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO competitions (id_competitionparticipants,competition_id,user_id,ranking) VALUES (%s,%s, %s, %s)",
                (id_competitionparticipants,competition_id,user_id,ranking)

            )
            connection.commit()
            print(f"✅ This record was added !")
        except Exception as e:
            print(f"❌ Error adding Competitions Participants: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_competitions_participants():
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute("SELECT * FROM competitionparticipants")
            comp_par=cursor.fetchall()
            return comp_par
        except Exception as e:
            print(f"❌ Error reading Competition Participants: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def update_competition_participants_ranking(id_competitionparticipants,ranking):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "UPDATE competitionparticipants SET ranking=%s WHERE id_competitionparticipants=%s",
                (ranking,id_competitionparticipants)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating ranking: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def delete_competition(id_competition_participants):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM competitionsparticipants WHERE id_competitionparticipants=%s",
                (id_competition_participants,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Competition Participants: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)
