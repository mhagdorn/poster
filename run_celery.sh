export POSTER_ADMIN=poster@poster.org
python3 -m celery worker -A poster.celery --loglevel=info
