wsl
conda create -n django python=3.12
conda activate django
pip install django
django-admin startproject upload
cd upload
python manage.py startapp uploadapp

sudo apt-get install postgresql postgresql-contrib
systemctl status postgresql@10-main.service

sudo -u postgres createdb uploadsql
sudo -u postgres psql
\c uploadsql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE ROLE admin WITH LOGIN PASSWORD 'pass';
GRANT ALL PRIVILEGES ON DATABASE uploadsql TO admin;
CREATE ROLE web NOLOGIN;

CREATE TABLE file_metadata (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    file_size BIGINT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    last_accessed TIMESTAMP,
    permissions VARCHAR(50),
    owner VARCHAR(100)
);

sudo apt-get install libpq-dev python3-dev
pip install psycopg