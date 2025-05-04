def bot_response(message):
    msg = message.lower()

    if "jogo" in msg or "partida" in msg:
        return "O próximo jogo da FURIA é contra a G2, amanhã às 16h!"
    elif "placar" in msg:
        return "A FURIA venceu a última partida por 2x1 contra a Natus Vincere!"
    elif "jogador" in msg:
        return "KSCERATO foi o destaque da última partida com 27 abates!"
    elif "vai furia" in msg:
        return "VAAAAAAI FURIA! 🔥🖤"
    else:
        return "Não entendi, mas a FURIA sempre responde com garra! 💪"

