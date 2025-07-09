import os
from dotenv import load_dotenv
import pyodbc
import psycopg2
from psycopg2.extras import execute_values

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

# --- SQL Server connection ---
sql_conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('MSSQL_SERVER')};"
    f"DATABASE={os.getenv('MSSQL_DATABASE')};"
    f"UID={os.getenv('MSSQL_USERNAME')};"
    f"PWD={os.getenv('MSSQL_PASSWORD')};"
)
sql_cursor = sql_conn.cursor()

# --- PostgreSQL connection ---
pg_conn = psycopg2.connect(os.getenv("DATABASE_URL"))

# Step 1: Read from SQL Server
sql_cursor.execute("SELECT * FROM vw_DealerCategories")
rows = sql_cursor.fetchall()
columns = [column[0] for column in sql_cursor.description]

# Step 2: Push to PostgreSQL
pg_cursor = pg_conn.cursor()
pg_cursor.execute("TRUNCATE TABLE sales_app.dealer_categories")

insert_query = f"""
    INSERT INTO sales_app.dealer_categories ({', '.join(columns)})
    VALUES %s
"""
execute_values(pg_cursor, insert_query, rows)
pg_conn.commit()

# Cleanup
sql_cursor.close()
pg_cursor.close()
sql_conn.close()
pg_conn.close()

print("✅ Dealer categories pushed to Render PostgreSQL.")
