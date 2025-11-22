import random, time
from flask import Flask, jsonify
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def sensor_loop():
    while True:
        data = {
            "temperature": round(random.uniform(20, 40), 2),
            "pressure": round(random.uniform(1.0, 1.5), 3)
        }
        
        # Send data over socketio using emit
        socketio.emit("sensor_update", data)
        time.sleep(1)
        
Thread(target=sensor_loop, daemon=True).start()

@app.route("/api/status")
def status():
    return {"status": "running"}

if __name__ == "__main__":
    socketio.run(app)