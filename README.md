py -m venv venv

git clone https://github.com/shoxxd221/wellcards.git

venv\Scripts\activate

pip install -r requirements.txt

cd wellcards

cd wellcards

py manage.py migrate

celery -A wellcards worker -l info -B

py manage.py runserver
