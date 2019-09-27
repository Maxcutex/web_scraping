# Introduction

This is a simple api setup to execute the web scraping functionality of searching a search engine and scraping the
of the search

## Setup
To use this app, clone this repo into `project_root`, ensure your python environments are configured and activated.

Run: `$ pip install -r requirements.txt`

This will pull and install all vessel dependencies into the current or active virtual environment. Copy the content of 
`.env_sample` into `.env` and set proper environment variables.


## Start Server
In the `project_root` with environment activated, 

Run: `$ python run.py runserver`

Open your browser and enter `http://127.0.0.1:5000/api/v1/`



## Tests
Ofcourse there's support for testing using pytest.

To run tests `$ python -m pytest`

## Folder and Code Structure
```
|-- project_root
    |-- app/
        |-- blueprints/
            |-- base_blueprint.py
        |-- controllers/
            |-- __init__.py
            |-- base_controller.py
            |-- home_controller.py
        |-- models/
            |-- __init__.py
            |-- base_model.py
            |-- web_scraper.py
        |-- repositories/
            |-- __init__.py
            |-- base_repo.py
        |-- utils/
            |-- __init__.py
            |-- auth.py
            |-- security.py
        |-- __init__.py
        |-- test_db.db
    |-- config/
        |-- __init__.py
        |-- env.py
    |-- factories
        |-- __init__.py
    |-- migrations
    |-- tests
        |-- integration/
            |-- endpoints/
                |-- __init__.py
                |-- test_dummy_endpoints.py
            |-- __init__.py
        |-- unit
            |-- repositories/
            |-- test_auth.py
        |-- __init__.py
        |-- base_test_case.py
    |-- .env_sample
    |-- .gitignore
    |-- LICENSE
    |-- Procfile
    |-- pytest.ini
    |-- README.md
    |-- requirements.txt
    |-- run.py
    |-- vessel.py
```
## Procfile
For Heroku enthusiast. Delete if you'd not be deploying to Heroku.

