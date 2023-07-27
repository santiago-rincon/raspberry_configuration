import mysql.connector as mariadb

class Database:
    def __init__(self):
        self.connection = mariadb.connect(
            host='192.168.1.3', 
            user='raspberry', 
            password='raspberry', 
            database='nodos'
        )
        self.cursor = self.connection.cursor()

    def search_node(self,mac):
        query = f"SELECT nodeId FROM nodes WHERE mac = '{mac}';"
        try:
            self.cursor.execute(query)
            nodes = self.cursor.fetchone()
            return nodes[0]
        except Exception as e:
            print("Error: ",str(e))
            return None
    
    def update_intervals(self,new_interval):
        query = f"UPDATE intervals SET minutes={new_interval};"
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Datos actualizados correctamente")
        except Exception as e:
            print("Error: ",str(e))
            return None
        
    def update_thresholds(self,new_thresholds):
        collections = {"temp" : "Temperatura", "ha": "HumedadA", "hs": "HumedadS", "co2": "CO2", "rad": "Rad"}
        for key,value in collections.items():
            query = f"UPDATE thresholds SET umbral={new_thresholds[value]} WHERE variable='{key}'"
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print("Datos actualizados correctamente")
            except Exception as e:
                print("Error: ",str(e))
                return None

    def close(self):
        self.connection.close()