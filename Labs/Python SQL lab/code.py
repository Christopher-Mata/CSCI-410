import sqlite3

#create a connection to emails.sqlite
conn = sqlite3.connect('emails.sqlite')

#create a database cursor in order to execute SQL statements
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

#use the cursor to create a table named counts with 2 columns: org (TEXT), count(INTEGER)
cur.execute(''' CREATE TABLE Counts (
                org   TEXT,
                count INTEGER
            )''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    
    # extract the orgnization name from the email address
    organization = email.split('@')[1]
    organizationname = organization.split('.')[0]
    
    #use the database cursor to execute a select statement that will return the count of emails for the extracted organization
    cur.execute(''' SELECT count 
                    FROM Counts 
                    WHERE org = ? ''', (organization,))
    
    row = cur.fetchone()
    if row is None:
        '''use the database cursor to execute an insert statement that will insert a new record in table 
           counts for the extracted organization with count 1'''
        cur.execute(''' INSERT INTO Counts (org, count) VALUES (?, 1)''', (organization,))       
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (organization,))
conn.commit()

#use the database cursor to execute a select statement that will return all the records in the table counts then print the results
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')
rows = cur.fetchall()
for row in rows:
    print(str(row[0]), row[1])

cur.close()
