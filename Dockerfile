FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD gunicorn test_stripe.wsgi:application --bind 0.0.0.0:8000
