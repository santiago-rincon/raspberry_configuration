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

    def close(self):
        self.connection.close()

# --------- Methods used to interact with Firebase --> Local ---------

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
        collections = {"temp" : "Temperatura", "ha": "Humedad", "hs": "HumedadS", "co2": "CO2", "rad": "Rad"}
        for key,value in collections.items():
            query = f"UPDATE thresholds SET umbral={new_thresholds[value]} WHERE variable='{key}'"
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print("Datos actualizados correctamente")
            except Exception as e:
                print("Error: ",str(e))
                return None

    def get_all_macs(self):
        query = "SELECT mac FROM nodes;"
        try:
            self.cursor.execute(query)
            macs = self.cursor.fetchall()
            return macs
        except Exception as e:
            print("Error: ",str(e))
            return None
        
    def get_all_ids(self):
        query = "SELECT nodeId FROM nodes;"
        try:
            self.cursor.execute(query)
            ids = self.cursor.fetchall()
            return ids
        except Exception as e:
            print("Error: ",str(e))
            return None
    
    def add_node(self, macs, new_node, id_firebase):
        if new_node['mac'] not in macs:
                try:
                    query = f"INSERT INTO nodes(mac,nodeId,nodeStatus,latitude,longitude,id_firebase) values('{new_node['mac']}',{new_node['nodeId']}, {new_node['nodeStatus']}, {new_node['latitude']}, {new_node['longitude']}, '{id_firebase}');"
                    self.cursor.execute(query)
                    self.connection.commit()
                    print(f"Nodo agregado correctamente ({new_node['mac']})")        
                except Exception as e:
                    print("Error: ",str(e))

    def update_node(self, id_firebase, update_node):
        try:
            query = f"UPDATE nodes SET nodeStatus={update_node['nodeStatus']}, mac='{update_node['mac']}', nodeId={update_node['nodeId']}, latitude={update_node['latitude']}, longitude={update_node['longitude']}  WHERE id_firebase='{id_firebase}';"
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Nodo actualizado correctamente ({update_node['mac']})")
        except Exception as e:
            print("Error: ",str(e)) 

    def delete_node(self, id_firebase):
        query = f"DELETE FROM nodes WHERE id_firebase = '{id_firebase}';"
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Nodo eliminado correctamente")
        except Exception as e:
            print("Error: ",str(e))
            return None

# --------- Methods used to interact with Local --> Firebase ---------

    def get_local_nodes(self):
        query = "SELECT * FROM nodes ORDER BY nodeId ASC;"
        try:
            self.cursor.execute(query)
            nodes = self.cursor.fetchall()
            return nodes
        except Exception as e:
            print("Error: ",str(e))
            return None
        
    def get_all_id(self):
        query = "SELECT nodeId FROM nodes;"
        try:
            self.cursor.execute(query)
            ids = self.cursor.fetchall()
            return ids
        except Exception as e:
            print("Error: ",str(e))
            return None
        
    def get_local_node(self, id_firebase):
        query = f"SELECT * FROM nodes WHERE id_firebase = '{id_firebase}';"
        try:
            self.cursor.execute(query)
            node = self.cursor.fetchone()
            return node
        except Exception as e:
            print("Error: ",str(e))
            return None
    
    def get_local_variables(self):
        query = "SELECT * FROM thresholds;"
        try:
            self.cursor.execute(query)
            node = self.cursor.fetchall()
            return node
        except Exception as e:
            print("Error: ",str(e))
            return None
    
    def get_local_intervals(self):
        query = "SELECT minutes FROM intervals;"
        try:
            self.cursor.execute(query)
            interval = self.cursor.fetchone()
            return interval[0]
        except Exception as e:
            print("Error: ",str(e))
            return None