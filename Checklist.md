- [x] Crear servidor que suba los datos mediante Python
- [x] Identificar nodo mediante base de datos
- [x] CRUD en la base de datos desde Firebase a la local
- [x] Interfaz gráfica vinculado con la base de datos de manera bidireccional
- [x] Actualizar base de datos al recibir un cambio
- [x] Enviar alerta por SMS cuando el umbral sea superado
- [x] Establecer la Raspberry en modo router
- [ ] Usar la interfaz GSM para salida a internet
- [ ] Enviar pulso por el transector
## Credenciales sistema
- **Usuario:** raspberry
- **Password:** raspberry
- **Usuario:** root
- **Password:** raspberry
- **Usuario:** raspberry (Mariadb)
- **Password:** raspberry (Mariadb)
- **Usuario:** root (Mariadb)
- **Password:** raspberry (Mariadb)
- **AP:** RaspberryAP (192.168.20.1/24)
- **Password:** raspberry
## Sintaxis curl para envío de datos 
- Windows
```bash
curl -X POST -H "Content-Type: application/json" -d '{"""Name""":"""Test Value"""}' http://192.168.1.7:8080
```
- Linux
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Juan", "age": 30}' http://192.168.1.7:8080
```
## Estructura de envío de datos
```json
{
	"mac": "string",
	"temp": number,
	"ha": number,
	"hs": number,
	"rad": number,
	"co2": number,
}
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"mac": "ae:58:ff:d5:c1:55", "temp":25.6, "ha":50.36, "hs": 72.98, "rad":150.25, "co2":600}' http://192.168.1.7:8080
```

## Instalación de dependencias

### Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### Motor de base de datos

```bash
sudo apt install mariadb-server
```

### Librerías de Python

```python
pip install pytz firebase_admin mysql-connector-python twilio python-crontab
```
## Configuración de mariadb
1. Instalación segura
```bash
sudo mysql_secure_installation
```

2. Creación de la base de datos
```sql
CREATE DATABASE <dbname>;
CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON <dbname>.* TO '<username>'@'%';
FLUSH PRIVILEGES;
```
- **dbname:** proyecto
- **username:** raspberry
- **password:** raspberry

3. Importación de las tablas a la base de datos.
```bash
mariadb <usuername> -p <dbmane> < nodos.sql
```

4. Habilitar el servicio SQL en la red local (Reemplazar 127.0.0.1 por 0.0.0.0)
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

5. Actualizar permisos del usuario (si se creo erroneamente)
```mysql
RENAME USER '<username>'@'localhost' TO '<username>'@'%';
FLUSH PRIVILEGES;
```
## Configuración del modo router ([raspAP](https://raspap.com/))

1. Actualización del sistema 
```bash
sudo apt-get update
sudo apt-get full-upgrade
sudo reboot
```

 2. Instalación de dependencias
```bash
curl -sL https://install.raspap.com | bash
```

3. Credenciales por defecto
**IP address:** 10.3.141.1
**Username:** admin
**Password:** secret
**DHCP range:** 10.3.141.50 — 10.3.141.254
**SSID:** raspi-webgui
**Password:** ChangeMe

4. Cambio de credenciales
**IP address:** 192.168.20.1/24
**Username:** raspberry
**Password:** raspberry
**DHCP range:** 192.168.20.2 - 192.168.20.30
**SSID:** RaspberryAP
**Password:** raspberry


