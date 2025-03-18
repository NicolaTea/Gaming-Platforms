from Database.db_connection import DatabaseConnection

class Wishlists:

    @staticmethod
    def create_whishlist(id_whishlist,user_id,game_id,added_date):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO wishlists (id_whishlist,user_id,game_id,added_date) VALUES (%s,%s,%s,%s)",
                (id_whishlist,user_id,game_id,added_date)
            )
            connection.commit()
            print(f"✅ The Record was added !")
        except Exception as e:
            print(f"❌ Error creating The Wishlist: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_wishlists():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM wishlists")
            w = cursor.fetchall()
            return w
        except Exception as e:
            print(f"❌ Error reading The Wishlists {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)



    @staticmethod
    def delete_wishlist(id_wishlist):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM wishlists WHERE id_wishlist=%s",
                (id_wishlist,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting Wishlist: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)