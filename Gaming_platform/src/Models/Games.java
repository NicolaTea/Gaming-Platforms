package Models;

import DatabaseConnection.DataConnector;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Games {

    public static void createGame(int idGames, String title, String genre, double price, String developer, String dbType) {
        String query = "INSERT INTO games (id_games, title, genre, price, developer) VALUES (?, ?, ?, ?, ?)";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setInt(1, idGames);
            stmt.setString(2, title);
            stmt.setString(3, genre);
            stmt.setDouble(4, price);
            stmt.setString(5, developer);

            stmt.executeUpdate();
            System.out.println("✅ Game " + title + " added successfully!");

        } catch (SQLException e) {
            System.out.println("❌ Error adding game: " + e.getMessage());
        }
    }

    public static void getAllGames(String dbType) {
        String query = "SELECT * FROM games";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                int id = rs.getInt("id_games");
                String title = rs.getString("title");
                String genre = rs.getString("genre");
                double price = rs.getDouble("price");
                String developer = rs.getString("developer");

                System.out.println("🎮 " + id + ": " + title + " | " + genre + " | " + price + "$ | Developer: " + developer);
            }

        } catch (SQLException e) {
            System.out.println("❌ Error fetching games: " + e.getMessage());
        }
    }

    public static void updateGamePrice(int idGame, double newPrice, String dbType) {
        String query = "UPDATE games SET price = ? WHERE id_games = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setDouble(1, newPrice);
            stmt.setInt(2, idGame);

            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Price updated for game " + idGame + "!");
            } else {
                System.out.println("⚠️ Game with ID " + idGame + " does not exist.");
            }

        } catch (SQLException e) {
            System.out.println("❌ Error updating price: " + e.getMessage());
        }
    }

    public static void deleteGame(int idGame, String dbType) {
        String query = "DELETE FROM games WHERE id_games = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setInt(1, idGame);

            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Game " + idGame + " deleted!");
            } else {
                System.out.println("⚠️ Game with ID " + idGame + " does not exist.");
            }

        } catch (SQLException e) {
            System.out.println("❌ Error deleting game: " + e.getMessage());
        }
    }
}
