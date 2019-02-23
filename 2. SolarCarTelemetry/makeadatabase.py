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
    
commands= "DROP TABLE solardata"
cur.execute(commands)

commands="CREATE OR REPLACE FUNCTION trigger_set_timestamp() RETURNS TRIGGER AS $$ BEGIN NEW.updated_at = NOW(); RETURN NEW; END; $$ LANGUAGE plpgsql;"
cur.execute(commands)

commands= '''CREATE TABLE solardata (id SERIAL PRIMARY KEY,
     created_at TIMESTAMP NOT NULL DEFAULT NOW(),
     datetime TEXT NULL, 
     latitude DECIMAL NULL,
     Longitude DECIMAL NULL, 
     speed DECIMAL NULL, 
     mainvoltage DECIMAL, 
     auxvolt DECIMAL, 
     current DECIMAL, 
     motortemp DECIMAL, 
     amphours DECIMAL)'''   
cur.execute(commands)


cur.close()
conn.commit()
conn.close()