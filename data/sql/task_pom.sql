-- Version 0.1
-- Create the sequence
CREATE SEQUENCE task_pom_id_seq;

-- Main Table

CREATE TABLE task_pom (
    id INTEGER DEFAULT nextval('task_pom_id_seq'),
    file_name VARCHAR,
    start_time TEXT,
    end_time TEXT,
    duration INTEGER,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comment TEXT
)

