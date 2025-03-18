from Database.db_connection import DatabaseConnection

class Games:

    @staticmethod
    def create_game(id_games,title,genre,price,developer):
        connection=DatabaseConnection.get_connection()
        cursor=connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO games (id_games,title,genre,price,developer) VALUES (%s, %s, %s, %s, %s)",
                (id_games,title,genre,price,developer)
            )
            connection.commit()
            print(f"✅ Game {title} added successfully!")
        except Exception as e:
            print(f"❌ Error adding game: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def get_all_games():
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM games")
            games = cursor.fetchall()
            return games
        except Exception as e:
            print(f"❌ Error reading games: {e}")
            return []
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)


    @staticmethod
    def update_game_price(id_game, new_price):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE games SET price = %s WHERE id_games = %s",
                (new_price, id_game)
            )
            connection.commit()
            print(f"✅ New price {id_game}!")
        except Exception as e:
            print(f"❌ Error updating price: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)

    @staticmethod
    def delete_game(id_game):
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM games WHERE id_games = %s", (id_game,))
            connection.commit()
            print(f"✅ Game with id  {id_game} was deleted!")
        except Exception as e:
            print(f"❌Error deleting the game: {e}")
            connection.rollback()
        finally:
            cursor.close()
            DatabaseConnection.return_connection(connection)