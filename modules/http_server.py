from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from modules.firebase import send_data

# Definimos un manejador personalizado para el servidor
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # Intentamos parsear el JSON recibido
        try:
            # Extrallendo los datos y la mac
            data = json.loads(post_data)
            mac = data.pop("mac")
            # Enviando los datos a Firebase
            reports = send_data(mac,data)
            # Verificación del reporte de envío de datos a Firebase
            response_message = ""
            for report in reports:
                if not report[1]: 
                    response_message += f"Error en el dato {report[0]}. "
                    response_status = 500
            if len(response_message) == 0 and len(reports) > 0:
                response_message = "Datos enviados correctamente"
                response_status = 200
            else:
                response_message = "Dirección MAC no encontrada"
                response_status = 400
        # Manejo de errores
        except json.JSONDecodeError as e:
            response_message = f"Error al parsear JSON: {str(e)}"
            response_status = 400
        # Envío de respuesta
        self.send_response(response_status)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))

# Función para levantar el servidor
def run_server(port):
    host = '0.0.0.0'
    port = port
    server_address = (host, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Servidor iniciado en http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Servidor detenido.")