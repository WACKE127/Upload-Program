wsl
conda create -n django python=3.12
conda activate django
pip install django
django-admin startproject upload
cd upload
python manage.py startapp uploadapp
