import mysql.connector 
import time

class DatabaseManager(object): 
    
    connection = None 

    def __init__(self): 
        self.connect("52.172.31.113", "root", "nJWYdBpv5J", "visitorMgmt")

    def connect(self, host, username, password, db): 
        try: 
            DatabaseManager.connection = mysql.connector.connect(host=host, database=db, user=username, password=password)
            print(f"Successfully connected to { host } ") 
        except mysql.connector.Error as e: 
            print(str(e)) 

    def save_detection_activity(self):
        timestamp = int(time.time())

        try: 
            sql = "INSERT INTO face_activity(time, version) VALUES ('%d', '%d' )"  % (timestamp, 0)
            cursor = DatabaseManager.connection.cursor() 
            cursor.execute(sql) 
            DatabaseManager.connection.commit()
            print("Saved face activity to database.")
        except Exception as e:
            error = str(e)
            print(f"Error while inserting into face_activity, Error: { error }.")             


    def increment_total_detection(self):
        sql = "update total_people_detected set count=count+1 where id=1;" 
        try: 
            cursor = DatabaseManager.connection.cursor() 
            cursor.execute(sql)    
            print("Incrementing total people detected.")  
        except Exception as e:
            error = str(e)
            print(f"Error while inserting into total_people_detected, Error: { error }.")          


