import psycopg2
from config import config


def create_tables():
    """ create tables in the NBA database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY,
            name VARCHAR(255),
            city VARCHAR(255),
            nickname VARCHAR(255),
            conference VARCHAR(10),
            division VARCHAR(12),
            abbr VARCHAR(3)
        )
        """,
        """ CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                team_id INTEGER,
                position VARCHAR(5),
                jersey INTEGER,
                height_ft INTEGER,
                height_in INTEGER,
                height_m FLOAT,
                weight_ibs INTEGER,
                weight_kg FLOAT,
                dob_utc DATE,
                draft_round INTEGER,
                draft_pick INTEGER,
                draft_team VARCHAR(255),
                draft_year INTEGER,
                debut_year INTEGER,
                years_pro INTEGER,
                college VARCHAR(255),
                last_affiliation VARCHAR(255),
                country VARCHAR(100),
                teams JSONB,
                is_active BOOLEAN,
                FOREIGN KEY (team_id)
                    REFERENCES teams (team_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
                )
        """,
        """
        CREATE TABLE IF NOT EXISTS coaches (
                coach_id INTEGER PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                team_id INTEGER,
                college VARCHAR(255),
                is_assistant BOOLEAN,
                FOREIGN KEY (team_id)
                    REFERENCES teams (team_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()

        # connect to the PostreSQL server
        print("Connecting to the PostgreSQL database...")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        # create table one by one
        print("Creating tables: ")
        for index, command in enumerate(commands, start=0):
            try:
                cur.execute(command)
                cur.execute("SELECT table_name FROM information_schema.tables where table_schema = 'public'")
                table_name = cur.fetchall()[index]
                print(''.join(table_name) + " was created successfully.")
            except (Exception, psycopg2.ProgrammingError) as perror:
                print(perror)

        # close communication with the PostgreSQL database server
        cur.close()

        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == '__main__':
    create_tables()