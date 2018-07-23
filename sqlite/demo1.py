# /usr/bin/env python3
import sqlite3


def convert(value):
    if value.startswith('~'):
        return value.strip('~\n')
    if not value:
        value = '0'
        return float(value)


conn = sqlite3.connect('database.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE user(
id TEXT primary key,
name text,
mobie text
)
 ''')
query = 'INSERT INTO user VALUES (?,?,?)'
field_count = 3
for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    print(vals)
    curs.execute(query, vals)

conn.commit()
conn.close()
