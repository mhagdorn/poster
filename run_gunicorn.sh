export FLASK_APP=poster
export SCRIPT_NAME=/poster
export FLASK_ENV=development
export MAIL_SERVER=localhost
export MAIL_PORT=8025

#. secret.sh

gunicorn3 --log-level debug --bind 0.0.0.0:5000 poster:app
