from db import get_conn

def get_one_wallet_by_uuid(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM credit_wallet WHERE user_id = %s", (uuid,))
    wallet = cursor.fetchall()

    cursor.close()
    conn.close()

    return wallet   


def get_all_wallets():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM credit_wallet")
    wallets = cursor.fetchall()

    cursor.close()
    conn.close()

    return wallets




def create_new_wallet(uuid:str, user_id:str, balance:int, cycle_started_at:str, cycle_finish_at:str, updated_at:str, created_at:str ):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO credit_wallet 
        (id, user_id, balance, cycle_started_at, cycle_finish_at, updated_at, created_at )
    VALUES 
        (%s, %s, %s , %s, %s, %s, %s )
    ''',
    (uuid, user_id, balance, cycle_started_at, cycle_finish_at, updated_at, created_at)
    )

    conn.commit()

    cursor.close()
    conn.close()

def put_value_in_wallet_by_user_id(new_value:int, id:str):        

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)


    cursor.execute('''
   UPDATE credit_wallet SET     
        balance = %s

    WHERE user_id = %s
    ''',
    (new_value, id)


    )


    conn.commit()
     
    cursor.close()
    conn.close()








