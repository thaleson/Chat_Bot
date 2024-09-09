# 🤖 **Chatbot Inteligente com Streamlit** 🚀

Bem-vindo ao projeto **Chatbot Inteligente**! Este projeto demonstra como criar um chatbot interativo e inteligente usando o Streamlit e técnicas avançadas de Processamento de Linguagem Natural (NLP). 🌟

## 📜 **Descrição**

Este chatbot é projetado para entender e responder a mensagens dos usuários de maneira precisa e envolvente. Utilizando um modelo de linguagem avançado, ele oferece respostas contextuais e naturais em uma interface intuitiva criada com Streamlit. 🌐💬

## 🔧 **Recursos**

- **Interface Amigável**: Desenvolvida com Streamlit para uma experiência de usuário fluida e visualmente atraente. 🖥️✨
- **Modelo de Linguagem Avançado**: Utiliza um modelo LLM para gerar respostas contextuais e precisas. 🧠💡
- **Segurança**: Credenciais armazenadas com segurança em variáveis de ambiente. 🔒🛡️
- **Estilização**: Respostas estilizadas para uma aparência moderna e atraente. 🎨🎨

## 📁 **Estrutura do Projeto**

- `.streamlit/config.toml`: Configurações do Streamlit.
- `static/style.css`: Arquivo de estilo para customização da aparência.
- `app.py`: Código principal da aplicação Streamlit.
- `chatbot_interface.py`: Interface do chatbot.
- `chatbot.py`: Implementação do chatbot inteligente.
- `secrets.toml`: Armazena variáveis de ambiente de forma segura.

## 🚀 **Como Executar**

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/thaleson/Chat_Bot.git
    cd Chat_Bot
    ```

2. **Crie um Ambiente Virtual**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Para Windows: .venv\Scripts\activate
    ```

3. **Instale as Dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure suas Credenciais**:

    Crie um arquivo `.env` na raiz do projeto e adicione sua chave API:

    ```env
    API_KEY=your_api_key_here
    ```

5. **Execute a Aplicação**:

    ```bash
    streamlit run app.py
    ```

## 🔍 **Observações**

- Certifique-se de que suas credenciais da API estejam corretamente configuradas no arquivo `.env`.
- Para personalizar a aparência do chatbot, edite o arquivo `static/style.css`.

