# Cadastro e Listagem de Produtos - Flask App

Este é um aplicativo web desenvolvido em Python utilizando o framework Flask. Ele foi criado como parte de um teste técnico, com foco em funcionalidade e organização.

# 🎯 Funcionalidades

- Cadastro de Produtos:
  - Nome do produto
  - Descrição
  - Valor
  - Disponibilidade para venda (sim/não)

- Listagem de Produtos:
  - Exibição de nome e valor dos produtos cadastrados
  - Ordenação dos produtos pelo valor (do menor para o maior)
  - Botão para cadastrar novos produtos diretamente na página de listagem

# 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- HTML5 e CSS3
- Jinja2 (Template Engine)

# 📂 Estrutura do Projeto

OAK_challenge/
├── venv/                   # Ambiente virtual
├── templates/              # Templates HTML
│   ├── cadastro.html       # Página de cadastro de produtos
│   ├── listagem.html       # Página de listagem de produtos
├── static/                 # Arquivos estáticos (CSS, imagens)
│   ├── style.css           # Estilo CSS
├── app.py                  # Código principal da aplicação
├── requirements.txt        # Dependências do projeto
└── .gitignore              # Arquivos e pastas ignorados pelo Git

# 🚀 Como Rodar o Projeto

1. Clone o repositório:
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Navegue até o diretório do projeto:
   cd OAK_challenge

3. Crie e ative um ambiente virtual:
     # No Windows:
   ```bash
   python -m venv venv
   
   .\venv\Scripts\activate
     # No Linux/macOS:
   python3 -m venv venv
   source venv/bin/activate

5. Instale as dependências:
   pip install -r requirements.txt

6. Inicie o servidor:
   python app.py

7. Acesse o aplicativo no navegador:
   # http://127.0.0.1:5000

# 🖌️ Estilo Visual

O design do projeto foi feito com base nas cores da Oak Tecnologia, buscando um layout limpo e profissional.

# 📜 Licença

Este projeto é de uso interno e educativo, e foi desenvolvido como parte de um teste técnico.
```
