
from flask import Flask
import random
import json

app = Flask(__name__)

# Função para carregar a lista de animais do arquivo JSON
@app.route('emojis', methods=['GET'])
def carregaranimais():
    try:
        with open('animals.json', 'r') as file:
            data = json.load(file)
        return data["animals"]
    except FileNotFoundError:
        return ["🐒", "🐊", "🐯", "🦆", "🦁"]


def emojisrandom():
    # Carrega a lista de animais dinamicamente
    animais = carregaranimais()
    
    # Escolhe aleatoriamente um animal da lista
    animalescolhido = random.choice(animais)
    return animalescolhido

if __name__ == '__main__':
    app.run(debug=True)
