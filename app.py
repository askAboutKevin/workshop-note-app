# app/app.py
from flask import Flask
from controllers import note_controller

app = Flask(__name__)
app.register_blueprint(note_controller.note_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
