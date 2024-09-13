<img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="py-logo" width="200"/>

  
Este projeto permite a execução remota de scripts através de uma interface web.

### Tecnologias Utilizadas

* Flask (Python): Framework web para desenvolvimento do servidor.
* HTML: Estrutura da página web.
* JavaScript: Funcionalidade interativa do cliente.

### Como Funciona

1. O usuário acessa a página web.
2. Ao clicar em um dos botões "Run Script", o caminho do script correspondente é enviado ao servidor.
3. O servidor Flask recebe a requisição e executa o script informado.
4. O resultado da execução (sucesso ou erro) é enviado de volta para a página web.
5. A mensagem de resultado é exibida para o usuário.

### Requisitos

* Python 3.x
* Flask

### Instalação

1. Clone este repositório.
2. Instale as dependências:

```bash
pip install flask
```

### Executando o Projeto

1. Navegue até a pasta do projeto.
2. Execute o seguinte comando:

```bash
python app.py
```

3. Acesse `http://127.0.0.1:5000/` em seu navegador web.

### Uso

* Altere os caminhos dos scripts definidos nas variáveis `bottom1`, `bottom2`, e `bottom3` no arquivo `script.js`.
* Clique em um dos botões "Run Script" para executar o script correspondente.

### Considerações de Segurança

* **Atenção:** Executar scripts arbitrários no servidor pode ser um risco de segurança. Certifique-se de limitar os scripts que podem ser executados e implementar mecanismos de autenticação e autorização adequados.
* Os scripts devem estar localizados em um diretório seguro e acessível apenas pelo aplicativo.
