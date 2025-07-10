cd ..
env-beta-be\Scripts\activate
cd pe_siakad_backend
pip install -r requirements.txt

python manage.py makemigrations users
python manage.py migrate


python manage.py runserver


Swagger: http://127.0.0.1:8000/swagger/
Admin Panel (jika sudah dibuat superuser): http://127.0.0.1:8000/admin/