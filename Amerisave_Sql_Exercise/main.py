import sqlite3
import json

# Load input
with open('input.json') as f:
    customer = json.load(f)

# SQL
with open('matched_assignments.sql') as f:
    sql_query = f.read()

# Connect
conn = sqlite3.connect('agents.db')
cursor = conn.cursor()

cursor.execute(sql_query, customer)

results = cursor.fetchall()
for row in results:
    print(row)
