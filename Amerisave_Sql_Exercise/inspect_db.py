import sqlite3

db_path = "agents.db"
conn = sqlite3.connect(db_path)

conn = sqlite3.connect("agents.db")
cur = conn.cursor()

tables = ["space_travel_agents", "assignment_history", "bookings"]

for table in tables:
    print(f"\n Table: {table}")
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

conn.close()
