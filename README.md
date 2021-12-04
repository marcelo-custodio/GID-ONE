# Resumo Criptográfico

-  ## Tecnologias Utilizadas

### Backend:

> + cryptography: disponibiliza código de alto nível e interfaces de baixo nível para algoritmos criptográficos comuns, como cifras simétricas, resumos criptográficos de mensagens e funções de derivação de chaves. [1]
>> Utilizado para gerar o resumo criptográfico SHA-256.
> + Flask: É um *framework* leve de aplicações web com Python. Projetado para tornar o desenvolvimento rápido e fácil, com a capacidade de escalar para aplicações mais complexas. [2]
>> Utilizado para disponibilizar a interface gráfica da aplicação.
> + Flask-RESTful: é uma extensão para Flask que adiciona suporte para construir *API's RESTful* de maneira mais ágil. [3]
>> Utilizado para disponibilizar o *endpoint* responsável por gerar o resumo criptográfico para a interface gráfica.

### Frontend:
> + Jinja: É um mecanismo de modelos rápido e extensível, que permite substituir *placeholders* com código semelhante a Python. [4]
>> Utilizado para gerar a interface gráfica web.
> + Axios: É um cliente *HTTP* baseado em promessas para o navegador. [5]
>> Utilizado para realizar as chamadas *HTTP* *client-side* para a *API* *server-side* da aplicação.

-  ## Dificuldades Encontradas

> Falta de conhecimento sobre o framework Flask no desenvolvimento do *backend* da aplicação, resolvido após assistir alguns tutoriais no YouTube e leitura da documentação.

> Falta de conhecimento sobre chamadas HTTP no desenvolvimento *frontend*, resolvido após encontrar o *client* Axios e ler sua documentação.

### Como executar

1. Execute python3 -m pip install -r requirements.txt
2. Execute python3 main.py

Ou

1. docker build . -t "nome_da_imagem"
2. docker run -p 5000:5000 "nome_da_imagem"

### Referências

1. [cryptography](https://cryptography.io/)
2. [Flask](https://flask.palletsprojects.com/)
3. [Flask RESTful](https://flask-restful.readthedocs.io/)
4. [Jinja](https://jinja.palletsprojects.com/)
5. [Axios](https://axios-http.com/docs/intro)
