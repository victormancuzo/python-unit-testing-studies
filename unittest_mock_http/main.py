# pip install requests
import requests


def obter_dados_usuario(id_usuario):
    response = requests.get(f"https://api.example.com/users/{id_usuario}")
    return response.json()
