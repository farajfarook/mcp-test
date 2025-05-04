import psycopg
from contextlib import contextmanager

# Connection details from docker-compose.yml
DB_NAME = "ragdb"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"

# Construct the connection string
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


@contextmanager
def get_db_connection():
    """Provides a database connection using a context manager."""
    conn = None
    try:
        conn = psycopg.connect(DATABASE_URL)
        yield conn
    except psycopg.OperationalError as e:
        print(f"Database connection error: {e}")
        # Consider more specific error handling or re-raising
        raise
    finally:
        if conn:
            conn.close()


def execute_query(query: str, params: tuple = None):
    """Executes a given SQL query with optional parameters."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()


def fetch_all(query: str, params: tuple = None) -> list:
    """Executes a query and fetches all results."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            results = cur.fetchall()
            return results


def fetch_one(query: str, params: tuple = None) -> tuple | None:
    """Executes a query and fetches the first result."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            result = cur.fetchone()
            return result


# Example usage (optional, can be removed or placed in main.py)
if __name__ == "__main__":
    try:
        # Example: Create a dummy table and insert data
        print("Attempting to create table...")
        execute_query(
            "CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));"
        )
        print("Table created or already exists.")

        print("Attempting to insert data...")
        execute_query("INSERT INTO test_table (name) VALUES (%s);", ("Test Name",))
        print("Data inserted.")

        print("Fetching all data...")
        all_data = fetch_all("SELECT * FROM test_table;")
        print("All data:", all_data)

        print("Fetching one row...")
        one_row = fetch_one("SELECT * FROM test_table WHERE name = %s;", ("Test Name",))
        print("One row:", one_row)

        print("Fetching candidate names...")
        candidate_names = fetch_all("SELECT name FROM candidates;")
        print("Candidate names:", candidate_names)

    except Exception as e:
        print(f"An error occurred during database operations: {e}")
