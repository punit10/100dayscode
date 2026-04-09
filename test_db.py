import psycopg

user = ""
password = ""
conn = psycopg.connect(
    host="xxxx.us-east-1.rds.amazonaws.com",
    dbname="postgres",
    user=user,
    password=password,
    port=5432,
    connect_timeout=5
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("Version")
print(cur.fetchone())

conn.close()
