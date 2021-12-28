FROM python:3.8-bullseye

RUN python3 -m venv /opt/venv

COPY ./app /app 
COPY ./requirements.txt /app/requirements.txt

RUN . /opt/venv/bin/activate && pip install -r /app/requirements.txt

WORKDIR /app

CMD . ../opt/venv/bin/activate && exec python app.py


