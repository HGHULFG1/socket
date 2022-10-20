FROM python:3

FROM python:3
EXPOSE 12001
WORKDIR /app
COPY . /app/
CMD [ "python", "app-server.py" ]
