from db import get_conn




def post_new_wallet(uuid:str, user_id:str, balance:int, cycle_started_at:str, cycle_finish_at:str, updated_at:str, created_at:str ):

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO users 
        (id, user_id, balance, cycle_started_at, cycle_finish_at, updated_at, created_at )
    VALUES 
        (%s, %s, %s , %s, %s, %s, %s )
    ''',
    (uuid, user_id, balance, cycle_started_at, cycle_finish_at, updated_at, created_at)
    )

    conn.commit()

    cursor.close()
    conn.close()


