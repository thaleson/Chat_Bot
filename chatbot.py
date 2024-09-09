import requests
from chatbot_interface import ChatbotInterface

class NvidiaChatbot(ChatbotInterface):
    def __init__(self, api_key: str):
        """
        Inicializa o NvidiaChatbot com a chave da API e URL base.

        Parâmetros:
        -----------
        api_key : str
            Chave da API para autenticação.
        """
        self.api_key = api_key
        self.api_url = "https://integrate.api.nvidia.com/v1/chat/completions"  # Verifique a URL

    def responder(self, mensagem: str) -> str:
        """
        Envia uma mensagem para a API e retorna a resposta gerada.

        Parâmetros:
        -----------
        mensagem : str
            Texto a ser enviado para a API.

        Retorna:
        --------
        str
            Resposta gerada pela API.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta/llama3-70b-instruct",  # Verifique se o nome do modelo está correto
            "messages": [{"role": "user", "content": mensagem}]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

            data = response.json()
            resposta = data.get("choices", [{}])[0].get("message", {}).get("content", "Desculpe, não entendi a sua mensagem.")
            return resposta

        except requests.exceptions.HTTPError as http_err:
            print(f"Erro HTTP: {http_err}")
            return "Desculpe, ocorreu um erro ao processar a sua solicitação."
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Erro de Conexão: {conn_err}")
            return "Desculpe, não foi possível conectar ao servidor."
        except requests.exceptions.Timeout as timeout_err:
            print(f"Erro de Timeout: {timeout_err}")
            return "Desculpe, a solicitação demorou demais para ser processada."
        except requests.exceptions.RequestException as req_err:
            print(f"Erro na Requisição: {req_err}")
            return "Desculpe, ocorreu um erro ao processar a sua solicitação."

# Exemplo de uso:

