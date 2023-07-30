- [x] Crear servidor que suba los datos mediante Python
- [x] Identificar nodo mediante base de datos
- [x] CRUD en la base de datos desde Firebase a la local
- [x] Interfaz gráfica vinculado con la base de datos de manera bidireccional
- [x] Actualizar base de datos al recibir un cambio
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

```bash
curl -X POST -H "Content-Type: application/json" -d '{"mac": "ae:58:ff:d5:c1:55", "temp":25.6, "ha":50.36, "hs": 72.98, "rad":150.25, "co2":600}' http://192.168.1.7:8080
```
