from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from utils.bot import bot_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'furia_chat_secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    emit('message', {'user': 'Você', 'text': msg}, broadcast=True)
    
    response = bot_response(msg)
    emit('message', {'user': 'FURIA Bot', 'text': response}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
