FROM python:3.8.2
RUN pip install pipenv
RUN apt-get update && apt-get install -y netcat
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pip install -r requirements.txt
CMD python3 prova.py