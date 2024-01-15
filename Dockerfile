FROM python3.10

WORKDIR /docker-app

COPY ./requirements.txt /docker-app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /docker-app/requirements.txt

COPY . /docker-app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]