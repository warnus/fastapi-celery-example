
from fastapi import FastAPI
from celery_worker import divide

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/work")
async def work(task_id: str, input_a: int, input_b: int):
    divide.apply_async([input_a, input_b], task_id=task_id)
    return {"message": "celery start"}

@app.get("/work_result")
async def work_result(task_id: str):
    result = divide.AsyncResult(task_id)
    return {"message": result.info}