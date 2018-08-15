FROM python:2.7
ADD . /millionaire
WORKDIR /millionaire
RUN pip install -r requirements.txt
RUN bash -c 'python manage.py collectstatic <<<yes'
EXPOSE 8000
CMD gunicorn -b 0.0.0.0:8000 millionaire.wsgi:application --log-level=debug --log-file=- 
