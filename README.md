# Assistente virtual
Este projeto é um programa com interface gráfica desenvolvido em python, que permite o usuário a ter um assistente virtual inteligente para te auxiliar nas suas duvidas do dia a dia. Utiliza a biblioteca tkinter para a interface gráfica, a biblioteca SpeechRecognition o reconhecimento da fala e a api do google gemini.


## Pré-requisitos


Como Usar
Ao executar o aplicativo, uma janela será exibida com a mensagem "Clique para falar com a IA" e um círculo azul.
Clique no círculo azul para iniciar o reconhecimento de fala.
A interface exibirá "Estou ouvindo..." enquanto captura o áudio.
Após o reconhecimento, o texto será exibido na interface como "Você disse: [frase]" ou "Não entendi o que você disse!".
A função de síntese de fala (não implementada no código acima) poderia ser adicionada para fazer o assistente responder de forma falada ao usuário.
Observações
O código depende de uma conexão de internet para funcionar corretamente, pois usa a API do Google para o reconhecimento de fala.
A interface gráfica é simples e interativa, focada apenas na captura de áudio e no processamento de fala.
