import mysql.connector
from mysql.connector import Error, pooling
import psycopg2
from psycopg2 import pool

class DatabaseConnection:
    _connection_pool = None
    _db_type = None
    @staticmethod
    def initialize(db_type):
        if DatabaseConnection._connection_pool is None:
            DatabaseConnection._db_type = db_type
            try:
                if db_type == "mysql":
                    DatabaseConnection._connection_pool = pooling.MySQLConnectionPool(
                        pool_name="mypool",
                        pool_size=10,
                        host="localhost",
                        database="gaming_platform",
                        user="root",
                        password="password"
                    )
                    print("✅ Pool-ul of connection from MySQL was initialized!")
                elif db_type == "postgres":
                    DatabaseConnection._connection_pool = pool.SimpleConnectionPool(
                        minconn=1,
                        maxconn=10,
                        host="localhost",
                        database="gaming_platform",
                        user="postgres",
                        password="1111"
                    )
                    print("✅ Pool-ul  of connection from PostgreSQL was initialized!")
                else:
                    print("❌ The database type is unknown")
            except Exception as e:
                print(f"❌ Error initializing pool: {e}")
                raise

    @staticmethod
    def get_connection():

        if DatabaseConnection._connection_pool is None:
            raise Exception("⚠️ Connection was not initialized.")
        try:
            return DatabaseConnection._connection_pool.getconn()
        except Exception as e:
            print(f"❌ Error getting the connection {e}")
            raise

    @staticmethod
    def return_connection(connection):

        if connection:
            if DatabaseConnection._db_type == "mysql":
                connection.close()
            elif DatabaseConnection._db_type == "postgres":
                DatabaseConnection._connection_pool.putconn(connection)
            print("🔌 The connection was returned in the pool!")

    @staticmethod
    def close_all_connections():

        if DatabaseConnection._connection_pool:
            if DatabaseConnection._db_type == "mysql":
                print("🔌 Manual close of pool in MySQL.")
            elif DatabaseConnection._db_type == "postgres":
                DatabaseConnection._connection_pool.closeall()
            print("🔌 All connections are closed.")
