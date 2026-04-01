from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "secure", "message": "SecretShield is running!"}

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True)