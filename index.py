
from flask import Flask
import random
import json

app = Flask(__name__)

# Função para carregar a lista de animais do arquivo JSON
def carregar_animais():
    try:
        with open('animals.json', 'r') as file:
            data = json.load(file)
        return data["animals"]
    except FileNotFoundError:
        return ["🐒", "🐊", "🐯", "🦆", "🦁"]

@app.route('/EA/Emojis', methods=['GET'])
def emojisrandom():
    # Carrega a lista de animais dinamicamente
    animais = carregar_animais()
    
    # Escolhe aleatoriamente um animal da lista
    animal_escolhido = random.choice(animais)
    return animal_escolhido

if __name__ == '__main__':
    app.run(debug=True)
