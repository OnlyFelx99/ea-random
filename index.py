
from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

# Função para carregar a lista de animais do arquivo JSON
def carregaranimais():
    try:
        with open('animals.json', 'r') as file:
            data = json.load(file)
        return data["animals"]
    except FileNotFoundError:
        return ["🐒", "🐊", "🐯", "🦆", "🦁"]

# Rota para retornar a lista de animais
@app.route('/emojis', methods=['GET'])
def obter_emojis():
    animais = carregaranimais()
    return jsonify(animais)

# Rota para retornar um animal aleatório
@app.route('/emojis/random', methods=['GET'])
def emojisrandom():
    animais = carregaranimais()
    animalescolhido = random.choice(animais)
    return jsonify(animalescolhido)

if __name__ == '__main__':
    app.run(debug=True)

