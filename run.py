from app import create_app
from app.socketi0 import socketio


app = create_app()
if __name__ == '__main__':
    socketio.run(app=app)