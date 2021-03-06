import sqlite3


class DBConnector():  # Writes into the database very simple

    # Inserts the measurement data into the database
    def database_insert_measurement(self, measurement):
        connection = sqlite3.connect('/home/pi/triops.db')
        cursor = connection.cursor()
        cursor.execute("""
            insert into measurement (
                DateTime,
                temperature_C,
                temperature_F,
                temperature_K)
            VALUES (?,?,?,?)""", measurement)
        connection.commit()
        connection.close()
