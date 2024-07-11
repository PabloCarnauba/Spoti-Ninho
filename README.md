# Spoti-Ninho

## Descrição do Projeto

Spoti-Ninho é um projeto de interface gráfica de um player de música desenvolvido em Python usando a biblioteca PySimpleGUI. A aplicação permite a seleção, reprodução, pausa e navegação entre músicas, além de exibir informações sobre a faixa e a capa do álbum em execução. Este projeto é ideal para aqueles que estão iniciando no desenvolvimento de interfaces gráficas e manipulação de áudio com Python.

## Funcionalidades

- **Reprodução de Música**: Inicie a reprodução da música selecionada.
- **Pausar/Despausar**: Pause ou despause a música atual.
- **Próxima Música**: Avance para a próxima faixa na lista de reprodução.
- **Música Anterior**: Retorne para a faixa anterior na lista de reprodução.
- **Exibição de Informações**: Mostra o nome da música, artista e a capa do álbum.

## Estrutura do Projeto

- **`player.py`**: Módulo responsável pela reprodução de músicas usando o Pygame.
- **`musica.py`**: Módulo que gerencia a lista de músicas e seus atributos.
- **`Interface.py`**: Arquivo principal contendo a interface gráfica e a lógica de interação com o usuário.

## Requisitos

- Python 3.6 ou superior
- PySimpleGUI
- Pygame

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/PabloCarnauba/Spoti-Ninho.git
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute a aplicação:**
   ```bash
   python Interface.py
   ```

## Estrutura da Interface

A interface do Spoti-Ninho foi projetada para ser intuitiva e agradável, com o tema `Reddit` do PySimpleGUI e uma paleta de cores em preto e branco. Os elementos principais da interface incluem:

- **Título da Música**: Exibe o nome da música em execução.
- **Informações do Player**: Exibe o nome do player (Spoti-Ninho).
- **Capa do Álbum**: Mostra a imagem da capa do álbum da música em reprodução.
- **Controles de Música**: Botões para voltar, pausar/despausar e avançar a faixa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.
