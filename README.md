# Assistente Virtual em Python

Este projeto é uma **assistente virtual baseada em inteligência artificial**, que utiliza reconhecimento de voz, síntese de fala e processamento de linguagem natural para interagir com o usuário. A interface gráfica é construída com `Tkinter`, e ferramentas como `speech_recognition`, `pyttsx3` e a API do **Google Generative AI** são integradas para criar uma experiência interativa.

## ⚙️ Funcionalidades

- **Reconhecimento de Fala**: Captura a voz do usuário via microfone e converte em texto.
- **Respostas Inteligentes**: Processa as entradas com a API do Google Generative AI.
- **Síntese de Voz**: Converte as respostas da IA em áudio usando `pyttsx3`.
- **Interface Simples**: Um botão em uma janela gráfica para interação.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Bibliotecas**:
  - [`Tkinter`](https://docs.python.org/3/library/tk.html): Utilizada para a construção da interface gráfica..
  - [`speech_recognition`](https://pypi.org/project/SpeechRecognition/): Captura e converte áudio em texto.
  - [`pyttsx3`](https://pypi.org/project/pyttsx3/): Converte o texto gerado pela IA em áudio.
  - [`google-generativeai`](https://github.com/google/generative-ai-python): Biblioteca que interage com a API generativa do Google para respostas inteligentes.
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/): Gerenciamento de variáveis de ambiente.

## 🚀 Como Usar
Ao executar o aplicativo, uma janela será exibida com a mensagem "Clique para falar com a IA" e um círculo azul.
Clique no círculo azul para iniciar o reconhecimento de fala.
A interface exibirá "Estou ouvindo..." enquanto captura o áudio. Após o reconhecimento, a ia irá responder de forma falada ao usuário 

### 1. **Pré-requisitos**
Certifique-se de que tem o Python instalado e as bibliotecas necessárias. Instale-as com:
```bash
pip install -r requirements.txt
```
### 2. **Configuração da API Key**
Crie um arquivo .env no diretório do projeto e adicione sua chave da API da Google Generative AI da seguinte maneira:
```bash
API_KEY=(sua api)
```
**Nota: A chave da API pode ser obtida através da [`Google AI for Developers`](https://ai.google.dev/), criando um novo projeto e habilitando a API desejada.**
