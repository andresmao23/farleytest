# farleytest
Django project for academic registration

Python version: Python 2.7
Django version: Django 1.9
Database: MySQL
MySQL connector: mysql-python 1.2.5
Frontend: Materialize

Create super user (open linux terminal or windows cmd into project folder):
>python manage.py createsuperuser (Follow steps)
>python manage.py migrate (Migrate models to MySQL database)
>python manage.py runserver (run server on localhost => http://127.0.0.1:8000/)

System links
1) http://127.0.0.1:8000/ (System Student login)
2) http://127.0.0.1:8000/admin/ (Admin panel => login as super user)

Academic System Functionalities
1) Add, Update, Delete (Students, Enrolls, Subjects, Teachers and Users)
