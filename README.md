# [Soft Dashboard PRO Django](https://appseed.us/product/soft-ui-dashboard-pro/django/)

**Django** starter styled with **[Soft Dashboard PRO](https://appseed.us/product/soft-ui-dashboard-pro/django/)**, a premium `Bootstrap 5` KIT from `Creative-Tim`.
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

- 👉 [Soft UI Dashboard PRO Django](https://appseed.us/product/soft-ui-dashboard-pro/django/) - `Product Page`
- 👉 [Soft UI Dashboard PRO Django](https://django-soft-dash-pro.onrender.com/) - `LIVE Demo`

<br />

## Features

- `Up-to-date dependencies`
- Database: `SQLite`, PgSQL, MySql
- **Authentication**
  - `Session-Based authentication`
  - `Social Login`: **Github** & **Google**
- **User Extended profile**
- **API** via DRF
- DataTables
- Charts
- Celery
- File Manager
- i18n (internationalization) 
- `Docker`

![Soft Dashboard PRO Django](https://github.com/app-generator/priv-django-soft-ui-dashboard-enh/assets/51070104/108fab39-b351-41c9-b9b0-06e8fdde51f9)

<br />

## Start in `Docker`

> **Step 1** - Download the [code](https://appseed.us/product/soft-ui-dashboard-pro/django/) and unzip the sources (requires a `purchase`). 

```bash
$ unzip django-soft-ui-dashboard-pro.zip
$ cd django-soft-ui-dashboard-pro
```

<br />

> **Step 2** - Start the APP in `Docker`

```bash
# Optional (kill all existing containers)
$ docker container kill $(docker ps -q) ; docker container rm $(docker ps -a -q) ; docker network prune -f 
# Start the APP
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

## Create new `.env` from `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `MYSQL` credentials 
  - `DB_ENGINE`, default value = `mysql`
  - `DB_NAME`, default value = `appseed_db`
  - `DB_HOST`, default value = `localhost`
  - `DB_PORT`, default value = `3306`
  - `DB_USERNAME`, default value = `appseed_db_usr`
  - `DB_PASS`, default value = `pass`
- `OAuth` via Github
  - `GITHUB_ID`=<GITHUB_ID_HERE>
  - `GITHUB_SECRET`=<GITHUB_SECRET_HERE> 
- `OAuth` via Google
  - `GOOGLE_CLIENT_ID`=<GOOGLE_ID_HERE>
  - `GOOGLE_SECRET_KEY`=<GOOGLE_SECRET_HERE> 

<br />

## Manual Build

> Download the [code](https://appseed.us/product/soft-ui-dashboard-pro/django/) and unzip the sources (requires a `purchase`).  

```bash
$ unzip django-soft-ui-dashboard-pro.zip
$ cd django-soft-ui-dashboard-pro
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Create Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />

## Start Celery (async task)

- Make sure you have a Redis Server running: `redis://localhost:6379`
  - `$ redis-cli` and type `ping` 
- In the base directory inside `tasks_scripts` folder you need to write your scripts file.
- Run the celery command from the CLI.

```bash
$ export DJANGO_SETTINGS_MODULE="core.settings"  
$ celery -A apps.tasks worker -l info -B
```

- You will see a new route `Apps -> Tasks` in the sidebar.
- You can start and cancel any task from the UI.

<br />

## Enable Social Login 

> 👉 **Github Setup** - [Create an OAuth App](https://docs.github.com/en/developers/apps/building-oauth-apps/creating-an-oauth-app)

- SignIN to `Github`
- Access `Settings` -> `Developer Settings` -> `OAuth Apps`
- Edit your OAuth App
  - `App Name`
  - `App Description`
  - (mandatory) `HomePage`: `https://localhost:8000`
  - (mandatory) `Authorization callback URL`: `https://localhost:8000/`
  - Generate a new `secret key`

<br />

## Recompile SCSS  

> Tested with `NodeJS v14.0.0`

The SCSS/CSS files used to style the Ui are saved in the `static/assets` directory. 
In order to update the Ui colors (primary, secondary) this procedure needs to be followed. 

```bash
$ yarn # install modules
$ # # edit variables 
$ vi static/assets/scss/soft-ui-dashboard/custom/_variables.scss 
$ gulp # SCSS to CSS translation
```

The `_variables.scss` content defines the `primary` and `secondary` colors: 

```scss
$primary:       #cb0c9f !default; // EDIT for customization
$secondary:     #8392AB !default; // EDIT for customization
$info:          #17c1e8 !default; // EDIT for customization
$success:       #82d616 !default; // EDIT for customization
$warning:       #fbcf33 !default; // EDIT for customization
$danger:        #ea0606 !default; // EDIT for customization
```

<br />

## Codebase

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/              # Implements app configuration
   |    |-- settings.py   # Defines Global Settings
   |    |-- wsgi.py       # Start the app in production
   |    |-- urls.py       # Define URLs served by all apps/nodes
   |
   |-- home/              # Serves all pages from the UI Kit  
   |
   |-- apps/
   |    |
   |    |-- common/       # Assets used by all APPS (models, helpers)
   |    |-- users/        # Handles Auth Flow
   |    |-- api/          # DRF API
   |    |-- charts/       # Charts APP
   |    |-- tables/       # DataTables APP
   |    |-- tasks/        # Celery App
   |
   |-- templates/         # Pages & Templates   
   |-- assets/            # Static Assets [ JS, CSS, images ]   
   |
   |-- requirements.txt   # Development modules - SQLite storage
   |
   |-- .env               # Environment
   |-- env.sample         # Environment Sample
   |
   |-- manage.py          # Django Manager File
   |
   |-- ************************************************************************
```

<br />

---
[Soft Dashboard PRO Django](https://appseed.us/product/soft-ui-dashboard-pro/django/) - Starter crafted by **[AppSeed](https://appseed.us/)**.
