from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Clave secreta para verificar la autenticidad de las solicitudes
secret_key = 'No89LaBn6x2MPk3f5Y7G'

# Página HTML simple
html_page = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webhook API</title>
</head>
<body>
    <h1>Webhook API</h1>
    <p>La API está activa y funcionando correctamente.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_page)

@app.route('/webhook', methods=['POST'])
def webhook():
    received_key = request.headers.get('x-api-key')  # Supongamos que la clave viene en el encabezado

    # Verifica si la clave coincide con la clave secreta
    if received_key != secret_key:
        return jsonify({'message': 'Clave no válida.'}), 403

    # Procesar los datos recibidos del webhook
    data = request.json
    print('Datos recibidos:', data)

    # Respuesta a la solicitud
    return jsonify({'message': 'Evento recibido y autenticado correctamente.'}), 200

if __name__ == '__main__':
    app.run(port=5000)
