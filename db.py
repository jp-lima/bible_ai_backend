from mysql.connector import pooling

db_pool = pooling.MySQLConnectionPool(
    pool_name = "bible_ai",
    pool_size = 5,  
    host = "srv1922.hstgr.io",
    password="databaseAI@@1",
    user="u670476727_joaopedro",
    database="u670476727_bible_ai",
    port=3306
)

def get_conn():
    return db_pool.get_connection()

