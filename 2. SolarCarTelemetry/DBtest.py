
import psycopg2


try:
    conn = psycopg2.connect(
         dbname='dd1bpvtvs1alq3',
         user='zfguszkndowgtn',
         password='e41a639c9f4a37a400efbc5940ae418fee0c16f37648522b5f0b1c28abfa7a88',
         host='ec2-54-227-246-152.compute-1.amazonaws.com',
         port='5432')
    print("connected")
    cur = conn.cursor()
except:
    print("I am unable to connect to the database.")
    
    
cur.execute("INSERT INTO public.solardata (latitude, longitude, speed, mainvoltage, auxvolt, current, motortemp,amphours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (10.1, 12.31, 1, 2, 10, 5, 0,4))
conn.commit()