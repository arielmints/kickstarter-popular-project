# kickstarter-popular-project

This project is a home project mission - A KickStarter popular projects view.


### Installing the dependencies

Before running the project, please install the dependencies as they appear in the requirements.txt file.

### Migrate DB

To create the db with the right table, run django migration in the main project folder

```
manage.py migrate
```

### Run Django server with your favorite PORT

```
manage.py runserver PORT
```
This will run the server on localhost:PORT, you can now enter http://localhost:8080/projects/ in your browser and watch the UI with the pre built DB.

### Set scheduled task for scrapping every hour

The commaned you need to schedule is scrapy's crawl command

```
scrapy crawl kickstarter
```



