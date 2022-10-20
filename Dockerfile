FROM python:3

FROM python:3
WORKDIR /app
COPY . /app/
CMD [ "python", "app-server.py" ]
