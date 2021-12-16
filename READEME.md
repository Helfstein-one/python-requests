#Pré-Requisitos para rodar a Aplicação

É necessário instalar as bibliotecas abaixo

Abra esse projeto na IDE Python e execute os seguintes comandos:
```
pip install flask
pip install requests
```

## Rodando a aplicação

Para rodar a aplicação você precisa executar o seguinte comando: 

```
flask run
```

O sistema vai devolver o endereço do server(Geralmente: http://127.0.0.1:5000/).
Acesse pelo seu navegador(Google Chrome) a URL abaixo:

```
http://127.0.0.1:5000/
```

Se preferir utilize um client http de sua preferência.

## Visualização dos recebimentos

Execute as chamadas nos seguintes recursos:

Para saber os dados do Maurício (nome, idade, telefone e o status da requisição ), execute:

/pegarinfo - GET

#Objetivos da aplicação:
Desenvolver uma api em Python utilizando a biblioteca requests que retorne em
json: seu nome, idade, telefone e o status da requisição.