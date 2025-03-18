package Models;

import DatabaseConnection.DataConnector;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Transactions {

    public static void createTransaction(int idTransactions, int userId, int gameId, double amount, String dbType) {
        String query = "INSERT INTO transactions (id_transactions, user_id, game_id, amount, date) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setInt(1, idTransactions);
            stmt.setInt(2, userId);
            stmt.setInt(3, gameId);
            stmt.setDouble(4, amount);

            stmt.executeUpdate();
            System.out.println("✅ The transaction " + idTransactions + " was successfully added!");

        } catch (SQLException e) {
            System.out.println("❌ Error creating the transaction: " + e.getMessage());
        }
    }

    public static void getAllTransactions(String dbType) {
        String query = "SELECT * FROM transactions";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                int id = rs.getInt("id_transactions");
                int userId = rs.getInt("user_id");
                int gameId = rs.getInt("game_id");
                double amount = rs.getDouble("amount");
                String date = rs.getString("date");

                System.out.println("💳 Transaction ID: " + id + " | User ID: " + userId + " | Game ID: " + gameId + " | Amount: $" + amount + " | Date: " + date);
            }

        } catch (SQLException e) {
            System.out.println("❌ Error reading transactions: " + e.getMessage());
        }
    }

    public static void updateTransactionAmount(int idTransactions, double amount, String dbType) {
        String query = "UPDATE transactions SET amount = amount + ? WHERE id_transactions = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setDouble(1, amount);
            stmt.setInt(2, idTransactions);

            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Transaction " + idTransactions + " amount updated!");
            } else {
                System.out.println("⚠️ Transaction with ID " + idTransactions + " does not exist.");
            }

        } catch (SQLException e) {
            System.out.println("❌ Error updating amount: " + e.getMessage());
        }
    }

    public static void deleteTransaction(int idTransactions, String dbType) {
        String query = "DELETE FROM transactions WHERE id_transactions = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setInt(1, idTransactions);

            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Transaction " + idTransactions + " deleted!");
            } else {
                System.out.println("⚠️ Transaction with ID " + idTransactions + " does not exist.");
            }

        } catch (SQLException e) {
            System.out.println("❌ Error deleting transaction: " + e.getMessage());
        }
    }
}
