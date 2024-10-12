# Mars Rover Photo Dashboard

Um aplicativo web simples em **Dash** que permite explorar imagens tiradas pelos rovers da NASA em Marte.

## Descrição

Este projeto usa a API da NASA para buscar e exibir fotos tiradas pelos rovers **Curiosity**, **Opportunity** e **Spirit**. O usuário pode escolher um rover e um "sol" (um dia marciano) para ver as imagens capturadas nesse dia.

## Tecnologias Utilizadas

- [Dash](https://dash.plotly.com/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [API da NASA](https://api.nasa.gov/)

## Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/leticia-pontes/mars-rover-dashboard
   cd mars-rover-dashboard
   ```
   
2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto:
   ```bash
   touch .env
   ```

5. Adicione sua chave de API da NASA em `.env`:
   ```python
   API_KEY = "SUA_API_KEY"  # Substitua pela sua chave
   ```

## Uso
Para iniciar o aplicativo, execute o seguinte comando:
```bash
python app.py
```

Depois, abra o navegador e acesse http://127.0.0.1:8050/.
1. Escolha um rover no dropdown.
2. Insira um número de "sol" (por exemplo, 1000).
3. Clique em Submit para ver as imagens.
