from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)


def enviar_a_rabbitmq(mensaje):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hechos_delictivos')
    channel.basic_publish(
        exchange='',
        routing_key='hechos_delictivos',
        body=json.dumps(mensaje),
        properties=pika.BasicProperties(content_type='application/json')
    )
    connection.close()


@app.route('/enviar-hecho', methods=['POST'])
def recibir_hecho():
    try:
        mensaje = request.get_json()
        if not mensaje:
            return jsonify({"error": "No se recibió JSON válido"}), 400

        # Campos requeridos
        campos_requeridos = [
            "direccion", "interseccion", "numero_casa", "latitud", "longitud",
            "tipo_lugar", "sector_punto_referencia", "fecha_hecho", "hora_aproximada_hecho",
            "enlace_fuente", "transcripción_de_video", "transcripción_de_audio"
        ]

        # Verificar si todos los campos están presentes
        faltantes = [campo for campo in campos_requeridos if campo not in mensaje]
        if faltantes:
            return jsonify({
                "error": "Faltan campos requeridos",
                "campos_faltantes": faltantes
            }), 400

        enviar_a_rabbitmq(mensaje)
        return jsonify({"mensaje": "✅ Mensaje válido y enviado a RabbitMQ"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
