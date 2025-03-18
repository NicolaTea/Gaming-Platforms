from Database.db_connection import DatabaseConnection

class DLCs:

    @staticmethod
    def create_dlcs(id_dlcs,game_id,title,price,release_date):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO dlcs (id_dls,game_id,title,price,release_date) VALUES (%s,%s,%s,%s,%s)",
                (id_dlcs,game_id,title,price,release_date)
            )
            connection.commit()
            print(f"✅ The DLC  {title} was successfully added !")
        except Exception as e:
            print(f"❌ Error creating The DLC: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def get_all_dlcs():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM dlcs")
            dlcs = cursor.fetchall()
            return dlcs
        except Exception as e:
            print(f"❌ Error reading the DLCS {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def update_dlcs_balance(id_dlcs, amount):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE dlcs SET price=price + %s WHERE id_dls=%s",
                (amount, id_dlcs)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error updating price: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def delete_dlc(id_dlcs):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM dlcs WHERE id_dls=%s",
                (id_dlcs,)
            )
            connection.commit()
        except Exception as e:
            print(f"❌ Error deleting DLC: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)