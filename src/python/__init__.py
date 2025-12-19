import configparser
import psycopg2
from sqlalchemy import create_engine, text

def load_db_config(filename="db_config.ini", section="postgresql"):
    config = configparser.ConfigParser()
    config.read(filename)

    if not config.has_section(section):
        raise Exception(f"Section '{section}' not found in {filename}")

    return {key: value for key, value in config.items(section)}

def connect():
    db_config = load_db_config()
    conn = psycopg2.connect(**db_config)
    return conn

if __name__ == "__main__":
    try:
        connection = connect()
        print("Connected to PostgreSQL")
        connection.close()
    except Exception as e:
        print("Error:", e)


def connect_SQL_alchemy():
    params = load_db_config()
    engine = create_engine(
        f"postgresql://{params['user']}:{params['password']}@"
        f"{params['host']}:{params['port']}/"
        f"{params['database']}"
    )
    return engine