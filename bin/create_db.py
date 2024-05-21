import duckdb

# Connect to your DuckDB database (it will create a new one if it doesn't exist)
conn = duckdb.connect('data/task_pom.db')

# SQL script to create the sequence and table
create_sql = """
-- Create the sequence
CREATE SEQUENCE IF NOT EXISTS task_pom_id_seq;

-- Main Table
CREATE TABLE IF NOT EXISTS task_pom (
    id INTEGER DEFAULT nextval('task_pom_id_seq'),
    file_name VARCHAR,
    start_time TEXT,
    end_time TEXT,
    comment TEXT,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

# Execute the SQL script
conn.execute(create_sql)

# Verify the creation by listing the tables
tables = conn.execute("SHOW TABLES;").fetchall()
print("Tables in the database:", tables)

# Close the connection
conn.close()

