import sqlite3

connection = sqlite3.connect('lab3demo.db')

c = connection.cursor()
#akready created table with sensorID, type, zone
c.execute("INSERT INTO sensors VALUES (1, 'door', 'kitchen')")
c.execute("INSERT INTO sensors VALUES (2, 'temperature', 'kitchen')")
c.execute("INSERT INTO sensors VALUES (3, 'door', 'garage')")
c.execute("INSERT INTO sensors VALUES (4, 'motion', 'garage')")
c.execute("INSERT INTO sensors VALUES (5, 'temperature', 'garage')")

connection.commit()

for row in c.execute('SELECT * FROM sensors ORDER BY sensorID'):
    print(row)
    
connection.close()    



