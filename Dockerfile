FROM python:3.12.1-slim

WORKDIR /docker-app

COPY ./requirements.txt /docker-app/requirements.txt

RUN pip install --no-cache-dir -r /docker-app/requirements.txt

COPY . /docker-app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]