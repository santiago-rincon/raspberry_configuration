from modules.firebase import init_firebase, start_listeners

# Inicialización la aplicación de Firebase
init_firebase()
# Creación del listener para la colección de nodos
start_listeners()

try: 
    while True:
        pass
except KeyboardInterrupt:
    print("\nSaliendo...\n")