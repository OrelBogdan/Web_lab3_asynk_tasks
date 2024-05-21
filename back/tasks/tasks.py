from celery import shared_task, Task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime
import random
import math
import itertools
import exrex
import sympy


channel_layer = get_channel_layer()

class CallbackTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print(f"Task {task_id} is {retval}")


task1_counter = itertools.count(0)

@shared_task(name="task1", base=CallbackTask)
def task1():

    a = random.randint(1, 50)
    b = random.randint(1, 50)
    result = a*b
    info = {
        'task_name': 'Test task',
        'result': f"{task} = {result}",
        'finish time': datetime.now().astimezone().isoformat()
    }
    async_to_sync(channel_layer.group_send)('tasks', {'type': 'send_task_info', 'data': info})

    return result
