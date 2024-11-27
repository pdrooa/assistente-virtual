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
  - [`Tkinter`](https://docs.python.org/3/library/tk.html): Interface gráfica.
  - [`speech_recognition`](https://pypi.org/project/SpeechRecognition/): Reconhecimento de voz.
  - [`pyttsx3`](https://pypi.org/project/pyttsx3/): Síntese de fala.
  - [`google-generativeai`](https://github.com/google/generative-ai-python): Interface para a API generativa do Google.
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/): Gerenciamento de variáveis de ambiente.

## 🚀 Como Usar

### 1. **Pré-requisitos**
Certifique-se de que tem o Python instalado e as bibliotecas necessárias. Instale-as com:
```bash
pip install -r requirements.txt
