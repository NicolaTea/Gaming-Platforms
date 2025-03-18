import Models.Users;
import Models.Games;
import Models.Transactions;
import java.util.Scanner;
import Concurrency.ConcurrencyManager; // Assume this package handles concurrency simulations

public class Main {

    private static String dbType = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Choose the database
        System.out.println("Select the database:\n1. PostgreSQL\n2. MySQL");
        int dbChoice = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        dbType = (dbChoice == 1) ? "postgres" : "mysql";

        System.out.println("✅ Connected to " + dbType.toUpperCase());

        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Manage Users");
            System.out.println("2. Manage Games");
            System.out.println("3. Manage Transactions");
            System.out.println("4. Concurrency Issues");
            System.out.println("5. Exit");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    manageUsers(scanner);
                    break;
                case 2:
                    manageGames(scanner);
                    break;
                case 3:
                    manageTransactions(scanner);
                    break;
                case 4:
                    concurrencyMenu(scanner);
                    break;
                case 5:
                    System.out.println("👋 Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("❌ Invalid choice. Try again.");
            }
        }
    }

    private static void concurrencyMenu(Scanner scanner) {
        while (true) {
            System.out.println("\nChoose Isolation Level:");
            System.out.println("1 - READ UNCOMMITTED");
            System.out.println("2 - READ COMMITTED");
            System.out.println("3 - REPEATABLE READ");
            System.out.println("4 - SERIALIZABLE");
            System.out.println("5 - Back to main menu");

            int isolationChoice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            if (isolationChoice == 5) return;

            String isolationLevel = switch (isolationChoice) {
                case 1 -> "READ UNCOMMITTED";
                case 2 -> "READ COMMITTED";
                case 3 -> "REPEATABLE READ";
                case 4 -> "SERIALIZABLE";
                default -> {
                    System.out.println("❌ Invalid option. Defaulting to READ COMMITTED.");
                    yield "READ COMMITTED";
                }
            };

            System.out.println("\nChoose concurrency problem:");
            System.out.println("1 - Dirty Read");
            System.out.println("2 - Lost Update");
            System.out.println("3 - Non-repeatable Read");
            System.out.println("4 - Phantom Read");
            System.out.println("5 - Back to main menu");

            int problemChoice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            if (problemChoice == 5) return;

            // Passing dbType along with isolationLevel to the concurrency manager
            switch (problemChoice) {
                case 1:
                    ConcurrencyManager.dirtyReadSimulation(dbType, isolationLevel);
                    break;
                case 2:
                    ConcurrencyManager.lostUpdateSimulation(dbType, isolationLevel);
                    break;
                case 3:
                    ConcurrencyManager.nonRepeatableReadSimulation(dbType, isolationLevel);
                    break;
                case 4:
                    ConcurrencyManager.phantomReadSimulation(dbType, isolationLevel);
                    break;
                default:
                    System.out.println("❌ Invalid option, try again.");
            }
        }
    }

    private static void manageUsers(Scanner scanner) {
        System.out.println("\nUser Management:");
        System.out.println("1. Add User");
        System.out.println("2. View Users");
        System.out.println("3. Update User Balance");
        System.out.println("4. Delete User");
        int choice = scanner.nextInt();
        scanner.nextLine(); // Consume newline

        switch (choice) {
            case 1:
                System.out.print("Enter User ID: ");
                int id = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Enter Name: ");
                String name = scanner.nextLine();
                System.out.print("Enter Email: ");
                String email = scanner.nextLine();
                System.out.print("Enter Password: ");
                String password = scanner.nextLine();
                System.out.print("Enter Balance: ");
                double balance = scanner.nextDouble();
                Users.createUser(id, name, email, password, balance, dbType);
                break;
            case 2:
                Users.getAllUsers(dbType);
                break;
            case 3:
                System.out.print("Enter User ID: ");
                int userId = scanner.nextInt();
                System.out.print("Enter Amount to Add: ");
                double amount = scanner.nextDouble();
                Users.updateUserBalance(userId, amount, dbType);
                break;
            case 4:
                System.out.print("Enter User ID to Delete: ");
                int deleteId = scanner.nextInt();
                Users.deleteUser(deleteId, dbType);
                break;
            default:
                System.out.println("❌ Invalid choice.");
        }
    }

    private static void manageGames(Scanner scanner) {
        System.out.println("\nGame Management:");
        System.out.println("1. Add Game");
        System.out.println("2. View Games");
        System.out.println("3. Update Game Price");
        System.out.println("4. Delete Game");
        int choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
            case 1:
                System.out.print("Enter Game ID: ");
                int id = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Enter Title: ");
                String title = scanner.nextLine();
                System.out.print("Enter Genre: ");
                String genre = scanner.nextLine();
                System.out.print("Enter Price: ");
                double price = scanner.nextDouble();
                scanner.nextLine();
                System.out.print("Enter Developer: ");
                String developer = scanner.nextLine();
                Games.createGame(id, title, genre, price, developer, dbType);
                break;
            case 2:
                Games.getAllGames(dbType);
                break;
            case 3:
                System.out.print("Enter Game ID: ");
                int gameId = scanner.nextInt();
                System.out.print("Enter New Price: ");
                double newPrice = scanner.nextDouble();
                Games.updateGamePrice(gameId, newPrice, dbType);
                break;
            case 4:
                System.out.print("Enter Game ID to Delete: ");
                int deleteId = scanner.nextInt();
                Games.deleteGame(deleteId, dbType);
                break;
            default:
                System.out.println("❌ Invalid choice.");
        }
    }

    private static void manageTransactions(Scanner scanner) {
        System.out.println("\nTransaction Management:");
        System.out.println("1. Add Transaction");
        System.out.println("2. View Transactions");
        System.out.println("3. Update Transaction Amount");
        System.out.println("4. Delete Transaction");
        int choice = scanner.nextInt();
        scanner.nextLine();

        switch (choice) {
            case 1:
                System.out.print("Enter Transaction ID: ");
                int id = scanner.nextInt();
                System.out.print("Enter User ID: ");
                int userId = scanner.nextInt();
                System.out.print("Enter Game ID: ");
                int gameId = scanner.nextInt();
                System.out.print("Enter Amount: ");
                double amount = scanner.nextDouble();
                Transactions.createTransaction(id, userId, gameId, amount, dbType);
                break;
            case 2:
                Transactions.getAllTransactions(dbType);
                break;
            case 3:
                System.out.print("Enter Transaction ID: ");
                int transactionId = scanner.nextInt();
                System.out.print("Enter New Amount: ");
                double newAmount = scanner.nextDouble();
                Transactions.updateTransactionAmount(transactionId, newAmount, dbType);
                break;
            case 4:
                System.out.print("Enter Transaction ID to Delete: ");
                int deleteId = scanner.nextInt();
                Transactions.deleteTransaction(deleteId, dbType);
                break;
            default:
                System.out.println("❌ Invalid choice.");
        }
    }
}