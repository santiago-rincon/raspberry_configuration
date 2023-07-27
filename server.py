from modules.http_server import run_server
from modules.firebase import init_firebase

if __name__ == '__main__':
    init_firebase()
    run_server(8080)
    