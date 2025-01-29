# Desafio do Serasa

## Passo a passo para rodar o projeto

Siga os passos a seguir para testar a aplicação:

1. Clone o projeto em sua máquina
2. Crie um arquivo chamado ".env" com os dados que tem no arquivo ".env.example"
3. Acesse a raiz da pasta "src" e execute o comando: 
    ```bash
    docker-compose up --build
    ```
4. Acesse no navegador a seguinte URL: 
    [http://localhost:8000/api/swagger/](http://localhost:8000/api/swagger/)
5. Com o Swagger, é possível fazer requisições às rotas desejadas
6. Verifique os relacionamentos no modelo de classes na foto abaixo, isso servirá para que você possa se orientar sobre os relacionamentos dos modelos.

![diagrama](https://github.com/user-attachments/assets/6d2db6c3-19e4-465c-9020-222f4390ad9d)
