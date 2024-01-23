# FastAPI Muck About

Designed to work with Docker and docker-compose (venv also possible if you have a local postgres install!)

## Install

```
cp .env.example .env
docker-compose build
docker-compose up
```

### Docker compose (needed for db tests)

```
docker-compose build 
docker-compose up
docker exec -it [containerId] /bin/sh
cd tests
pytest
```