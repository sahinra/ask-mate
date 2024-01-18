import psycopg2
import os
from psycopg2 import extras


def make_connection():
    try:
        conn = psycopg2.connect(
            database=os.environ.get("PSQL_DB_NAME"),
            user=os.environ.get("PSQL_USER"),
            password=os.environ.get("PSQL_PASSWORD"),
            port=os.environ.get("PSQL_PORT"),
            host=os.environ.get("PSQL_HOST")
        )
    except psycopg2.DatabaseError as ex:
        print("Connection error occurred.")
        raise ex
    conn.autocommit = True
    return conn


def handle_connection():
    conn = make_connection()
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    cursor.execute("SELECT * FROM questions")
    result = cursor.fetchall()
    print("Questions\n", result)


if __name__ == "__main__":
    handle_connection()