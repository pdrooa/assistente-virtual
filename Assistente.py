from tkinter import *
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Configuração da ia
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""Você é uma assistente virtual especializada em computadores e tecnologia. Seu objetivo é ajudar usuários a resolver problemas relacionados a hardware, software, sistemas operacionais, redes e tecnologia em geral. Seja claro, técnico quando necessário, mas sempre educado e acessível para atender desde iniciantes até especialistas.
Aqui estão algumas diretrizes:
Explique conceitos técnicos de forma simplificada quando necessário.
Forneça soluções passo a passo para problemas técnicos.
Sugira boas práticas para manutenção de computadores e segurança digital.
Esteja atualizado(a) sobre tendências e inovações em tecnologia.
Use exemplos e metáforas para facilitar a compreensão de tópicos complexos.
quando for falar algo que conter * ignore"""
)

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Ola"},
        {"role": "model", "parts": "Prazer"},
    ]
)

# Configurar tela 
Tela_inicial = Tk()
Tela_inicial.title("Assistente Virtual")
Tela_inicial.resizable(False, False)

# Definir botao e texto
texto1 = Label(Tela_inicial, text="Clique para falar com a Ia")
canvas = Canvas(Tela_inicial, width=200, height=200)
circle = canvas.create_oval(50, 50, 150, 150, fill="blue", outline="black")
texto2 = Label(Tela_inicial, text="")

# Definir botao
canvas.tag_bind(circle, "<Button-1>", lambda event: on_click())

# Alinhar no centro
texto1.grid(row=0, column=0, columnspan=3, pady=20)
canvas.grid(row=1, column=0, columnspan=3, pady=(20, 0))
texto2.grid(row=2, column=0, columnspan=3, pady=20)

# Função que reconhece a fala 
def reconhecer_fala():    
    microfone = sr.Recognizer() # Habilita o microfone
    with sr.Microphone() as source:           
        audio = microfone.listen(source) #Guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        try:
            frase = microfone.recognize_google(audio,language='pt-BR') # Audio sera interpretado em portugues do brasil     
            return frase 
        except:
            texto2.configure(text="Não entendi o que você disse!")
            
 

# Função falar com o bot
def on_click():
    texto2.configure(text="Estou ouvindo...")  # Altera o texto2 para uma mensagem 
    Tela_inicial.update_idletasks()
    texto2.configure(text="")
    Tela_inicial.update_idletasks()



    # Inicializa o mecanismo de fala
    engine = pyttsx3.init()
    frase = reconhecer_fala()
    response = chat.send_message(frase)

    # Usa o engine para transformar o texto em fala
    engine.say(response.text)   # coloca a frase

    # Espera até que a fala termine para finalizar o programa
    engine.runAndWait()

# Manter tela executada
Tela_inicial.mainloop()