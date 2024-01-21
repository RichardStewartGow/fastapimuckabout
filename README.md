#FastAPI Muck About


##Install

###Local with Venv

windows

###Docker compose


##Tests
###Local with Venv

windows/venv



###Docker compose (needed for db tests)

```
docker-compose up
docker exec -it [containerId] /bin/sh
cd tests
pytest
```