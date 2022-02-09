# FastAPI with Celery Simple Example

## How to Start

You can use poetry. Check poetry github [poetry](https://github.com/python-poetry/poetry)

## Install Dependency Packages
```
poetry install
```

## Start FastAPI Process
```
poetry run uvicorn main:app
```

## Start Celery Process
```
poetry run celery -A celery_app worker --loglevel=info
```

Now, access http://127.0.0.1:8000/docs on your brooser.


If you want to more detail guide, visit my blog [here](https://vlee.kr/4965)