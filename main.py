from flask import Flask, jsonify, render_template
import adafruit_dht
import board

app = Flask(__name__)

# Sensor en GPIO17
sensor = adafruit_dht.DHT11(board.D3)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/salida')
def salida():
    valor = request.args.get('valor')
    GPIO.output(17, int(valor))   # pin 17 por ejemplo
    return jsonify({"ok": True})


@app.route("/datos")
def datos():
    try:
        temperatura = sensor.temperature
        humedad = sensor.humidity

        return jsonify({
            "temperatura": temperatura,
            "humedad": humedad
        })
    except Exception:
        return jsonify({"error": "Error leyendo el sensor"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

