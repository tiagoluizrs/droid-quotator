# Cotador de Droids


## Iniciando a aplicação no Docker


Rode os comandos à seguir na ordem em que estão para poder executar a aplicação utilizando o docker-compose:

Rode este comando para criar os serviços que irão rodar em container. Toda vez que você alterar um arquivo do serviço ou o `Dockerfile` você precisará rodar esse comando novamente:
```console
sudo docker-compose build
```

Agora que tudo está pronto, rode o comando à seguir para rodar os serviços no docker.
```console
sudo docker-compose up
```

Agora com o docker rodando os containers você verá um erro ocorrendo, pois ainda não rodamos a migração. Devido à questão de termos um serviço no django customizado de usuários, precisaremos seguir alguns passos. Entre no container onde está a aplicação rodando, mesmo com erro deixe-a rodando.
```console
docker-compose run web python manage.py makemigrations account
docker-compose run web python manage.py migrate account
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
``` 

Se por algum motivo o migrate não funcionar conforme está acima siga os passos abaixo:
```console
sudo docker exec -it CONTAINER_ID bash (Para ver o id do container é só rodar sudo docker container ls)
python manage.py makemigrations account
python manage.py migrate account
python manage.py makemigrations
python manage.py migrate
```

Agora pare e inicie novamente os serviços.
```console
sudo docker-compose down
sudo docker-compose up
```

Abra uma nova aba no terminal e rode o comando abaixo para criar um super usuário para o sistema. Esse usuário terá acesso ao admin e será um super usuário;
```console
sudo docker-compose run web python manage.py createsuperuser
```


## Postman


Para realizar qualquer requisição aos endpoints das demandas é necessário autenticar o usuário antes. Para isso, acesse o endpoint `Login para solicitação de Token de acesso à API` e faça conforme à imagem abaixo:

![Login {w=100%}](readme_images/login_endpoint.png)

Pegue o token que foi entregue no resultado da requisição e faça igual à imagem abaixo:
![Login {w=100%}](readme_images/endpoint_with_token.png)

Perceba que no local onde o token se encontra você deverá seguir o padrão:
Exemplo: **JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI...**

> Todos os endpoints exceto o login exigem esse padrão de cabeçalho.


## Testes unitários