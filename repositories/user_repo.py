from db import get_conn


def get_user_by_id(uuid:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id = %s", (uuid,))
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


def get_all_users():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def get_user_by_email(email: str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s LIMIT 1",(email,))
    users = cursor.fetchone()

    cursor.close()
    conn.close()
    return users

def post_new_user(uuid:str, name:str, email:str, password_hash:str, created_at:str,phone:str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    '''
    INSERT INTO users 
        (id, name, email, password_hash, created_at, role, status, phone)
    VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s)
    ''',
    (uuid, name, email, password_hash, created_at, "user", "offline", phone)
    )

    conn.commit()

    cursor.close()
    conn.close()

def del_user(uuid:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
    DELETE FROM users
    WHERE id = %s 
    ''',
    (uuid,)
 )

    conn.commit()

    cursor.close()
    conn.close()

def put_user(username:str,phone:str,email:str, password_hashed:str, user_id:str):
    conn = get_conn()

    cursor = conn.cursor(dictionary = True)

    cursor.execute( '''
        UPDATE users SET
        name = %s,
        phone = %s, 
        email = %s,
        password_hash = %s
    WHERE id = %s 
     ''',
    (username, phone, email,password_hashed, user_id)
 )

    conn.commit()

    cursor.close()
    conn.close()


    






