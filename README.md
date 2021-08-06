# FamPay Assignment
The assignment is to implement a back-end which constantly fetches latest videos of a certain defined keyword using the YouTube Data API.

## Tasks completed

 - Buillt a REST API using Django REST Framework.
 - Swagger implemented for API documentation
 - Containerized application using Docker.
 - Async API calls using Celery with RabbitMQ as a message broker.
 - Basic search API implemented for videos stored in database.
 - GET Request for fetching all videos in the database.
 - Paginated responses for both requests.
 - Implemented support for multiple API keys and deletion of them from the database once quota of a key is exhausted
 - Implemented partial searching in the search API.


## Built With

- [Django REST Framework](https://www.django-rest-framework.org)

- [RabbitMQ](https://www.rabbitmq.com)

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)

- [docker-compose](https://docs.docker.com/compose/install/)

## Installation and Usage

1. Clone this repository and change directory.

```bash
git clone https://github.com/Rugz007/FamPayTask.git
cd FamPayTask
```
2. Run the following command to **build** all the containers
```bash
docker-compose build
```
4. Run the following command to **run** all the containers

```bash
docker-compose up
```
