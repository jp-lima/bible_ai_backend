from datetime import date, datetime
from locale import windows_locale
from db import get_conn


def create_row_analitycs_users(datetime:str, users_online:int, sales_mades:int, new_users:int):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
    '''
    INSERT INTO analitycs_users_activity
        (datetime, users_online, sales_mades, new_users)
    VALUES 
        (%s,%s,%s, %s)
    ''',
    (datetime, users_online, sales_mades, new_users)
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_all_rows_from_analitycs_users():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM analitycs_users_activity")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

def put_row_from_analitycs_users(users_online:int, sales_mades:int, datetime:str, new_users:int ):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
    '''
    UPDATE analitycs_users_activity SET
     users_online = %s,
     sales_mades = %s,
     new_users = %s
    WHERE datetime = %s 
    ''',
    ( users_online, sales_mades,new_users, datetime,)
    )

    conn.commit()
    cursor.close()
    conn.close()







