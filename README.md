# Flask JSONPlaceholder API

Este projeto é uma API simples desenvolvida em Flask, que consome dados da API pública JSONPlaceholder. Ele fornece endpoints para listar todos os usuários e obter detalhes de um usuário específico.

## Tecnologias Utilizadas

- **Flask**: Framework para desenvolvimento web em Python.
- **requests**: Biblioteca para fazer requisições HTTP em Python.

## Estrutura do Projeto


## Endpoints

### 1. Listar Todos os Usuários

- **URL**: `/api/users`
- **Método**: `GET`
- **Descrição**: Retorna uma lista de todos os usuários da API JSONPlaceholder.
- **Resposta**: Uma lista de usuários em formato JSON.

### 2. Obter Detalhes de um Usuário

- **URL**: `/api/users/<int:user_id>`
- **Método**: `GET`
- **Descrição**: Retorna os detalhes de um único usuário com base no ID fornecido.
- **Parâmetros**:
  - `user_id` (int): O ID do usuário que queremos obter.
- **Resposta**: Detalhes do usuário em formato JSON.
