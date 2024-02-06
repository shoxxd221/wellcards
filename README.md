py -m venv venv

git clone https://github.com/shoxxd221/wellcards.git

venv\Scripts\activate

pip install -r requirements.txt

cd wellcards

cd wellcards

py manage.py migrate

celery -A wellcards worker -l info -B

python3 manage.py runserver --settings=wellcards.settings.dev
python3 manage.py runserver --settings=wellcards.settings.prod
