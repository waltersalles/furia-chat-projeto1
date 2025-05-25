from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

respostas = {
    "oi": "Fala, FURIOSO! 👊 Pronto pra torcer com a gente?",
    "quando é o próximo jogo": "Nosso próximo confronto é amanhã, às 20h, contra a Natus Vincere! 🖤💛",
    "quem é o time titular": "Atualmente estamos com: arT, KSCERATO, yuurih, chelo e FalleN. Lenda reconhece lenda. 🔥",
    "ranking": "Estamos atualmente no top 10 mundial! #RunFURIA",
    "default": "Desculpa, não entendi. Tente perguntar sobre jogos, lineup ou ranking. 😉"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/responder', methods=['POST'])
def responder():
    pergunta = request.json.get("mensagem", "").lower()
    resposta = respostas.get(pergunta, respostas["default"])
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
