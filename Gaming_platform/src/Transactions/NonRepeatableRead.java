package Transactions;

import DatabaseConnection.DataConnector;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class NonRepeatableRead {
    public static void simulate(String dbType, String isolationLevel) {
        // Transaction 1 simulates the first transaction
        Thread transaction1 = new Thread(() -> {
            try (Connection conn = DataConnector.connect(dbType)) {
                conn.setAutoCommit(false);
                Statement stmt = conn.createStatement();
                stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                // First select to read balance for a specific user
                ResultSet rs = stmt.executeQuery("SELECT balance FROM users WHERE id_user = 1");
                if (rs.next()) {
                    double balance = rs.getDouble("balance");
                    System.out.println("Transaction 1: Initial balance for user 1: " + balance);

                    // Simulating delay
                    Thread.sleep(5000);

                    // Second select after waiting to see if data changes (non-repeatable read)
                    rs = stmt.executeQuery("SELECT balance FROM users WHERE id_user = 1");
                    if (rs.next()) {
                        double updatedBalance = rs.getDouble("balance");
                        System.out.println("Transaction 1: Updated balance for user 1: " + updatedBalance);
                    }
                }

                conn.commit();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        // Transaction 2 simulates the second transaction that modifies the data
        Thread transaction2 = new Thread(() -> {
            try {
                // Ensuring that Transaction 1 starts first by delaying the second transaction
                Thread.sleep(2000);

                try (Connection conn = DataConnector.connect(dbType)) {
                    conn.setAutoCommit(false);
                    Statement stmt = conn.createStatement();
                    stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                    // Update user 1's balance during the delay, causing a non-repeatable read
                    PreparedStatement pstmt = conn.prepareStatement("UPDATE users SET balance = balance + 50 WHERE id_user = 1");
                    pstmt.executeUpdate();
                    System.out.println("Transaction 2: Updating user 1's balance (50 added).");

                    conn.commit();
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        // Start both threads to simulate concurrency
        transaction1.start();
        transaction2.start();

        try {
            // Wait for both threads to finish
            transaction1.join();
            transaction2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("✅ Non-repeatable Read Simulation (" + isolationLevel + ") complete.");
    }
}
