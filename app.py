from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Endpoint para obter todos os usuários da API JSONPlaceholder.

    Faz uma requisição GET para a URL da API JSONPlaceholder que retorna uma lista de usuários.
    Em seguida, converte a resposta em formato JSON e a retorna como resposta da API Flask.

    Returns:
        Response: Uma lista de usuários em formato JSON.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    return render_template('users.html', users=users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Endpoint para obter um único usuário da API JSONPlaceholder com base no ID do usuário.

    Faz uma requisição GET para a URL da API JSONPlaceholder que retorna os detalhes de um usuário
    específico com base no ID fornecido. Converte a resposta em formato JSON e a retorna.

    Args:
        user_id (int): O ID do usuário que queremos obter.

    Returns:
        Response: Os detalhes do usuário em formato JSON.
    """
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user = response.json()
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
