from flask import Flask, render_template
import redis

app = Flask(__name__)
client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/count')
def count():
    count = client.incr('visitor_count')
    return render_template('count.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
