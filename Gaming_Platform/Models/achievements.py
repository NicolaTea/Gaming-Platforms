from Database.db_connection import DatabaseConnection

class Achievements:

    @staticmethod
    def create_achievements(id_achievements,game_id,name_achievements,description,points):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO achievements (id_achievements,game_id,name_achievements,description,points) VALUES (%s,%s,%s,%s,%s)",
                (id_achievements,game_id,name_achievements,description,points)
            )
            connection.commit()
            print(f"✅ The Achievements {name_achievements} was successfully added !")
        except Exception as e:
            print(f"❌ Error creating The Achievements: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_achievements():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM achievements")
            achievements = cursor.fetchall()
            return achievements
        except Exception as e:
            print(f"❌ Error reading The Achievements {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def update_achievements_points(id_achievements, points):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE achievements SET points=points+%s WHERE id_achievments=%s",
                (points,id_achievements)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating points: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def delete_achievements(id_achievements):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM achievements WHERE id_achievments=%s",
                (id_achievements,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Achievements: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)