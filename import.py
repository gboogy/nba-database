import psycopg2
import api as nba_api
from config import config


def insert_team_to_db():
    """ Inserts a new team to the database """
    insert_team_query = """
         INSERT INTO teams (
             team_id,
             name,
             city,
             nickname,
             conference,
             division,
             abbr)
         VALUES (%s, %s, %s, %s, %s, %s, %s)
         ON CONFLICT (team_id)
         DO UPDATE
         SET
            name = EXCLUDED.name,
            city = EXCLUDED.city,
            nickname = EXCLUDED.nickname,
            conference = EXCLUDED.conference,
            division = EXCLUDED.division,
            abbr = EXCLUDED.abbr;
         """
    rows = nba_api.get_teams()
    conn = None
    count = 0

    try:
        params = config()
        print("Connecting to the NBA database...")
        conn = psycopg2.connect(**params)
        print("Inserting records into TEAMS table...: ")
        gen_list = list(nba_api.get_teams())
        expected_records = len(gen_list)
        print("Expected # of records: " + str(expected_records))

        cur = conn.cursor()
        for row in rows:
            row = tuple(row.values())
            cur.execute(insert_team_query, row)
            conn.commit()
            count += 1
        print("Total # of records inserted: " + str(count))
        cur.close()
        print('Finished loading TEAMS table.')
        conn.close()
        print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print("** " + str(error) + " **")
    finally:
        if conn is not None:
            conn.close()


def insert_player_to_db():
    """ Inserts players to the database """
    insert_player_query = """
         INSERT INTO players (
             player_id,
             first_name,
             last_name,
             team_id,
             position,
             jersey,
             height_ft,
             height_in,
             height_m,
             weight_ibs,
             weight_kg,
             dob_utc,
             draft_round,
             draft_pick,
             draft_team,
             draft_year,
             debut_year,
             years_pro,
             college,
             last_affiliation,
             country,
             teams,
             is_active)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         ON CONFLICT (player_id)
         DO UPDATE
            SET
                first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name,
                team_id = EXCLUDED.team_id,
                position = EXCLUDED.position,
                jersey = EXCLUDED.jersey,
                height_ft = EXCLUDED.height_ft,
                height_in = EXCLUDED.height_in,
                height_m = EXCLUDED.height_m,
                weight_ibs = EXCLUDED.weight_ibs,
                weight_kg = EXCLUDED.weight_kg,
                dob_utc = EXCLUDED.dob_utc,
                draft_round = EXCLUDED.draft_round,
                draft_pick = EXCLUDED.draft_pick,
                draft_team = EXCLUDED.draft_team,
                draft_year = EXCLUDED.draft_year,
                debut_year = EXCLUDED.debut_year,
                years_pro = EXCLUDED.years_pro,
                college = EXCLUDED.college,
                last_affiliation = EXCLUDED.last_affiliation,
                country = EXCLUDED.country,
                teams = EXCLUDED.teams,
                is_active = EXCLUDED.is_active;
         """

    conn = None
    row_count = 0
    rows = nba_api.get_players()
    try:
        params = config()
        print("Connecting to the NBA database...")
        conn = psycopg2.connect(**params)
        print("Inserting records into PLAYERS table...: ")
        gen_list = list(nba_api.get_players())
        expected_records = len(gen_list)
        print("Expected # of records: " + str(expected_records))

        cur = conn.cursor()
        for row in rows:
            row = tuple(row.values())
            cur.execute(insert_player_query, row)
            row_count += 1
            conn.commit()
        print("Total # of records inserted: " + str(row_count))
        cur.close()
        print('Finished loading TEAMS table')
        conn.close()
        print("Database connection closed.")
    except (Exception, psycopg2.DatabaseError) as error:
        print("** " + str(error) + " **")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


def insert_coach_to_db():
    """ Inserts a new coach to the database """
    insert_coach_query = """
         INSERT INTO coaches (
             coach_id,
             first_name,
             last_name,
             team_id,
             college,
             is_assistant)
         VALUES (%s, %s, %s, %s, %s, %s)
         ON CONFLICT (coach_id)
         DO UPDATE
         SET
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            team_id = EXCLUDED.team_id,
            college = EXCLUDED.college,
            is_assistant = EXCLUDED.is_assistant;
         """
    rows = nba_api.get_coaches()
    conn = None
    row_count = 0

    try:
        params = config()
        print("Connecting to the NBA database...")
        conn = psycopg2.connect(**params)
        print("Inserting records into COACHES table...: ")
        gen_list = list(nba_api.get_coaches())
        expected_records = len(gen_list)
        print("Expected # of records: " + str(expected_records))

        cur = conn.cursor()
        for row in rows:
            row = tuple(row.values())
            cur.execute(insert_coach_query, row)
            conn.commit()
            row_count += 1
        print("Total # of records inserted: " + str(row_count))
        cur.close()
        print('Finished loading COACHES table.')
        conn.close()
        print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print("** " + str(error) + " **")
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    insert_team_to_db()
    insert_player_to_db()
    insert_coach_to_db()