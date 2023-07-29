import pytz
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timezone
from modules.database import Database

def init_firebase():
    # Inicialización la aplicación de Firebase con archivo de credenciales
    cred = credentials.Certificate("modules/credentials.json")
    firebase_admin.initialize_app(cred)

# Envío de datos
def send_data(mac, data):
    # Array de retorno con reporte
    report = []
    # Obtención de una referencia a la base de datos Firestore
    db = firestore.client()
    # Establacimiento de la hora actual
    now= datetime.now(timezone.utc).astimezone(pytz.timezone('America/Bogota'))
    # Diccionario de colecciones de Firebase
    collections = {"temp" : "Temperatura", "ha": "HumedadA", "hs": "HumedadS", "co2": "CO2", "rad": "Rad"}
    # Buscando el id del nodo según la mac
    database = Database()
    node_id = database.search_node(mac.lower())
    # Validación de la existencia del nodo
    if node_id is not None:
        # Recorrido de la data enviada por los nodos
        for key,value in data.items():
            # Obtención de la colección correspondiente a la medida
            collection  = collections.get(key, None)
            if collection is not None:
                # Datos para subir a Firebase
                data_to_firebase={
                    'dateAndTime': now,
                    'measure': value,
                    'node': node_id
                }
                # Intento de subida de datos
                try:
                    db.collection(collection).document().set(data_to_firebase)
                    print('Datos subidos correctamente')
                    report.append((key, True))
                except Exception as e:
                    print("Error:", str(e))
                    report.append((key, False))
            else :
                report.append((key, False))
    database.close()
    return report

def delete_node(id):
    db = firestore.client()
    try:
        # Eliminar el documento
        db.collection('Nodos').document(id).delete()
        print(f"Documento eliminado correctamente.")
        return True
    except Exception as e:
        print(f"Error al eliminar el documento: {e}")
        return False

def add_new_node(data):
    db = firestore.client()
    try:
        # Añadir el nuevo documento a la colección y obtener su ID asignado
        new_node = db.collection('Nodos').add(data) 
        id = new_node[1].id
        print(f"Nuevo documento agregado con ID: {id}")
        return True
    except Exception as e:
        print(f"Error al añadir el nuevo documento: {e}")
        return False

def update_node(id, data):
    db = firestore.client()
    try:
        # Actualizar el documento
        db.collection('Nodos').document(id).update(data)
        print(f"Documento actualizado correctamente.")
        return True
    except Exception as e:
        print(f"Error al actualizar el documento: {e}")
        return False

def start_listeners():
    db = firestore.client()
    nodes = db.collection('Nodos')
    thresholds  = db.collection('Umbrales')
    intervals  =db.collection('Umbrales/yB1NAzpx0V3m5BfLzuEJ/interval')
    nodes.on_snapshot(_nodes_changes)
    thresholds.on_snapshot(_thresholds)
    intervals.on_snapshot(_intervals)

# Define la función callback que se ejecutará cuando haya cambios
def _nodes_changes(col_snapshot, changes, read_time):
    print("Cambio en la colección de nodos")
    database= Database()
    macs_tuple = database.get_all_macs()
    macs = []
    for mac in macs_tuple:
        macs.append(mac[0].lower())
    for change in changes:
        if change.type.name == "ADDED":
            database.add_node(macs, change.document.to_dict(), change.document.id)
            database.close()
        elif change.type.name == "MODIFIED":
            database.update_node(change.document.id,change.document.to_dict())
            database.close()
        elif change.type.name == "REMOVED":
            database.delete_node(change.document.id)
            database.close()

def _thresholds(col_snapshot, changes, read_time):
    print("Cambio en la colección de umbrales")
    for change in changes:
        if change.type.name == "MODIFIED":
            database = Database()
            new_threshold = change.document.to_dict()
            database.update_thresholds(new_threshold)
            database.close()

def _intervals(col_snapshot, changes, read_time):
    print("Cambio en la colección de intervalos")
    for change in changes:
        if change.type.name == "MODIFIED":
            database = Database()
            new_interval = change.document.to_dict()
            database.update_intervals(new_interval["minutes"])
            database.close()