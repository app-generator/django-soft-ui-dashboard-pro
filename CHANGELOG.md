# Change Log

## [1.0.11] 2023-06-28
### Changes

- Bump UI Version, `v1.0.13`
  - Remove Duplicate asset: `nucleo-svg.css` 

## [1.0.10] 2023-06-27
### Changes

- Update `TEMPLATES` dir location
  - moved in the root of the project
- Added Sidebar  

## [1.0.9] 2023-06-27
### Changes

- Bump UI Version, `v1.0.12`
  - Remove `LOGIN` decorator for all routes 

## [1.0.8] 2023-06-20
### Changes

- Bump UI Version, `v1.0.11`
  - CleanUP MAP Files (JS, CSS)

## [1.0.7] 2023-06-13
### Changes

- Update `requirements.txt`
  - Specify the version for the private package

## [1.0.6] 2023-01-29
### Changes

- DOCS Update (readme). New sections:
  - `How to customize the theme`
  - Render deployment
- Configure the project to use `home/templates`
- Added `custom_footer` sample

## [1.0.5] 2023-01-01
### Changes

- Codebase Update: `theme-able pattern`
  - Desing is now installed as a package 
- Integrate [Django Soft PRO](https://github.com/app-generator/django-admin-soft-pro)
- CI/CD included via `Render`

## [1.0.4] 2022-06-28
### Improvements

- Bump UI to `Soft UI Dashboard PRO v1.0.8`
- Improved `Docker`
- Improved Codebase

## [1.0.3] 2021-12-14
### Improvements

- Bump UI: Soft UI Dashboard PRO v1.0.5

## [1.0.2] 2021-09-20
### Improvements 

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Codebase update
  - `assets` & `templates` moved to `apps` folder
  - `apps/base` renamed to `apps/home`

## [1.0.1] 2021-09-08
### Improvements & Fixes

- Bump Django Codebase to [v2.0.2](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - Dependencies update (all packages)
    - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.0] 2021-06-25
### Initial release

- UI: Soft UI Dashboard PRO v1.0.1
- [Django Codebase](https://github.com/app-generator/boilerplate-code-django-dashboard): v1.0.4
