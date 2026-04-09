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

tech_colors = {'NG_boiler':(0.98, 0.4, 0.02),
               'GSHP':    (0.8,0.8,1.0),
               'ASHP':    (0.5,0.5,0.9),
               'E_boiler':(0.01,0.2,0.6),
               'BTES':(0.6,0.0,0.6)}

ssp_colors = {
    'Historical': (0.4, 0.4, 0.4),
    'SSP1-2.6': (30/255, 119/255, 180/255),
    'SSP2-4.5': (81/255, 158/255, 63/255),
    'SSP3-7.0': (238/255, 134/255, 54/255),
    'SSP5-8.5': (196/255, 57/255, 50/255)
}