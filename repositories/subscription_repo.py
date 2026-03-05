from db import get_conn
from models import user


def create_row_subscription(uuid:str, user_id:str, plan_id:str,status:str ,next_billing_date:str, payment_provider_id:str, created_at:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
    '''
    INSERT INTO subscriptions  
        (id, user_id, plan_id, status, next_billing_date, payment_provider_id, created_at)
    VALUES 
        (%s, %s, %s, %s, %s, %s, %s )
    ''',
    (uuid, user_id, plan_id, status, next_billing_date, payment_provider_id, created_at)
    )

    conn.commit()

    cursor.close()
    conn.close()


def put_subscription_by_payment_id(payment_provider_id, status):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
        UPDATE subscriptions SET
            status = %s     

    WHERE payment_provider_id = %s 
     ''',
    (status, payment_provider_id)
 )

    conn.commit()

    cursor.close()
    conn.close()






