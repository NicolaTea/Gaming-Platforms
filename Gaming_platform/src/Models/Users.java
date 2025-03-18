package Models;
import DatabaseConnection.DataConnector;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
public class Users {
    public static void createUser(int idUser, String nameUser, String emailUser, String passwordUser, double balance, String dbType) {
        String query = "INSERT INTO users (id_user, name_user, email_user, password_user, balance) VALUES (?, ?, ?, ?, ?)";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setInt(1, idUser);
            stmt.setString(2, nameUser);
            stmt.setString(3, emailUser);
            stmt.setString(4, passwordUser);
            stmt.setDouble(5, balance);
            stmt.executeUpdate();
            System.out.println("✅ User " + nameUser + " added successfully!");
        } catch (SQLException e) {
            System.out.println("❌ Error adding user: " + e.getMessage());
        }
    }
    public static void getAllUsers(String dbType) {
        String query = "SELECT * FROM users";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query);
             ResultSet rs = stmt.executeQuery()) {
            while (rs.next()) {
                int id = rs.getInt("id_user");
                String name = rs.getString("name_user");
                String email = rs.getString("email_user");
                String password = rs.getString("password_user");
                double balance = rs.getDouble("balance");
                System.out.println("👤 " + id + ": " + name + " | " + email + " | Balance: $" + balance);
            }
        } catch (SQLException e) {
            System.out.println("❌ Error fetching users: " + e.getMessage());
        }
    }

    public static void updateUserBalance(int idUser, double amount, String dbType) {
        String query = "UPDATE users SET balance = balance + ? WHERE id_user = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {
            stmt.setDouble(1, amount);
            stmt.setInt(2, idUser);
            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ Balance updated for user " + idUser + "!");
            } else {
                System.out.println("⚠️ User with ID " + idUser + " does not exist.");
            }
        } catch (SQLException e) {
            System.out.println("❌ Error updating balance: " + e.getMessage());
        }
    }

    public static void deleteUser(int idUser, String dbType) {
        String query = "DELETE FROM users WHERE id_user = ?";
        try (Connection connection = DataConnector.connect(dbType);
             PreparedStatement stmt = connection.prepareStatement(query)) {

            stmt.setInt(1, idUser);

            int rowsAffected = stmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("✅ User " + idUser + " deleted!");
            } else {
                System.out.println("⚠️ User with ID " + idUser + " does not exist.");
            }

        } catch (SQLException e) {
            System.out.println("❌ Error deleting user: " + e.getMessage());
        }
    }
}