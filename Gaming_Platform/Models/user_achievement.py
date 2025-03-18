from Database.db_connection import DatabaseConnection

class UserAchievement:

    @staticmethod
    def create_user_achievements(id_user_achievements,user_id,achievement_id,unlocked_date):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO userachievements (id_user_achievements,user_id,achievement_id,unlocked_date) VALUES (%s,%s,%s,%s)",
                (id_user_achievements,user_id,achievement_id,unlocked_date)
            )
            connection.commit()
            print(f"✅ The Record was added !")
        except Exception as e:
            print(f"❌ Error creating The User's Achievement: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_user_achievements():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM userachievements")
            achievements = cursor.fetchall()
            return achievements
        except Exception as e:
            print(f"❌ Error reading The User's Achievements {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)



    @staticmethod
    def delete_user_achievements(id_user_achievements):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM userachievements WHERE id_user_achievements=%s",
                (id_user_achievements,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting User's Achievements: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)