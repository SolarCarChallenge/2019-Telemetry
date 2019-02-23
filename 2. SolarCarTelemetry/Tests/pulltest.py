import psycopg2


try:
    conn = psycopg2.connect(
         dbname='your DB name ',
         user='you username',
         password='your password',
         host='ec2-54-227-246-152.compute-1.amazonaws.com',
         port='5432')
    print("connected")
    cur = conn.cursor()
except:
    print("I am unable to connect to the database.")
    

comm="SELECT * from public.solardata"    
cur.execute(comm)
lastrow=cur.rowcount
print(lastrow)

comm=("SELECT * from public.solardata WHERE id = %s" %(lastrow))
print(comm)

cur.execute(comm)
data=cur.fetchone()

print(data)

