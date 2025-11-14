from flask import Flask, jsonify, render_template
import RPi.GPIO as GPIO
import dht11
import time

app = Flask(__name__)

# -------------------------
# CONFIGURACIÓN DEL DHT11
# -------------------------

PIN_DHT = 7  # Pin físico N°7 (GPIO4). Cámbialo si usas otro.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

sensor = dht11.DHT11(pin=PIN_DHT)

# -------------------------
# RUTAS DE LA WEB
# -------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/datos")
def datos():
    lectura = sensor.read()

    if lectura.is_valid():
        return jsonify({
            "temperatura": lectura.temperature,
            "humedad": lectura.humidity
        })
    else:
        return jsonify({"error": "No se pudo leer el DHT11"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
