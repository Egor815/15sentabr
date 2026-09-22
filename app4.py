import psycopg

conn = psycopg.connect(
    host="localhost",
    dbname="tracks_db",
    user="postgres",
    password="Admin"
)

cur = conn.cursor()


cur.execute("SELECT * FROM tracks WHERE \"release_year\" > 2015;")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()