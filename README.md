# Simple API for Parsing Data from Module Bank

<p>This simple api on the index page requests a token from the "Module Bank". An asynchronous transaction starts to be executed to save to the local database. Data to save: all companies on the account, all bank accounts for each company, all transactions on each bank account.</p>

### Stack:
<p align="center">
    <img src="https://img.shields.io/badge/Django-3.2.8-blue?logo=django&style=flat"/>
    <img src="https://img.shields.io/badge/Django%20REST%20framework-3.12.4-green?logo=django&style=flat"/>
    <img src="https://img.shields.io/badge/SQLite-3.36.0-blue?logo=sqlite&style=flat"/>
    <img src="https://img.shields.io/badge/Celery-5.1.2-green?logo=celery&style=flat"/>
    <img src="https://img.shields.io/badge/Redis-7.0.0-red?logo=redis&style=flat"/>
    <img src="https://img.shields.io/badge/Flower-1.0.0-purple?logo=flower&style=flat"/>
    <img src="https://img.shields.io/badge/Postman-7.37.0-orange?logo=postman&style=flat"/>
    <img src="https://img.shields.io/badge/Requests-2.26.0-yellow?logo=requests&style=flat"/>
    <img src="https://img.shields.io/badge/Docker%20Compose-1.29.2-blue?logo=docker&style=flat"/>
</p>

### Getting Started:
1. Clone the repository:
```
git clone git@github.com:leabrun/api_bank.git
```
2. Navigate to the project directory
```
cd api_bank
```
3. Run the containers
```
docker-compose up -d --build
```

### API Testing
Explore the API using [Postman](https://www.postman.com/leabrun/workspace/api-bank/overview).
