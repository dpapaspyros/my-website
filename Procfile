web: python manage.py collectstatic --no-input; NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn project.wsgi
release: python manage.py migrate