import psycopg2
from config import config

def delete(part_id):
    conn = None
    rows_deleted = 0

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        rows_deleted = cur.rowcount

        conn.commit()
        cur.close()
    except psycopg2.DatabaseError as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted