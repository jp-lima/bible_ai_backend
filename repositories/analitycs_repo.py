from db import get_conn
from models import user



def create_row_of_analitycs(year:str, mounth:str, day:str, hour:str, orders_count:int, revenue:float, new_users:int, users_online:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO analitycs_users_activity 
        (year, month, day, time ,orders_count, revenue, new_users, users_online)
    VALUES 
        (%s,%s,%s,%s,%s, %s, %s, %s)
    ''',
    (year,mounth,day,hour ,orders_count, revenue, new_users, users_online )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_rows_of_analitycs():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM analitycs_users_activity")
    datas = cursor.fetchall()

    cursor.close()
    conn.close()

    return datas

def put_row_of_analityc(year:str, mounth:str, day:str, hour:str, orders_count:int, revenue:float, new_users:int, users_online:int):

    conn = get_conn()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
     UPDATE analitycs_users_activity SET 
        orders_count = %s,
        revenue = %s, 
        new_users = %s,
        users_online = %s
       WHERE
       year = %s AND
       month = %s AND
       time = %s AND
       day = %s
    ''',
    ( orders_count, revenue, new_users,users_online, year,mounth, hour,day)
    )

    conn.commit()

    cursor.close()
    conn.close()




