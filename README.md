# DevelopsToday test task

This app implements an API for signup, getting and refreshing JWT, CRUD for Posts and Comments on them. Additionally Post has an endpoint for an upvote. Check full API:  
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/13374882-b97c2246-9e33-43a0-8fa6-15bedf809077?action=collection%2Ffork&collection-url=entityId%3D13374882-b97c2246-9e33-43a0-8fa6-15bedf809077%26entityType%3Dcollection%26workspaceId%3Dcd3ff25d-062e-4ffc-92fa-cecfe8ea2306#?env%5BDevelopsToday%20test%20task%20production%5D=W3sia2V5IjoidXNlcl9wYXNzd29yZCIsInZhbHVlIjoiLz9BVUNULTd3PlpFcn5ocCIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJzZWNyZXQifSx7ImtleSI6IkpXVF9hY2Nlc3MiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJKV1RfcmVmcmVzaCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6InVzZXJuYW1lIiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiZW1haWwiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJpZF9sYXN0X3Bvc3QiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJob3N0IiwidmFsdWUiOiJodHRwOi8vZGV2ZWxvcHMtdG9kYXktdGFzay5oZXJva3VhcHAuY29tIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImlkX2xhc3RfY29tbWVudCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

## Used Tools
- Django Rest Framework
- Django Rest Framework Nested Routers
- Celery
- Django Celery Beat  
Additionally the application uses docker-compose.  
For managing periodical tasks, django admin panel is used  

# How to run the application

1) Activate virtual environment
2) Install dependencies with
```pip install -r requirements.txt```  
3) Create directory ```.env``` and file ```.dev-sample``` in it  
```mkdir .env```  
```cd .envtouch```  
```.env```  
4) Add following text to the .env file
```
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432

CELERY_BROKER=amqp://rabbit:5672//
CELERY_BACKEND=rpc://
```
5) Run 
```docker-compose build```
6) Run 
```docker-compose up```  
By default, the application would run on port **8765**
[]