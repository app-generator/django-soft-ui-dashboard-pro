# [Django Material PRO](https://github.com/app-generator/django-material-dashboard-pro) `Starter`

**Django** starter styled with **Material Design PRO**, a premium `Bootstrap 5` KIT from [Creative-Tim](https://bit.ly/3fKQZaL)
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 👉 [Django Material PRO](https://django-material-dashboard-pro.onrender.com) - `LIVE Demo` on Render
- 🚀 [Support](https://appseed.us/support/) via `Email` & `Discord`

<br />

## Purchase Product via `GUMROAD`

- 🛒 `Personal License`: **[PAY - $49](https://appseed.gumroad.com/l/django-mat-pro)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-personal): `Support & Updates: 6mo`
  
- 🛒 `StartUp License`: **[PAY - $99](https://appseed.gumroad.com/l/django-mat-pro-startup)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-startup): `Support & Updates: 12mo`
  
- 🛒 `Company License`: **[PAY - $199](https://appseed.gumroad.com/l/django-mat-pro-company)** (payment link)
  - Usage [terms](https://github.com/app-generator/license-personal): `Support & Updates: Lifetime`, **SaaS** products allowed
  
<br />

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Material](https://github.com/app-generator/django-admin-material-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Deployment-Ready` for Render 

<br />

![Material Dashboard BS5 - Modern Dashboard design by Creative-Tim.](https://user-images.githubusercontent.com/51070104/209104783-22f04139-8919-457c-b21d-7383d57f07b1.png)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-material-dashboard-pro.git
$ cd django-material-dashboard-pro
```

<br />

> Export `GITHUB_TOKEN` in the environment. The value is provided by AppSeed during purchase. 

This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-material-pro`

```bash
$ export GITHUB_TOKEN='TOKEN_HERE'  # for Linux, Mac
$ set GITHUB_TOKEN='TOKEN_HERE'     # Windows CMD
$ $env:GITHUB_TOKEN = 'TOKEN_HERE'  # Windows powerShell 
```

<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Edit the `.env` using the template `.env.sample`. 

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

## Screenshots

![Theme Material Dashboard PRO - Main (Dark-Mode active), crafted by AppSeed.](https://user-images.githubusercontent.com/51070104/209695422-7863697f-e6c5-4b08-b395-422074e399df.jpg)

<br />

> [Django Admin Material PRO](https://github.com/app-generator/django-admin-material-pro) - `Calender` Page

![Theme Material Dashboard PRO - Calender Page, crafted by AppSeed.](https://user-images.githubusercontent.com/51070104/209695529-f4cea8ee-68d9-4658-bb54-110ff530c8da.jpg)

<br />

> [Django Admin Material PRO](https://github.com/app-generator/django-admin-material-pro) - `Automotive` Page

![Theme Material Dashboard PRO - Automotive Page, crafted by AppSeed.](https://user-images.githubusercontent.com/51070104/209695692-e681b3c8-fca8-4ebf-8803-2795bcd8f7d1.jpg)

<br />

---
[Django Material PRO](https://github.com/app-generator/django-material-dashboard-pro) - Minimal **Django** starter provided by **[AppSeed](https://appseed.us/)**
