FROM python:2.7-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "gunicorn", "-w4", "-b", ":8080", "bot:server" ]
