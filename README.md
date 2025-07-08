# Flask + RabbitMQ: API para recepción de hechos delictivos

Este proyecto es una API RESTful construida con **Flask** que recibe reportes de hechos delictivos en formato JSON y los envía a una cola de **RabbitMQ** para su posterior procesamiento.

## 🛠️ Tecnologías usadas

- Flask
- RabbitMQ
- Pika (cliente Python para RabbitMQ)

## 📦 Estructura del proyecto

.
├── app.py           # Código principal de la API
├── README.md        # Documentación del proyecto
└── requirements.txt # (Opcional) Dependencias del proyecto

## 🚀 ¿Cómo ejecutar el proyecto?

### 1. Pre-requisitos

- Python 3.x
- RabbitMQ instalado y ejecutándose en localhost
- pip para instalar paquetes

### 2. Clonar el repositorio

git clone https://github.com/tuusuario/api-hechos-delictivos.git
cd api-hechos-delictivos

### 3. Instalar dependencias

pip install flask pika

(O crea un archivo llamado `requirements.txt` con este contenido:)

flask
pika

Y luego instala con:

pip install -r requirements.txt

### 4. Ejecutar RabbitMQ

Asegúrate de que RabbitMQ esté corriendo en tu máquina local. Si usas Docker:

docker run -d --hostname rabbitmq --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Accede al panel en: http://localhost:15672  
Usuario: guest | Contraseña: guest

### 5. Ejecutar la API

python app.py

La API estará disponible en http://127.0.0.1:5000

## 📤 Endpoint disponible

### POST `/enviar-hecho`

Recibe un objeto JSON con la siguiente estructura:

{
  "direccion": "Av. Siempre Viva",
  "interseccion": "con Calle Falsa",
  "numero_casa": "742",
  "latitud": -0.22985,
  "longitud": -78.52495,
  "tipo_lugar": "casa",
  "sector_punto_referencia": "cerca del parque central",
  "fecha_hecho": "2025-07-08",
  "hora_aproximada_hecho": "14:30",
  "enlace_fuente": "https://example.com/video",
  "transcripción_de_video": "Se observa el hecho...",
  "transcripción_de_audio": "Se escucha un ruido fuerte..."
}

#### Respuestas posibles

- ✅ 200 OK: Mensaje válido y enviado a RabbitMQ.
- ❌ 400 Bad Request: Faltan campos requeridos o JSON inválido.
- ⚠️ 500 Internal Server Error: Error inesperado del servidor.

## 📚 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
