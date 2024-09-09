import streamlit as st
from chatbot import NvidiaChatbot
from dotenv import load_dotenv
import os
import time  # Import necessário para simular o tempo de carregamento

# Carrega variáveis do arquivo .env
load_dotenv()

def main():
    # Obtém a chave da API do arquivo .env
    api_key = os.getenv("API_KEY")
    if not api_key:
        st.error("A chave da API não foi encontrada. Verifique o arquivo .env.")
        return

    chatbot = NvidiaChatbot(api_key)

    # Configuração da página
    st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")

    st.title('🤖 Bem vindo ao MariTalk  Streamlit')
    st.write('Digite sua mensagem abaixo e veja a resposta da MariTalk .')
    
    # Aplicar estilos de CSS à página
    with open("static/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Caixa de entrada do usuário
    mensagem_usuario = st.text_input("Você:", "")

    # Botão para enviar a mensagem
    if st.button('Enviar'):
        if mensagem_usuario:
            # Exibir indicador de carregamento
            with st.spinner('Processando a resposta...'):
                resposta = chatbot.responder(mensagem_usuario)
                # Exibição da resposta com estilização
                st.markdown(f"""
                    <div style="background-color:#e0f7fa; border-radius:8px; padding:12px; margin-top:10px;">
                        <strong style="color:#00796b;">Você:</strong> <span style="color:#004d40;">{mensagem_usuario}</span>
                    </div>
                    <div style="background-color:#bbdefb; border-radius:8px; padding:12px; margin-top:10px;">
                        <strong style="color:#0d47a1;">Chatbot:</strong> <span style="color:#0d47a1;">{resposta}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning('Por favor, digite uma mensagem.')

if __name__ == '__main__':
    main()
