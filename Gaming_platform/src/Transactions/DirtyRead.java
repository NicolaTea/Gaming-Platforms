package Transactions;

import DatabaseConnection.DataConnector;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class DirtyRead {
    public static void simulate(String dbType, String isolationLevel) {
        // Transaction 1 simulates the first transaction
        Thread transaction1 = new Thread(() -> {
            try (Connection conn = DataConnector.connect(dbType)) {
                conn.setAutoCommit(false);
                Statement stmt = conn.createStatement();
                stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                // Read balance of user 1
                ResultSet rs = stmt.executeQuery("SELECT balance FROM users WHERE id_user = 1");
                if (rs.next()) {
                    double balance = rs.getDouble("balance");
                    System.out.println("Transaction 1: Initial balance for user 1: " + balance);
                }

                Thread.sleep(5000); // Simulating a delay
                conn.commit();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });

        // Transaction 2 simulates the second transaction
        Thread transaction2 = new Thread(() -> {
            try {
                // Ensuring Transaction 1 starts first
                Thread.sleep(2000);

                try (Connection conn = DataConnector.connect(dbType)) {
                    conn.setAutoCommit(false);
                    Statement stmt = conn.createStatement();
                    stmt.execute("SET TRANSACTION ISOLATION LEVEL " + isolationLevel);

                    // Update balance of user 1
                    stmt.executeUpdate("UPDATE users SET balance = balance + 100 WHERE id_user = 1");
                    System.out.println("Transaction 2: Modify user's balance.");

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

        System.out.println("✅ Dirty Read Simulation (" + isolationLevel + ") complete.");
    }
}
