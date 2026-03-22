from flask import Flask
import redis
import os

app = Flask(__name__)

# Get Redis host from environment
redis_host = os.getenv("REDIS_HOST", "localhost")

r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def hello():
    count = r.incr("counter")
    return f"Hello Kubernetes 🚀 | Count: {count}"

app.run(host="0.0.0.0", port=5000)