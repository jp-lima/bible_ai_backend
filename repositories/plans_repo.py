from db import get_conn


def get_all_plans():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM plans")
    plans = cursor.fetchall()

    cursor.close()
    conn.close()

    return plans


def get_plan_by_id(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM plans WHERE id = %s", (uuid,))
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users












