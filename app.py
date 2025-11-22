import random, time
from flask import Flask
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # หรือใส่เฉพาะ URL React
# async_mode ต้องเป็น gevent

def sensor_loop():
    while True:
        data = {
            "temperature": round(random.uniform(20, 40), 2),
            "pressure": round(random.uniform(1.0, 1.5), 3)
        }
        socketio.emit("sensor_update", data)
        time.sleep(1)

Thread(target=sensor_loop, daemon=True).start()

@app.route("/api/status")
def status():
    return {"status": "running"}

# ❌ ไม่ต้องมี socketio.run()
