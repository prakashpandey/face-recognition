import mysql.connector 
import time


def connect(host, username, password, database): 
    try: 
        connection = mysql.connector.connect(host=host, database=database, user=username, password=password)
        print(f"Successfully connected to { host } ") 
        return connection
    except mysql.connector.Error as e: 
        print(str(e)) 

def save_detection_activity(connection):
        timestamp = int(time.time())

        try: 
            sql = "INSERT INTO face_recognition.face_activity(time) VALUES ('%s' )"  % (timestamp)
            cursor = connection.cursor() 
            cursor.execute(sql) 
            connection.commit()
            print("Saved face activity to database.")
        except Exception as e:
            error = str(e)
            print(f"Error while inserting into face_activity, Error: { error }.")           


if __name__ == "__main__":
    connection = connect(host = "localhost", username = "root", password = "root", database = "face_recognition")
    save_detection_activity(connection)
