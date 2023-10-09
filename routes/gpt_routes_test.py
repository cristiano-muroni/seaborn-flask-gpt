import json
import pytest
from config_test import app, client


def test_chatbot_route(client):
    # Defina um exemplo de entrada de solicitação JSON
    request_data = {
        "content": "Fale me da Citrosuco?"
    }

    # Faça uma solicitação POST para a rota '/chatbot'
    response = client.post('/chatbot', json=request_data)

    # Verifique o código de status da resposta
    assert response.status_code == 200

    # Verifique o conteúdo da resposta
    response_data = response.data.decode('utf-8')
    assert  response_data
    assert response_data.strip()  # Verifique se a mensagem não está vazia

    # Você pode adicionar mais verificações aqui, dependendo das expectativas da sua rota
