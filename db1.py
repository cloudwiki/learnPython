import sqlite3

con = sqlite3.connect(r'c:\Users\meng_\Programs\sqllite3\data\test.db')

cur = con.cursor()
#truncate table
cur.execute('delete from person')
con.commit()
        
insert_many = r'insert into person values (?, ?, ?)'

person_entries = [(x, 'test_first_'+repr(x), 'test_last_'+repr(x)) for x in range(20)]

cur.executemany(insert_many, person_entries)


cur.execute('select * from person')
cols = [f[0] for f in cur.description]
for row in cur.fetchall():
    for pair in zip(cols, row):
        print '%s: %s' % pair
        print

cur.execute('select * from person')
cols = [f[0] for f in cur.description]
row = cur.fetchone()
while row:
    for pair in zip(cols, row):
        print '%s: %s' % pair
        print
    print '*'*25  
    row = cur.fetchone()
                
        
con.commit()
con.close()