from Database.db_connection import DatabaseConnection

class Reviews:

    @staticmethod
    def create_review(id_reviews,game_id,user_id,rating,comment_reviews,timestamp):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO reviews (id_reviews,game_id,user_id,rating,comment_reviews,timestamp) VALUES (%s,%s,%s,%s,%s,%s)",
                (id_reviews,game_id,user_id,rating,comment_reviews,timestamp)
            )
            connection.commit()
            print(f"✅ The Record was added!")
        except Exception as e:
            print(f"❌ Error creating The Review: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_reviews():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM reviews")
            rev = cursor.fetchall()
            return rev
        except Exception as e:
            print(f"❌ Error reading The Review {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def update_review_rating(id_review, rating):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE reviews SET rating=%s WHERE id_reviews=%s",
                (rating,id_review)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating rating: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def delete_review(id_review):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM reviews WHERE id_reviews=%s",
                (id_review,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Review: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)