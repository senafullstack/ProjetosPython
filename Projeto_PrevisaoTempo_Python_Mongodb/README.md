# Aplicação de Previsão do Tempo

Este projeto é uma aplicação de backend que retorna os dados da previsão do tempo dos próximos dias. A aplicação foi desenvolvida utilizando a linguagem de programação Python e a API de previsão do tempo de 5 dias do https://openweathermap.org/.

Requisitos
Linguagem de programação Python
Virtualização de container utilizando Docker
Elaboração dos endpoints utilizando padrão REST
Banco de dados não relacional, como MongoDB
Bibliotecas e frameworks à escolha do desenvolvedor
Elaboração de README com instruções para subir o ambiente da aplicação
Como funciona
A aplicação utiliza a API do OpenWeatherMap para obter os dados da previsão do tempo. Os dados são então armazenados em um banco de dados não relacional, como MongoDB. A aplicação disponibiliza uma API REST para acessar os dados armazenados.

Endpoints
A aplicação disponibiliza os seguintes endpoints:

/api/v1/previsaotempo?city=Recife : Retorna a previsão do tempo para os próximos 5 dias.
Instalação
Para instalar a aplicação, siga estas etapas:

Instale o Docker.
Clone o repositório do projeto.
Navegue até o diretório do projeto.
Execute o seguinte comando para construir a imagem Docker:
docker build -t previsaotempo.
Execute o seguinte comando para executar o container Docker:
docker run previsaotempo
Isso iniciará a aplicação no container Docker. Você pode então acessar a API no navegador usando o endereço IP do host do Docker.