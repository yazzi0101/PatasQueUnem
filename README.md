# 🐾 Patas que Unem

<!-- A logo do projeto será adicionada aqui posteriormente. -->

**Conectando animais que precisam de um lar a pessoas que desejam adotar.**

O **Patas que Unem** é uma aplicação web desenvolvida por alunos do projeto integrador da UNIVESP. A plataforma tem como objetivo facilitar a divulgação de animais disponíveis para adoção e aproximar esses animais de possíveis adotantes.

## ✨ Funcionalidades

- Visualização dos animais disponíveis para adoção.
- Página com informações detalhadas de cada animal.
- Formulário para demonstrar interesse na adoção.
- Validação de dados dos formulários.
- Preenchimento de endereço por meio da integração com a API ViaCEP.
- Interface web para facilitar a navegação dos usuários.

## 🛠️ Tecnologias utilizadas

- **Python**
- **Django**
- **SQLite**
- **HTML**
- **CSS**
- **JavaScript**
- **API ViaCEP**
- **Git e GitHub**

## 🚀 Como executar o projeto localmente

### Pré-requisitos

- Python instalado.
- Git instalado, caso deseje clonar o repositório.

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/yazzi0101/PatasQueUnem.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd PatasQueUnem
   ```

3. Crie um ambiente virtual e ative:


    No Windows:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    ```

    No Linux/Mac:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    
4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:

   ```text
   http://127.0.0.1:8000/
   ```

## 📌 Status do projeto
Projeto em desenvolvimento.
