package Transactions;

import DatabaseConnection.DataConnector;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class PhantomRead {
    public static void simulate(String dbType, String isolationLevel) {
        Thread transaction1 = new Thread(() -> {
            try (Connection conn = DataConnector.connect(dbType)) {
                conn.setAutoCommit(false);
                Statement stmt = conn.createStatement();
                stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE balance > 500");
                System.out.println("Transaction 1: Found users:");
                while (rs.next()) {
                    System.out.println(rs.getInt("id_user") + " | " + rs.getString("name_user") + " | " + rs.getDouble("balance"));
                }

                Thread.sleep(5000); // Simulating delay

                rs = stmt.executeQuery("SELECT * FROM users WHERE balance > 500");
                System.out.println("Transaction 1: Users after modification:");
                while (rs.next()) {
                    System.out.println(rs.getInt("id_user") + " | " + rs.getString("name_user") + " | " + rs.getDouble("balance"));
                }

                conn.commit();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        Thread transaction2 = new Thread(() -> {
            try {
                Thread.sleep(2000); // Ensure Transaction 1 starts first

                try (Connection conn = DataConnector.connect(dbType)) {
                    conn.setAutoCommit(false);
                    Statement stmt = conn.createStatement();
                    stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                    PreparedStatement pstmt = conn.prepareStatement(
                            "INSERT INTO users (id_user, name_user, email_user, password_user, balance) VALUES (?, ?, ?, ?, ?)"
                    );
                    pstmt.setInt(1, 99);
                    pstmt.setString(2, "User99");
                    pstmt.setString(3, "user99@example.com");
                    pstmt.setString(4, "pass123");
                    pstmt.setDouble(5, 600);
                    pstmt.executeUpdate();
                    System.out.println("Transaction 2: Adding a new user with balance 600.");

                    conn.commit();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        transaction1.start();
        transaction2.start();

        try {
            transaction1.join();
            transaction2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("✅ Phantom Read Simulation (" + isolationLevel + ") complete.");
    }
}