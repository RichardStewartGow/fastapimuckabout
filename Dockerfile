FROM python:3.10.11-slim

WORKDIR /docker-app

COPY ./requirements.txt /docker-app/requirements.txt

RUN pip install --no-cache-dir -r /docker-app/requirements.txt

COPY . /docker-app

CMD ["uvicorn", "app.application:app", "--host", "0.0.0.0", "--port", "80"]