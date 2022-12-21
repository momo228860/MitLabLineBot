from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola_ubunlog():
    return 'XDDDDD'

if __name__ == "__main__":
        app.run(host='0.0.0.0')
