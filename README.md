# FamPay Assignment
[![CodeFactor](https://www.codefactor.io/repository/github/rugz007/fampaytask/badge/master?s=0da46bcb1d77bcc7bb229632a6e590aace20b933)](https://www.codefactor.io/repository/github/rugz007/fampaytask/overview/master)

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

## System Architecture
![Images](https://i.imgur.com/6BCx5D0.png)

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
## Note
- Admin user with username as *admin* and password as *admin* is created.
- Query for fetching the videos can be changed in Django settings.
