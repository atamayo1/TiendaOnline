## First command to start a project with Django

    django-admin startproject TiendaOnline

## Second command to generate app

    python3 manage.py startapp gestionPedidos

## Third command to generate db.sqlite3

    python3 manage.py makemigrations

## create sql of the model to sqlite

    python3 manage.py sqlmigrate name_app number_migration(0001)

## Migrate the code sql of the model

    python3 manage.py migrate

