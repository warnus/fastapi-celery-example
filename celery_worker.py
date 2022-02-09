from celery_app import celery_task
import time

@celery_task.task
def divide(x, y):    
    time.sleep(5)
    return x / y
