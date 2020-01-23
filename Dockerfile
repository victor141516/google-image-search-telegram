FROM python:3-alpine

COPY . /app
WORKDIR /app
RUN rm config_example.py && pip install -r requirements.txt
CMD [ "gunicorn", "-w4", "-b", ":8080", "bot:server" ]
