package DatabaseConnection;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DataConnector {
    private static final String POSTGRES_URL = "jdbc:postgresql://localhost:5432/gaming_platform";
    private static final String POSTGRES_USER = "postgres";
    private static final String POSTGRES_PASSWORD = "1111";

    private static final String MYSQL_URL = "jdbc:mysql://localhost:3306/gaming_platform";
    private static final String MYSQL_USER = "root";
    private static final String MYSQL_PASSWORD = "password";


    public static Connection connect(String dbType) throws SQLException {
        try {
            if ("postgres".equalsIgnoreCase(dbType)) {
                Class.forName("org.postgresql.Driver");
                return DriverManager.getConnection(POSTGRES_URL, POSTGRES_USER, POSTGRES_PASSWORD);
            } else if ("mysql".equalsIgnoreCase(dbType)) {
                Class.forName("com.mysql.cj.jdbc.Driver");
                return DriverManager.getConnection(MYSQL_URL, MYSQL_USER, MYSQL_PASSWORD);
            } else {
                throw new IllegalArgumentException("Unknown database type: " + dbType);
            }
        } catch (ClassNotFoundException e) {
            throw new SQLException("Driver JDBC was not found for " + dbType, e);
        }
    }


    public static void closeConnection(Connection connection) {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("🔌 Connection was successfully closed!");
            } catch (SQLException e) {
                System.out.println("❌ Error closing connection: " + e.getMessage());
            }
        } else {
            System.out.println("⚠️ The connection is already closed or null.");
        }
    }
}
