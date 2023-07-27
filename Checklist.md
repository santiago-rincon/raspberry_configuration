- [ ] Crear servidor que suba los datos mediante Python
- [ ] Identificar nodo mediante base de datos
- [ ] CRUD en la base de datos
- [ ] Interfaz gráfica vinculado con la base de datos de manera bidireccional
- [ ] Actualizar base de datos al recibir un cambio
- [ ] Enviar alerta por SMS cuando el umbral sea superado
- [ ] Establecer la Raspberry en modo router
- [ ] Usar la interfaz GSM para salida a internet
- [ ] Enviar pulso por el transector
## Credenciales sistema
- **Usuario:** raspberry
- **Password:** raspberry
- **Usuario:** root
- **Password:** raspberry
- **Usuario:** raspberry (Mariadb)
- **Password:** raspberry (Mariadb)
## Sintaxis curl 
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
