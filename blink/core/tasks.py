from celery import Task

class BlinkTask(Task):
    pass

class BlinkInternalTask(BlinkTask):
    pass

class BlinkWebTask(BlinkTask):
    pass
