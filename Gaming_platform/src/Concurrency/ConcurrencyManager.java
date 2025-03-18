package Concurrency;
import Transactions.DirtyRead;
import Transactions.LostUpdate;
import Transactions.NonRepeatableRead;
import Transactions.PhantomRead;

public class ConcurrencyManager {


    public static void dirtyReadSimulation(String dbType, String isolationLevel) {
        System.out.println("🔄 Running Dirty Read Simulation with isolation level: " + isolationLevel);
        DirtyRead.simulate(dbType, isolationLevel);
    }


    public static void lostUpdateSimulation(String dbType, String isolationLevel) {
        System.out.println("🔄 Running Lost Update Simulation with isolation level: " + isolationLevel);
        LostUpdate.simulate(dbType, isolationLevel);
    }


    public static void nonRepeatableReadSimulation(String dbType, String isolationLevel) {
        System.out.println("🔄 Running Non-Repeatable Read Simulation with isolation level: " + isolationLevel);
        NonRepeatableRead.simulate(dbType, isolationLevel);
    }


    public static void phantomReadSimulation(String dbType, String isolationLevel) {
        System.out.println("🔄 Running Phantom Read Simulation with isolation level: " + isolationLevel);
        PhantomRead.simulate(dbType, isolationLevel);
    }
}
